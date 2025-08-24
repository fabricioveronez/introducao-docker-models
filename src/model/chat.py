from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "proj"
OPENAI_API_URL = os.environ["OPENAI_API_URL"]

def get_chat_model():
        
    return ChatOpenAI(
        base_url=OPENAI_API_URL,
        model_name="ai/gemma3:latest",  # Modelo mais leve para testes
        temperature=0.7
    )
