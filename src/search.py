import os

from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableLambda

from functions import check_variables, get_store
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    check_variables()

    print("PERGUNTA:" + question)

    if not question:
        raise RuntimeError(f"Missing required environment variable: {question}")

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))

    store = get_store(embeddings)

    results = store.similarity_search_with_score(question, k=3)

    prompt = PromptTemplate(
        input_variables = ["contexto", "pergunta"],
        template = PROMPT_TEMPLATE
    )

    return RunnableParallel(
        contexto=RunnableLambda(lambda _: results),
        pergunta=RunnableLambda(lambda _: question)
    ) | prompt