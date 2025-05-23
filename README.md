# Análise de Logs com IA para Ambientes Kubernetes

## Visão Geral

Este projeto utiliza modelos de linguagem natural (LLMs) para analisar logs de sistemas, especialmente em ambientes Kubernetes. Ele permite:
- Interagir com um modelo de linguagem para perguntas gerais.
- Analisar arquivos de log e obter respostas inteligentes sobre erros e eventos.

O projeto é preparado para rodar em ambiente isolado via DevContainer (Docker), facilitando o setup e a portabilidade.

---

## Estrutura do Projeto

```
├── src/
│   ├── index.py                # Script principal de interação com LLM
│   ├── index_analise.py        # Script de análise de logs com LLM
│   ├── requirements.txt        # Dependências Python
│   └── logs/                   # Exemplos de logs (nginx, controller-manager, etcd)
├── .devcontainer/              # Configuração de ambiente Docker/VSCode
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   └── Dockerfile
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

### 1. Interação com o Modelo de Linguagem
Execute:
```bash
python src/index.py
```
Isso enviará uma pergunta ao modelo e exibirá a resposta.

### 2. Análise de Logs
Execute:
```bash
python src/index_analise.py
```
O script irá ler o arquivo `src/logs/nginx.log`, enviar o conteúdo para o modelo e retornar uma análise dos principais erros encontrados.

#### Exemplo de log analisado:
```
2025-05-23T13:12:31.20476876Z stderr F 2025/05/23 13:12:31 [error] 33#33: *1 open() "/usr/share/nginx/html/teste" failed (2: No such file or directory), client: 127.0.0.1, server: localhost, request: "GET /teste HTTP/1.1", host: "localhost:8080"
```

Você pode substituir o arquivo de log por outros exemplos em `src/logs/`.

---

## Configuração de Variáveis de Ambiente

O projeto utiliza o arquivo `.env` para variáveis sensíveis, como a chave da API do modelo. Exemplo de `.env`:
```
OPENAI_API_KEY=sk-xxxxxx
```
> **Nota:** O valor padrão está "hardcoded" para desenvolvimento, mas recomenda-se usar o `.env` para produção.

---

## Observações
- O endpoint do modelo pode ser ajustado em `index.py` e `index_analise.py` (ex: `base_url`).
- O projeto é facilmente extensível para outros tipos de logs ou perguntas.
- Os logs de exemplo são reais de ambientes Docker/Kubernetes.

---

## Licença

Este projeto é distribuído sob a licença MIT. 