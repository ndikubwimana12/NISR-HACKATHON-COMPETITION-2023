import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def sheet1():
    df = pd.read_excel(
        io='RLFS Tables_ Annual_2022.xlsx',
        engine='openpyxl',
        sheet_name='summary',
        skiprows=1,
        nrows=41,
        converters={'Employed': pd.to_numeric, 'Unemployed': pd.to_numeric}
    )
    st.write("# Summary labour force indicators by District, RLFS 2022")
    st.write(df)
    # Convert column names to strings explicitly
    df.columns = df.columns.astype(str)

    # --- side bar ------
    st.sidebar.header("Please Select District Here :point_down: ")

    if "population" in df.columns:
        district_options = df["population"].unique()
        selected_districts = st.sidebar.multiselect(
            "Select districts To Get The Estmated Number of Employed and Unemployed: ",
            options=district_options
        )
    else:
        st.sidebar.write("The 'District' column is not present in the DataFrame.")
    st.write("# Select Districts In Side Bar :point_left:")

    if "Employed" in df.columns and "Unemployed" in df.columns:
        filtered_df = df[df['population'].isin(selected_districts)]

        fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=("Employed Data", "Unemployed Data"))

        for population in selected_districts:
            fig.add_trace(go.Bar(x=filtered_df[filtered_df['population'] == population]['Employed'], y=[population], orientation='h', text=filtered_df[filtered_df['population'] == population]['Employed'], textposition='inside'), row=1, col=1)

            fig.add_trace(go.Bar(x=filtered_df[filtered_df['population'] == population]['Unemployed'], y=[population], orientation='h', text=filtered_df[filtered_df['population'] == population]['Unemployed'], textposition='inside'), row=1, col=2)

        fig.update_layout(showlegend=False, height=600, width=800)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("The 'Employed' or 'Unemployed' column is not present in the DataFrame.")


