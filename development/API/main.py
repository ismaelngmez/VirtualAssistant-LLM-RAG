import time
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from model import Chatbot

app = FastAPI()
chatbot_instance = Chatbot()


@app.get("/", response_class=PlainTextResponse)
def read_root():
    # Confidential
    return 'Confidential'


@app.get("/set_main_model/", response_class=PlainTextResponse)
def set_main_model(model: str = '', temperature: int = 0.7, max_new_tokens: int = 200):
    # Confidential
    return 'Confidential'


@app.get("/set_embeddings_model/", response_class=PlainTextResponse)
def set_embeddings_model(model: str = '', embeddings_device: str = 'gpu'):
    # Confidential
    return 'Confidential'


@app.get("/set_vector_db/", response_class=PlainTextResponse)
def set_vector_db(k: int = 1, chunk_size=1024, chunk_overlap=128):
    # Confidential
    return 'Confidential'


@app.get("/construct_chain/", response_class=PlainTextResponse)
def construct_chain():
    # Confidential
    return 'Confidential'


@app.get("/query_model/", response_class=PlainTextResponse)
def query_llm(question: str = ''):
    # Confidential
    return 'Confidential'
