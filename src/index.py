from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import httpx
from model.chat import get_chat_model

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def main():
    try:

        model = get_chat_model()

        # Define a mensagem do usuário
        message = [
            HumanMessage(content="O que é Kubernetes."),
        ]

        # Gera a resposta
        response = model.invoke(message)
        print("Resposta do modelo:", response.content)
    
    except httpx.ConnectError as e:
        print(f"Erro de conexão: Não foi possível conectar ao servidor do modelo. Verifique se o serviço está rodando em localhost:11434")
        print(f"Detalhes do erro: {str(e)}")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

main()
