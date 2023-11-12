# sheet2.py
import pandas as pd
import streamlit as st
import plotly.express as px

def sheet2():
    df = pd.read_excel(
        io='RLFS Tables_ Annual_2022.xlsx',
        engine='openpyxl',
        sheet_name='population',
        skiprows=1
    )
    st.write("# Population by sex, age group and urban/rural area, RLFS 2022")
    st.write(df)

    # Convert column names to strings explicitly
    df.columns = df.columns.astype(str)

    # --- side bar ------
    st.sidebar.header("Please Filter Here: ")
    if "Population" in df.columns:  # Corrected column name
        district_options = df["Population"].unique()  # Corrected column name
        selected_districts = st.sidebar.multiselect(
            "Select population(s): ",
            options=district_options,
            default=district_options
        )
    else:
        st.sidebar.write("The 'Population' column is not present in the DataFrame.")

    year_columns = [col for col in df.columns if col != 'Population']
    if year_columns:
        selected_years = st.sidebar.multiselect(
            "Select Age Range(s): ",
            options=year_columns,
            default=year_columns
        )
        filtered_df = df[df['Population'].isin(selected_districts)][['Population'] + selected_years]

        for year in selected_years:
            fig = px.pie(filtered_df, names='Population', values=year, title=f'{year} Data | for Selected Population Based On Age Range')  # Corrected parameter names
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No valid year columns found in the DataFrame.")
