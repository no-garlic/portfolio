"""
Blog module for portfolio website.

This module contains the code to display the blog section of the portfolio,
showcasing articles, posts, and other written content.
"""

import streamlit as st
import streamlit_antd_components as sac

from utils import load_markdown


def show_blog():
    """
    Display the blog section of the portfolio.
    
    Renders a header for the blog section in the Streamlit app.
    """
    with st.container(border=True):
        #st.header("Blog")
        #st.markdown("---")

        tree_column, content_column = st.columns([1, 3])

        with tree_column:
            with st.container(border=False):
                sac.menu([
                    sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
                    sac.MenuItem('products', icon='box-fill', children=[
                        sac.MenuItem('apple', icon='apple'),
                        sac.MenuItem('other', icon='git', description='other items', children=[
                            sac.MenuItem('google', icon='google', description='item description'),
                            sac.MenuItem('gitlab', icon='gitlab'),
                            sac.MenuItem('wechat', icon='wechat'),
                        ]),
                    ]),
                    sac.MenuItem('disabled', disabled=True),
                    sac.MenuItem(type='divider'),
                    sac.MenuItem('link', type='group', children=[
                        sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
                        sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
                    ]),
                ], size='xl', variant='left-bar', open_all=True, return_index=True)


        with content_column:
            with st.container(border=False):
                st.markdown(load_markdown("test"))





"""
    def build_tree_structure():
        items = [
            sac.TreeItem("item 1"),
            sac.TreeItem("item 2", children=[
                sac.TreeItem("item 2a"),
                sac.TreeItem("item 2b")
            ]),
            sac.TreeItem("item 3"),        
        ]
        return items


    col1, col2 = st.columns([1, 3]);

    with col1:
        with st.container(height=1000, border=True):
            sac.menu([
                sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
                sac.MenuItem('products', icon='box-fill', children=[
                    sac.MenuItem('apple', icon='apple'),
                    sac.MenuItem('other', icon='git', description='other items', children=[
                        sac.MenuItem('google', icon='google', description='item description'),
                        sac.MenuItem('gitlab', icon='gitlab'),
                        sac.MenuItem('wechat', icon='wechat'),
                    ]),
                ]),
                sac.MenuItem('disabled', disabled=True),
                sac.MenuItem(type='divider'),
                sac.MenuItem('link', type='group', children=[
                    sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
                    sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
                ]),
            ], size='xl', variant='left-bar', open_all=True, return_index=True)


            selected = sac.tree(items=build_tree_structure(), 
                                label='Notebooks', 
                                index=0, 
                                align='left', 
                                size='xl',
                                icon='table', 
                                open_all=True, 
                                checkbox=False, 
                                key="selected_tree_item")


    with col2:
        with st.container(height=1000, border=True):
            st.header("A dog")

            sac.buttons([sac.ButtonsItem(icon=sac.BsIcon(name='house', size=150))], align='center', variant='text', index=None)

            st.image("images/mike.jpeg")

"""        