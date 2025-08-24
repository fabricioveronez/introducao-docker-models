# Chat com IA - Assistente Kubernetes

## Visão Geral

Este projeto é um chat interativo com IA especializado em Kubernetes e Docker. Ele permite:
- Interagir com um modelo de linguagem para perguntas sobre containers e orquestração
- Aprender conceitos de Kubernetes, Docker e tecnologias de containers
- Interface web amigável para conversação com modelo local de IA

O projeto é preparado para rodar em ambiente isolado via DevContainer (Docker), facilitando o setup e a portabilidade.

---

## Estrutura do Projeto

```
├── src/
│   ├── app.py                  # Interface Streamlit para chat com IA
│   ├── index.py                # Script CLI básico de interação
│   ├── model/
│   │   └── chat.py             # Configuração do modelo de IA
│   └── requirements.txt        # Dependências Python
├── docker-compose.yml          # Configuração dos serviços
├── Dockerfile                  # Imagem da aplicação
└── .vscode/                    # Configurações do VSCode
```

---

## Principais Dependências

- [langchain](https://python.langchain.com/): Orquestração de fluxos com LLMs
- [langchain-openai](https://python.langchain.com/docs/integrations/openai): Integração com modelos OpenAI e compatíveis
- [openai](https://pypi.org/project/openai/): Cliente para APIs de LLM
- [python-dotenv](https://pypi.org/project/python-dotenv/): Gerenciamento de variáveis de ambiente
- [httpx](https://www.python-httpx.org/): Cliente HTTP assíncrono

Veja todas as dependências em [`src/requirements.txt`](src/requirements.txt).

---

## Ambiente de Desenvolvimento

O projeto utiliza DevContainer para garantir um ambiente consistente. Você pode rodar localmente com Docker + VSCode ou manualmente.

### Pré-requisitos
- [Docker](https://www.docker.com/)
- [VSCode](https://code.visualstudio.com/) com a extensão [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (opcional, mas recomendado)

### Setup Rápido (com DevContainer)
1. Abra o projeto no VSCode.
2. Clique em "Reabrir em Container" quando solicitado.
3. O ambiente será configurado automaticamente e as dependências instaladas.

### Setup Manual
```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Uso

### 0. Baixar o Modelo de IA
Antes de executar as análises, é necessário baixar o modelo de IA:
```bash
docker model pull ai/gemma3:latest
```

### 1. Interface Web Streamlit (Recomendado)
Execute:
```bash
streamlit run src/app.py
```
Isso irá abrir uma interface web onde você pode conversar com a IA sobre Kubernetes e Docker.

### 2. Script CLI Básico
Execute:
```bash
python src/index.py
```
Isso enviará uma pergunta padrão ao modelo via linha de comando.

---

## Configuração de Variáveis de Ambiente

O projeto utiliza o arquivo `.env` para variáveis sensíveis, como a chave da API do modelo. Exemplo de `.env`:
```
OPENAI_API_KEY=sk-xxxxxx
```
> **Nota:** O valor padrão está "hardcoded" para desenvolvimento, mas recomenda-se usar o `.env` para produção.

---

## Observações
- O endpoint do modelo pode ser ajustado em `src/model/chat.py` (ex: `base_url`)
- O projeto utiliza Docker Models para execução local do modelo de IA
- Interface otimizada para aprendizado de conceitos de containers e orquestração
- Modelo roda localmente garantindo privacidade dos dados

---

## Licença

Este projeto é distribuído sob a licença MIT. 