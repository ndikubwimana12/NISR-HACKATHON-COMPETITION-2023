# dashboard.py
import streamlit as st
from home import home
from sheet1 import sheet1
from sheet2 import sheet2
from sheet3 import sheet3
from sheet4 import sheet4
from sheet5 import sheet5
from sheet6 import sheet6

# Set page configuration only once
st.set_page_config(
    page_title="Labour Force Survay Dashboard",
    page_icon=":bar_chart:",
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
            font-size: 44px;
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
        <h1 class="header-title"> NISR - Labor Force Survey 2022</h1>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo
st.sidebar.image("logo.jpg", use_column_width=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page_options = ["🏠 Home",
                "📊 Summary Of Labour Force Indicators by District, RLFS 2022",
                "🌆 Population by Level of Education, RLFS 2022",
                "📖 Unemployed population by Level of Education, RLFS 2022",
                "📈 Unemployed population By Age Group, RLFS 2022",
                "💼 Employement By Economic Activities Summary,				RLFS 2022",
                "🏬 Labour market indicators and educational type (general and Technical) , RLFS 2022"]
selected_page = st.sidebar.selectbox("Select Page Here :point_down:", page_options)

# Main content based on selected page
if selected_page == "📊 Summary Of Labour Force Indicators by District, RLFS 2022":
    sheet1()
elif selected_page == "🌆 Population by Level of Education, RLFS 2022":
    sheet2()
elif selected_page == "📈 Unemployed population By Age Group, RLFS 2022":
    sheet3()
elif selected_page == "📖 Unemployed population by Level of Education, RLFS 2022":
    sheet4()
elif selected_page == "💼 Employement By Economic Activities Summary,				RLFS 2022":
    sheet5()
elif selected_page == "🏠 Home":
    home()
elif selected_page == "🏬 Labour market indicators and educational type (general and Technical) , RLFS 2022":
    sheet6()

# Custom styling for the footer
st.markdown(
    """
    <style>
    .footer{
            background-color: #2e3c7f;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            color: white;
        }
        .footer-container {
            display: grid;
	        grid-template-columns: repeat(3, 1fr);
            background-color: #2e3c7f;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            color: white;
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
        .p{
        margin: 0 5%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer

st.markdown(
    """
     <div class="footer">
    <div class="footer-container">
        <div class="footer-text1">For more information, visit <a href="https://www.nisr.gov.rw/" 
        style="color: white; text-decoration: none;">NISR website | https://www.nisr.gov.rw/</a></div>
        <div class="footer-text2">Contact us at info@nisr.gov.rw</div>
        <div class="footer-text3">© 2023 National Institute of Statistics of Rwanda. All rights reserved.</div>
        <br>
        
    </div>
    <p class="p"> &copy developed by Byte Canvas Group</p>
    </div>
    """,
    unsafe_allow_html=True
)
