import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def openaikey():
    load_env()
    openaikey = os.getenv("OPENAI_API_KEY")
    return openaikey

def serperkey():
    load_env()
    serperkey = os.getenv("SERPER_API_KEY")
    return serperkey

