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

# Carregar os dados
dados = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vQo2ORfqALtxZziexogUMaFnFlgWMm1llUVjWX6kB4i4uapOJ39lShGcO2M9R_ketNORU22Po6KkTwX/pub?output=xlsx')
#dados

container1 = st.container()
with container1:
    col1, col2, col3 = st.columns([2,9,2])
    with col1:
        st.write('<div style="margin-top: 15px;">', unsafe_allow_html=True)
        st.write('</div>', unsafe_allow_html=True)
        st.write('<div style="display: flex; justify-content: left;">', unsafe_allow_html=True)
        st.image(r"yuri.jpg", width=200)
        st.write('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<h1 style="text-align: center;color:#ffffff;font-size:45px;margin-top:0px;margin-bottom:0px;">{"Mensagens de Carinho"}</h1>', unsafe_allow_html=True)    
        st.markdown(f'<h1 style="text-align: center;color:#ffffff;font-size:30px;margin-top:0px;margin-bottom:0px;">{"Colegas e ex colegas de trabalho do CEVS e da SES-RS"}</h1>', unsafe_allow_html=True)
        st.markdown(f'<h1 style="text-align: center;color:#ffffff;font-size:20px;margin-top:0px;margin-bottom:0px;">{f"Já são {len(dados)} mensagens!"}</h1>', unsafe_allow_html=True)
        
    with col3:    
        st.write('<div style="display: flex; justify-content: right;">', unsafe_allow_html=True)
        st.image(r'mario.png', width=250)
        st.write('</div>', unsafe_allow_html=True)


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
    'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam','Yuri','Mário'
}
stopwords_portugues.update(stopwords_personalizadas)

# Gerar a nuvem de palavras
wordcloud_yuri = WordCloud(stopwords=stopwords_portugues, width=400, height=200, background_color='black', ).generate(mensagens_yuri)

wordcloud_mario = WordCloud(stopwords=stopwords_portugues, width=400, height=200, background_color='black', ).generate(mensagens_mario)



col_yuri, col_mario = st.columns(2)

# Mostrar a nuvem de palavras no Streamlit
col_yuri.subheader('Nuvem de Palavras Yuri')
fig, ax = plt.subplots(figsize=(5, 2.5))
ax.imshow(wordcloud_yuri, interpolation='bilinear')
ax.axis('off')

buf_yuri = BytesIO()
fig.savefig(buf_yuri, format="png", transparent=True)

# Mostrar a nuvem de palavras no Streamlit
col_mario.subheader('Nuvem de Palavras Mário')
fig, ax = plt.subplots(figsize=(5, 2.5))
ax.imshow(wordcloud_mario, interpolation='bilinear')
ax.axis('off')

buf_mario = BytesIO()
fig.savefig(buf_mario, format="png", transparent=True)


col_yuri.image(buf_yuri)
col_mario.image(buf_mario)
# Caixa de seleção para filtrar mensagens por remetente
remetente = st.selectbox('Quem mandou a mensagem?', options=sorted(dados['Seu nome'].unique()))


# Mostrar o texto das mensagens de Mário e Yuri lado a lado
if remetente:
    mensagem_mario = dados_filtrados[dados_filtrados['Seu nome'] == remetente]['Mensagem para o MÁRIO '].values[0]
    mensagem_yuri = dados_filtrados[dados_filtrados['Seu nome'] == remetente]['Mensagem para o YURI'].values[0]

    col_mensagem_yuri, col_mensagem_mario = st.columns(2)
    
    with col_mensagem_mario:
        st.write(f'Mensagem de {remetente} para o Mário')
        st.write(mensagem_mario)

    with col_mensagem_yuri:
        st.write(f'Mensagem de {remetente} para o Yuri')
        st.write(mensagem_yuri)
