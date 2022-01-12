import streamlit as st
from Multi_App import MultiApp
from apps import Home, titanic, space# import your app modules here

st.set_page_config(page_title="My Projects")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


app = MultiApp()

st.markdown("""
# My Projects
""")

# Add all your application here
app.add_app("About Me", Home.app)
app.add_app("Titanic Log Regression", titanic.app)
app.add_app("Space Invaders", space.app)
# The main app
app.run()
