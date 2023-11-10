# pcall.py
import streamlit as st
from home import home
from sheet1 import sheet1
from sheet2 import sheet2
from sheet3 import sheet3
from sheet4 import sheet4
from sheet5 import sheet5

# Set page configuration only once
st.set_page_config(
    page_title="NISR",
    page_icon=":chart:",
    layout="wide"
)

# Custom styling for the header
st.markdown(
    """
    <style>
        .header-container {
            background-color: #2e3c7f;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
            height: 100px;
            text-overflow: hidden;
        }
        .header-title {
            color: white;
            font-size: 24px;
        }
       .link a{
            color: white;
            font-size: 16px;
            text-decoration: none;
            margin: 0 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <div class="header-container">
        <h1 class="header-title">NISR - Labor Force Survey 2022</h1>
        <div class="link">
        <a href="#Home">Home</a>
        <a href="Sheet1.py">Sheet1</a>
        <a href="Sheet2.py">Sheet2</a>
        <a href="#Sheet3">Sheet3</a>
        <a href="#Sheet4">Sheet4</a>
        <a href="#Sheet5">Sheet5</a>
        </div>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo
st.sidebar.image("logo.jpg", use_column_width=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page_options = ["Home", "Sheet1", "Sheet2", "Sheet3", "Sheet4", "Sheet5"]
selected_page = st.sidebar.selectbox("Select Page", page_options)

# Main content based on selected page
if selected_page == "Sheet1":
    sheet1()
elif selected_page == "Sheet2":
    sheet2()
elif selected_page == "Sheet3":
    sheet3()
elif selected_page == "Sheet4":
    sheet4()
elif selected_page == "Sheet5":
    sheet5()
elif selected_page == "Home":
    home()

# Custom styling for the footer
st.markdown(
    """
    <style>
        .footer-container {
            display: grid;
	        grid-template-columns: repeat(3, 1fr);
            background-color: #2e3c7f;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
        }
        .footer-text1 {
            color: white;
            font-size: 14px;
        }
        .footer-text2 {
            color: white;
            font-size: 14px;
        }
        .footer-text3 {
            color: white;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer

st.markdown(
    """
    <div class="footer-container">
        <div class="footer-text1">For more information, visit <a href="https://www.nisr.gov.rw/" 
        style="color: white; text-decoration: none;">NISR website | https://www.nisr.gov.rw/</a></div>
        <div class="footer-text2">Contact us at info@nisr.gov.rw</div>
        <div class="footer-text3">© 2023 National Institute of Statistics of Rwanda. All rights reserved.</div>
        <img src="logo.jpg" alt="Logo" width="100" style="margin-top: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)
