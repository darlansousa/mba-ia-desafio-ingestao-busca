import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector


def check_variables():
    load_dotenv()
    for k in ("OPENAI_API_KEY", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME"):
        if not os.getenv(k):
            raise RuntimeError(f"Missing required environment variable: {k}")


def get_store(embeddings: OpenAIEmbeddings):
    return PGVector(
        collection_name = os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection = os.getenv("DATABASE_URL"),
        embeddings = embeddings,
        use_jsonb = True
    )