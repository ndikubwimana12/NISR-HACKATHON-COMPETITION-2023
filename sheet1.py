# sheet1.py
import pandas as pd
import streamlit as st
import plotly.express as px

def sheet1():
    df = pd.read_excel(
        io='RLFS Tables_ Annual_2022.xlsx',
        engine='openpyxl',
        sheet_name='Sheet1',
    )

    # Convert column names to strings explicitly
    df.columns = df.columns.astype(str)

    # --- side bar ------
    st.sidebar.header("Please Filter Here: ")
    if "District" in df.columns:
        district_options = df["District"].unique()
        selected_district = st.sidebar.multiselect(
            "Select district(s): ",
            options=district_options,
            default=district_options
        )
    else:
        st.sidebar.write("The 'District' column is not present in the DataFrame.")

    year_columns = [col for col in df.columns if col != 'District']
    if year_columns:
        selected_years = st.sidebar.multiselect(
            "Select year(s): ",
            options=year_columns,
            default=year_columns
        )
        filtered_df = df[df['District'].isin(selected_district)][['District'] + selected_years]

        for year in selected_years:
            fig = px.bar(filtered_df, x='District', y=year, title=f'{year} Data for Selected Districts')
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No valid year columns found in the DataFrame.")
