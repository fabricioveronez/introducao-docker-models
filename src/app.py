import streamlit as st
from dotenv import load_dotenv
import os
from langchain.schema import HumanMessage
import httpx
from model.chat import get_chat_model

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def enviar_pergunta(pergunta):
    """
    Envia uma pergunta para o modelo de IA e retorna a resposta.
    """
    try:
        model = get_chat_model()
        message = [HumanMessage(content=pergunta)]
        response = model.invoke(message)
        return response.content, None
    
    except httpx.ConnectError as e:
        error_msg = "Erro de conexão: Não foi possível conectar ao servidor do modelo. Verifique se o serviço está rodando em localhost:11434"
        return None, error_msg
    except Exception as e:
        error_msg = f"Erro inesperado: {str(e)}"
        return None, error_msg

# Configuração da página
st.set_page_config(
    page_title="Chat com IA - Assistente Kubernetes",
    page_icon="🤖",
    layout="wide"
)

# Título da aplicação
st.title("🤖 Chat com IA - Assistente Kubernetes")
st.markdown("Faça perguntas sobre Kubernetes, Docker e conceitos de containers!")

# Inicializar histórico de conversas na sessão
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Informações")
    st.markdown("""
    **Modelo:** ai/gemma3:latest
    
    **Funcionalidades:**
    - Chat interativo com IA
    - Especializado em Kubernetes e Docker
    - Conceitos de orquestração de containers
    
    **Como usar:**
    1. Digite sua pergunta
    2. Clique em "Enviar"
    3. Veja a resposta da IA
    """)
    
    if st.button("🗑️ Limpar Histórico"):
        st.session_state.mensagens = []
        st.rerun()

# Área principal do chat
st.header("💬 Conversa")

# Exibir histórico de mensagens
for i, msg in enumerate(st.session_state.mensagens):
    if msg["tipo"] == "usuario":
        with st.chat_message("user"):
            st.write(msg["conteudo"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["conteudo"])

# Formulário para nova pergunta
with st.form("pergunta_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        pergunta = st.text_input(
            "Digite sua pergunta:",
            placeholder="Ex: O que é Kubernetes?",
            label_visibility="collapsed"
        )
    
    with col2:
        enviar = st.form_submit_button("📤 Enviar", use_container_width=True)

# Processar pergunta quando enviada
if enviar and pergunta.strip():
    # Adicionar pergunta do usuário ao histórico
    st.session_state.mensagens.append({
        "tipo": "usuario",
        "conteudo": pergunta
    })
    
    # Exibir pergunta do usuário
    with st.chat_message("user"):
        st.write(pergunta)
    
    # Exibir indicador de loading e buscar resposta
    with st.chat_message("assistant"):
        with st.spinner("Processando sua pergunta..."):
            resposta, erro = enviar_pergunta(pergunta)
        
        if erro:
            st.error(f"❌ {erro}")
            st.session_state.mensagens.append({
                "tipo": "assistente",
                "conteudo": f"❌ {erro}"
            })
        else:
            st.write(resposta)
            st.session_state.mensagens.append({
                "tipo": "assistente",
                "conteudo": resposta
            })

# Se não há mensagens, mostrar sugestões
if not st.session_state.mensagens:
    st.markdown("### 💡 Sugestões de perguntas:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔧 O que é Kubernetes?"):
            st.session_state.pergunta_sugerida = "O que é Kubernetes?"
            st.rerun()
        
        if st.button("📦 O que são containers?"):
            st.session_state.pergunta_sugerida = "O que são containers e como funcionam?"
            st.rerun()
    
    with col2:
        if st.button("🐳 Diferença entre Docker e Kubernetes?"):
            st.session_state.pergunta_sugerida = "Qual a diferença entre Docker e Kubernetes?"
            st.rerun()
        
        if st.button("⚙️ Como funciona um cluster?"):
            st.session_state.pergunta_sugerida = "Como funciona um cluster Kubernetes?"
            st.rerun()

# Processar pergunta sugerida se foi clicada
if "pergunta_sugerida" in st.session_state:
    pergunta_sugerida = st.session_state.pergunta_sugerida
    del st.session_state.pergunta_sugerida
    
    # Adicionar pergunta ao histórico
    st.session_state.mensagens.append({
        "tipo": "usuario",
        "conteudo": pergunta_sugerida
    })
    
    # Buscar resposta
    resposta, erro = enviar_pergunta(pergunta_sugerida)
    
    if erro:
        st.session_state.mensagens.append({
            "tipo": "assistente",
            "conteudo": f"❌ {erro}"
        })
    else:
        st.session_state.mensagens.append({
            "tipo": "assistente",
            "conteudo": resposta
        })
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("**Desenvolvido com Streamlit + LangChain + Modelo Local de IA**")