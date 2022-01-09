import streamlit as st

st.set_page_config(page_title="Space Invaders")

hide_st_style = """
            <head>
            <meta charset="UTF-8" />
            <title>Space Invaders</title>
            <style>
                canvas {
                 width: 20%;
                }
             </style>

            </head>
            <body>
                <script src="https://cdn.jsdelivr.net/npm/phaser@3.16.2/dist/phaser.min.js"></script>
            <script defer src="game.js"></script>
            </body>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)