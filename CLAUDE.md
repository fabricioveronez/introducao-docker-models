# CLAUDE.md

Este arquivo fornece orientações para o Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Visão Geral do Projeto

Este é um projeto Python que demonstra análise de logs com IA para ambientes Kubernetes usando LangChain e modelos compatíveis com OpenAI. O projeto usa um modelo de IA local (gemma3) executando via Docker para análise de logs e interações gerais com IA.

## Comandos de Desenvolvimento

### Configuração do Ambiente
```bash
# Instalar dependências (executar da raiz do projeto)
pip install -r src/requirements.txt

# Usando DevContainer (recomendado)
# Abra o projeto no VSCode e selecione "Reopen in Container"
```

### Executando a Aplicação

#### Modo Local (Python diretamente)
```bash
# Interação básica com chat IA (linha de comando)
python src/index.py

# Análise de logs (analisa nginx.log por padrão)
python src/index_analise.py

# Interface web com Streamlit
streamlit run src/app.py
```

#### Modo Docker (Recomendado para produção)
```bash
# Executar toda a aplicação com Docker Compose
docker-compose up -d

# Executar apenas a aplicação web
docker-compose up app

# Executar análise de logs
docker-compose --profile analysis up log-analyzer

# Parar todos os serviços
docker-compose down

# Parar e remover volumes (cuidado: remove dados do modelo)
docker-compose down -v
```

### Gerenciamento do Modelo
```bash
# Modo Local
docker model pull ai/gemma3:latest

# Modo Docker (o modelo será baixado automaticamente)
# Primeira execução irá baixar o modelo ollama
docker-compose up model-runner
```

## Arquitetura

### Componentes Principais

- **src/index.py**: Ponto de entrada principal para interações gerais com IA usando LangChain (linha de comando)
- **src/app.py**: Interface web com Streamlit para chat interativo com IA
- **src/index_analise.py**: Script de análise de logs que processa arquivos de log e gera insights com IA
- **src/model/chat.py**: Configuração e inicialização centralizada do modelo de chat
- **src/logs/**: Arquivos de log de exemplo (nginx.log, controller-manager.log, etcd.log) para testes de análise

### Dependências Principais

- **LangChain**: Framework para desenvolvimento de aplicações LLM (`langchain`, `langchain-openai`, `langchain-community`)
- **Streamlit**: Framework para criação de interfaces web interativas
- **OpenAI**: Biblioteca cliente para interações com modelos de IA
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **httpx**: Cliente HTTP para chamadas da API do modelo

### Configuração do Modelo

O projeto está configurado para usar um modelo de IA local:
- **Modelo**: ai/gemma3:latest
- **Base URL**: http://model-runner.docker.internal/engines/v1 (Docker) ou http://localhost:12434 (local)
- **API Key**: Definida como "proj" (placeholder para modelo local)

### Configuração do DevContainer

O projeto usa DevContainer para ambientes de desenvolvimento consistentes:
- **Base**: Python 3.11 no Debian Bullseye
- **Extensões**: Docker, GitHub Actions, Python
- **Auto-instalação**: Dependências instaladas via postCreateCommand
- **Mapeamento de volume**: Raiz do projeto montada em /app no container

### Configuração Docker

Para produção, o projeto inclui configuração Docker completa:
- **Dockerfile**: Imagem otimizada com Python 3.11-slim
- **docker-compose.yml**: Orquestração completa incluindo:
  - **app**: Interface Streamlit na porta 8501
  - **model-runner**: Servidor Ollama para o modelo de IA na porta 11434
  - **log-analyzer**: Serviço opcional para análise batch de logs
- **Healthchecks**: Monitoramento da saúde dos serviços
- **Volumes persistentes**: Dados do modelo preservados entre reinicializações
- **Rede isolada**: Comunicação segura entre serviços

### Tratamento de Erros

Ambos os scripts principais incluem tratamento abrangente de erros para:
- Erros de conexão com o serviço do modelo de IA
- Exceções gerais com mensagens de erro descritivas
- Verificações de disponibilidade do serviço para localhost:11434

## Trabalhando com Logs

A funcionalidade de análise de logs espera arquivos de log no diretório `src/logs/`. O sistema usa o TextLoader do LangChain para processar arquivos de log e aplica prompts personalizados para análise. Os logs de exemplo incluem logs reais de ambientes Kubernetes/Docker para testes.

## Variáveis de Ambiente

Use arquivo `.env` para configuração:
```
OPENAI_API_KEY=sua-chave-aqui
```
Nota: Para desenvolvimento local, a chave da API está codificada como "proj" na configuração do modelo de chat.