import streamlit as st
from streamlit_option_menu import option_menu
import base64

from aboutme import show_aboutme
from certification import show_certification
from education import show_education
from jobhistory import show_jobhistory
from projects import show_projects
from blog import show_blog


st.set_page_config(page_title="Michael Petrou - Portfolio", layout="wide", initial_sidebar_state="expanded", page_icon="💻")

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
    
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

mike_img = load_image("mike.jpeg")

mike_img_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{mike_img}" class="logo">
    </div>
"""

st.sidebar.markdown(mike_img_html, unsafe_allow_html=True)

nav_funcs = {
    "About me": show_aboutme,
    "Projects": show_projects,
    "Certification": show_certification,
    "Job History": show_jobhistory,
    "Education": show_education,
    "Blog": show_blog
}

with st.sidebar:
    pages = list(nav_funcs.keys())
    nav_tab_op = option_menu(
        menu_title="Michael Petrou",
        options=pages,
        icons=['person-fill', 'files', 'file-text', 'person-square', 'mortarboard', 'pencil'],
        menu_icon="file-earmark-text",
        default_index=0,
        styles={
            "menu-title": {"font-size": "26px", "font-weight": "700" },
            "container": {"padding": "20"},
            "icon": {"color": "#fff", "font-size": "22px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"4px", "--hover-color": "#c99"},
            "nav-link-selected": {"background-color": "darkred"},
        }
    )

for key, value in nav_funcs.items():
    if nav_tab_op == key:
        value()
