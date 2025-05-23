from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "proj"

def get_chat_model():
            # Inicializa o modelo de chat com configurações personalizadas
        return ChatOpenAI(
            base_url="http://model-runner.docker.internal/engines/v1",
            #base_url="http://localhost:12434",
            model_name="ai/gemma3:latest",
            temperature=1
        )
