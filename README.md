# Desafio MBA — Engenharia de Software com IA · Full Cycle

> Pipeline de ingestão e chat com Retrieval-Augmented Generation (RAG) desenvolvido como parte do MBA de Engenharia de Software com IA da Full Cycle.

---

## Pré-requisitos

- Python 3.10+
- Docker e Docker Compose

---

## Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/darlansousa/mba-ia-desafio-ingestao-busca
cd mba-ia-desafio-ingestao-busca
```

2. **Instale as dependências Python**

```bash
pip install -r requirements.txt
```

3. **Suba o banco de dados**

```bash
docker-compose up -d
```

---

## Uso

### 1. Ingestão de dados

Processa e indexa os documentos na base vetorial:

```bash
python3 src/ingest.py
```

### 2. Chat

Inicia a interface de chat com RAG:

```bash
python3 src/chat.py
```

> **Atenção:** execute a ingestão ao menos uma vez antes de iniciar o chat.

---

## Estrutura do projeto

```
.
├── src/
│   ├── ingest.py       # Pipeline de ingestão e indexação
│   └── chat.py         # Interface de chat com RAG
├── docker-compose.yml  # Configuração do banco de dados
└── requirements.txt    # Dependências Python
```