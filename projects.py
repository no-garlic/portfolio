"""
Projects module for portfolio website.

This module contains the code to display the projects section of the portfolio,
including project descriptions loaded from markdown files.
"""

import streamlit as st

from utils import load_markdown


def show_projects():
    """
    Display the projects section of the portfolio.
    
    Renders a header for the projects section and loads project content
    from a markdown file for display in the Streamlit app.
    """
    st.header("Projects")
    st.markdown("---")

    md = load_markdown("test")
    st.markdown(md)
