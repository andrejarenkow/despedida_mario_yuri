import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Até mais, guris!",
    page_icon=":smile:",
    layout="wide",
    initial_sidebar_state='collapsed'
)

st.title('Mensagens de Carinho - Mário e Yuri')

# Carregar os dados
dados = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vQo2ORfqALtxZziexogUMaFnFlgWMm1llUVjWX6kB4i4uapOJ39lShGcO2M9R_ketNORU22Po6KkTwX/pub?output=xlsx')
dados

# Exibir número de mensagens
st.metric('Número de mensagens', len(dados))

# Caixa de seleção para filtrar mensagens por remetente
remetente = st.selectbox('Quem mandou a mensagem?', options=sorted(dados['Seu nome'].unique()))

# Filtrar dados pelo remetente selecionado
dados_filtrados = dados[dados['Seu nome'] == remetente]

# Combinar textos das colunas 'Mensagem para o MÁRIO' e 'Mensagem para o YURI'
mensagens_mario = " ".join(dados_filtrados['Mensagem para o MÁRIO'].dropna())
mensagens_yuri = " ".join(dados_filtrados['Mensagem para o YURI'].dropna())
mensagens = mensagens_mario + " " + mensagens_yuri

# Gerar a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(mensagens)

# Mostrar a nuvem de palavras no Streamlit
st.subheader('Nuvem de Palavras')
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)


