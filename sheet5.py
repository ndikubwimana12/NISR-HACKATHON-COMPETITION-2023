# sheet1.py
import pandas as pd
import streamlit as st
import plotly.express as px

def sheet5():
    df = pd.read_excel(
        io='RLFS Tables_ Annual_2022.xlsx',
        engine='openpyxl',
        sheet_name='Sheet5',
    )
    st.write("Dtaset on table 1")
    st.write(df)
    # Convert column names to strings explicitly
    df.columns = df.columns.astype(str)

    # --- side bar ------
    st.sidebar.header("Please Filter Here: ")
    if "population" in df.columns:
        district_options = df["population"].unique()
        selected_district = st.sidebar.multiselect(
            "Select population(s): ",
            options=district_options,
            default=district_options
        )
    else:
        st.sidebar.write("The 'population' column is not present in the DataFrame.")

    year_columns = [col for col in df.columns if col != 'population']
    if year_columns:
        selected_years = st.sidebar.multiselect(
            "Select year(s): ",
            options=year_columns,
            default=year_columns
        )
        filtered_df = df[df['population'].isin(selected_district)][['population'] + selected_years]

        for year in selected_years:
            fig = px.bar(filtered_df, x='population', y=year, title=f'{year} Data for Selected Districts')
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No valid year columns found in the DataFrame.")

