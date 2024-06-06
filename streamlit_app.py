import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Até mais, guris!",
    page_icon=":smile:",
    layout="wide",
    initial_sidebar_state='collapsed')


dados = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vQo2ORfqALtxZziexogUMaFnFlgWMm1llUVjWX6kB4i4uapOJ39lShGcO2M9R_ketNORU22Po6KkTwX/pub?output=xlsx')
dados
