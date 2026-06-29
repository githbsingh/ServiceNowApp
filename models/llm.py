import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()


def get_llm():

    if PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
        )

    elif PROVIDER == "openai":
        return ChatOpenAI(
            model="gpt-4.1-mini",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
        )

    elif PROVIDER == "ollama":
        return ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    raise ValueError(f"Unsupported LLM_PROVIDER: {PROVIDER}")


llm = get_llm()