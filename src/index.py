from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import httpx
from model.chat import get_chat_model

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def enviar_pergunta_cli(pergunta):
    """
    Envia uma pergunta para o modelo de IA via linha de comando.
    
    Args:
        pergunta (str): A pergunta a ser enviada para o modelo
        
    Returns:
        str: A resposta do modelo ou mensagem de erro
    """
    try:
        model = get_chat_model()
        message = [HumanMessage(content=pergunta)]
        response = model.invoke(message)
        return response.content
    
    except httpx.ConnectError as e:
        return f"Erro de conexão: Não foi possível conectar ao servidor do modelo. Verifique se o serviço está rodando em localhost:11434\nDetalhes do erro: {str(e)}"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def main():
    """
    Função principal que executa uma pergunta padrão sobre Kubernetes.
    """
    pergunta = "O que é Kubernetes."
    resposta = enviar_pergunta_cli(pergunta)
    print("Resposta do modelo:", resposta)

if __name__ == "__main__":
    main()
