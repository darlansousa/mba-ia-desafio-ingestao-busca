from langchain_openai import ChatOpenAI

from search import search_prompt
from langchain_core.output_parsers import StrOutputParser

def main():
    question = input("Faça sua pergunta: ")
    search = search_prompt(question)

    if not search:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    model = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)

    pipeline = search | model | StrOutputParser()

    result = pipeline.invoke({})

    print("RESPOSTA:" + result)


if __name__ == "__main__":
    main()