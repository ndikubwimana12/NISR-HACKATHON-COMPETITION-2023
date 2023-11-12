# sheet6.py
import pandas as pd
import streamlit as st
import plotly.express as px

def sheet6():
    df = pd.read_excel(
        io='RLFS Tables_ Annual_2022.xlsx',
        engine='openpyxl',
        sheet_name='labourfource',
        skiprows=1,
        nrows=22,
    )

    st.write("# Labour market indicators and educational type (general and Technical) , RLFS 2022")
    st.write(df)

    # Convert column names to strings explicitly
    df.columns = df.columns.astype(str)

    # --- side bar ------
    st.sidebar.header("Please Filter Here: ")
    column_name = "Attainemnt status of vocational and general trainings"
    if column_name in df.columns:
        district_options = df[column_name].unique()
        selected_district = st.sidebar.multiselect(
            f"Select {column_name}(s): ",
            options=district_options,
            default=district_options
        )
    else:
        st.sidebar.write(f"The '{column_name}' column is not present in the DataFrame.")

    year_columns = [col for col in df.columns if col != column_name]
    if year_columns:
        selected_years = st.sidebar.multiselect(
            "Select Market Indicator(s): ",
            options=year_columns,
            default=year_columns
        )
        filtered_df = df[df[column_name].isin(selected_district)][[column_name] + selected_years]

        for year in selected_years:
            fig = px.bar(
                filtered_df,
                x=column_name,
                y=year,
                title=f'{year} Data | For {column_name}',
                color=column_name,  # Assign different colors for each category
                labels={column_name: 'Attainemnt status of vocational and general trainings', year: 'Unemployed Number'},
                hover_data={column_name: True, year: ':.0f'},  # Include additional information on hover
                template='plotly_dark'  # Use dark template
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No valid year columns found in the DataFrame.")

