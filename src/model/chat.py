from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "proj"

def get_chat_model():
    # Inicializa o modelo de chat com configurações personalizadas
    # Verifica se está rodando em container Docker
    import socket
    
    try:
        # Tenta resolver o hostname do container
        socket.gethostbyname('model-runner')
        base_url = "http://model-runner.docker.internal/engines/v1"
    except socket.gaierror:
        # Se não conseguir resolver, usa localhost (desenvolvimento local)
        base_url = "http://localhost:11434/v1"
    
    return ChatOpenAI(
        base_url=base_url,
        model_name="ai/gemma3:latest",  # Modelo mais leve para testes
        temperature=0.7,
        timeout=30
    )
