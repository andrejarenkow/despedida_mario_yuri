import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from io import BytesIO

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
dados_filtrados = dados#[dados['Seu nome'] == remetente]


# Combinar textos das colunas 'Mensagem para o MÁRIO' e 'Mensagem para o YURI'
mensagens_mario = ". ".join(dados_filtrados['Mensagem para o MÁRIO '].dropna())
mensagens_yuri = ". ".join(dados_filtrados['Mensagem para o YURI'].dropna())
mensagens = mensagens_mario + " " + mensagens_yuri

# Lista de stopwords em português
stopwords_portugues = set(STOPWORDS)
stopwords_personalizadas = {
    'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 
    'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 
    'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 
    'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 
    'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 
    'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 
    'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 
    'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 
    'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 
    'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 
    'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 
    'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 
    'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 
    'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 
    'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 
    'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 
    'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 
    'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 
    'temos', 'têm', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 
    'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 
    'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam'
}
stopwords_portugues.update(stopwords_personalizadas)

# Gerar a nuvem de palavras
wordcloud = WordCloud(stopwords=stopwords_portugues, width=400, height=200, background_color='black', ).generate(mensagens)

# Gerar a nuvem de palavras
wordcloud = WordCloud(width=400, height=200, background_color='black', ).generate(mensagens)

# Mostrar a nuvem de palavras no Streamlit
st.subheader('Nuvem de Palavras')
fig, ax = plt.subplots(figsize=(5, 2.5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

buf = BytesIO()
fig.savefig(buf, format="png")
st.image(buf)
