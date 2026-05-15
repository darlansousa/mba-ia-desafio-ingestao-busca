import os
from functions import check_variables, get_store
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector
import psycopg

load_dotenv()

def ingest_pdf():
    check_variables()

    pdf_path = os.getenv("PDF_PATH")

    docs = PyPDFLoader(str(pdf_path)).load()

    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=False
    ).split_documents(docs)

    if not splits:
        raise SystemExit("No documents to process after splitting.")

    enriched_docs = [
        Document(
            page_content=doc.page_content,
            metadata={"key": v for k, v in doc.metadata.items() if v not in ("", None)}
        )
        for doc in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched_docs))]

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    store = get_store(embeddings)

    store.add_documents(enriched_docs, ids=ids)


if __name__ == "__main__":
    ingest_pdf()