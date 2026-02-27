import streamlit as st
from google import genai
import os

st.set_page_config(page_title="IA", page_icon="🤖")
st.title("IA xupetetinha")

# Configuracao da API
CHAVE_API = "AIzaSyD9WOlNxRsZxNxJq3qQDRTGjYJFVhwFa1c"

# Inicializa o cliente e o chat na sessao (session_state)
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=CHAVE_API)
    
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model="gemini-2.5-flash")

if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibe as mensagens do historico na tela
for mensagem in st.session_state.historico:
    role = mensagem["role"]
    content = mensagem["content"]
    with st.chat_message(role):
        st.markdown(content)

# Campo de entrada de texto na parte inferior do chat
entrada = st.chat_input("Digite sua mensagem...")

if entrada:
    # 1. Guarda a mensagem do usuario no historico e mostra na tela
    st.session_state.historico.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.markdown(entrada)

    # 2. Envia a mensagem para o modelo Gemini e pega a resposta
    resposta = st.session_state.chat.send_message(entrada)
    texto_resposta = resposta.text

    # 3. Guarda a resposta da IA no historico e mostra na tela
    st.session_state.historico.append({"role": "model", "content": texto_resposta})
    with st.chat_message("model"):
        st.markdown(texto_resposta)
