# CLAUDE.md

Este arquivo fornece orientações ao Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Comandos Principais

### Desenvolvimento
```bash
# Instalar dependências Python
pip install -r src/requirements.txt

# Executar aplicação Streamlit
streamlit run src/app.py --server.address 0.0.0.0 --server.port 8501

# Executar script CLI básico
python src/index.py
```

### Docker e Docker Models
```bash
# Baixar modelo de IA necessário
docker model pull ai/gemma3:latest

# Executar com Docker Compose
docker-compose up --build

# Build da imagem Docker
docker build -t analise-logs-ia .
```

## Arquitetura do Projeto

### Estrutura Principal
- **src/app.py**: Interface Streamlit para chat interativo com IA
- **src/index.py**: Script CLI para interações básicas com o modelo
- **src/model/chat.py**: Configuração do modelo ChatOpenAI usando LangChain
- **docker-compose.yml**: Configuração com serviços da aplicação e modelo IA
- **Dockerfile**: Imagem Python 3.11 com Streamlit e dependências

### Integração com Modelos de IA
O projeto utiliza **Docker Models** com o modelo `ai/gemma3:latest` executando localmente. A configuração do modelo está centralizada em `src/model/chat.py` e usa:
- Endpoint: `http://model-runner.docker.internal/engines/v1` (via Docker Compose)
- API compatível com OpenAI via LangChain
- Token hardcoded como "proj" para desenvolvimento

### Dependências Principais
- **Streamlit**: Interface web para chat interativo
- **LangChain + langchain-openai**: Orquestração e integração com modelos de IA
- **httpx**: Cliente HTTP para conexões com o modelo
- **python-dotenv**: Gerenciamento de variáveis de ambiente

### Fluxo de Funcionamento
1. Docker Compose levanta o modelo de IA local e a aplicação Streamlit
2. Interface Streamlit (`app.py`) permite chat educativo sobre Kubernetes/Docker
3. Modelo configurado via `chat.py` processa perguntas usando LangChain
4. Respostas são exibidas na interface web com histórico de conversas

## Observações Importantes
- O projeto é um assistente educativo para aprendizado de Kubernetes e Docker
- Utiliza modelo local para privacidade e controle total dos dados
- Interface otimizada para perguntas sobre conceitos de containers e orquestração
- Configuração de segurança com usuário não-root no container