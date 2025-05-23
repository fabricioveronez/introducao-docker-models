from dotenv import load_dotenv
import os
from langchain.schema import HumanMessage
import httpx
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from model.chat import get_chat_model

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

loader = TextLoader('./logs/nginx.log')
documents = loader.load()

def main():
    try:

        model = get_chat_model()

        prompt_base_conhecimento = PromptTemplate(
            input_variables=['logs', 'pergunta'],
            template='''
            Você é um assistente de IA que analisa logs de um sistema de monitoramento em ambiente Kubernetes.
            Analise os logs e responda a pergunta do usuário com base nas informações contidas neles.
            Os logs são os seguintes:
            {logs}
            Pergunta: {pergunta}
            '''
        )

        chain = prompt_base_conhecimento | model | StrOutputParser()

        # Gera a resposta
        response = chain.invoke(
            {
                'logs': '\n'.join(doc.page_content for doc in documents),
                #'pergunta': 'Quais são os principais erros encontrados nos logs?',
                'pergunta': 'Analisando os logs, como está a execução da aplicação?',
            }
        )

        print(response)
    
    except httpx.ConnectError as e:
        print(f"Erro de conexão: Não foi possível conectar ao servidor do modelo. Verifique se o serviço está rodando em localhost:11434")
        print(f"Detalhes do erro: {str(e)}")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

main()