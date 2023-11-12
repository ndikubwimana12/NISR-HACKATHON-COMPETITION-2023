# Home.py
import pandas as pd
import streamlit as st
import plotly.express as px


def home():
    st.sidebar.success("# Select Page above.  :point_up_2:")

    # Use HTML to create the layout with shadow effect
    st.markdown(
        """
        <style>
            .shadow-box {
                width: 230px;
                height: 300px;
                border: solid 2px black;
                border-radius: 10px;
                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
                margin: 10px;
            }
        </style>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 0;">
            <div class="shadow-box">
            <p><h3>HOW TO NAVIGATE TO NISR - LABOR FORCE SURVEY'S DASHBOARD</h3></p>
            </div>
            <div class="shadow-box">
            <p>Here Are few steps that can guides you to navigate this Dashboard: </p>
            <p>
            <ol>
                <li>Select Page To Navigate In Side Bar Dropdown | On Left Side 👈</li>
                <li>Choose the page to visit and scroll down to see all information to the page.</li>
            </oli>
            </p>
            </div>
            <div class="shadow-box">
            <ol start="3">
                <li>On Selected Page, You Need to Justify or Filter The Content to display By Selecting Many or one Option | On Left Side 👈</li>
                <li>The Data Are Displayed by using Line Chart 📈, Bar chart 📊, and Pie chart, so as to make clear understandable for readers</li>
            </oli>
            </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Uncomment the next line if you want to test this code alone
# home()
