"""
Data Scientist Jr.: Karina Gonçalves soares

setup:
======

$ pip install fastapi
$ pip install "uvicorn[standard]"

Execução:
=========

$ uvicorn main:app --reload


Interactive API docs:
=====================

http://127.0.0.1:8000/docs

Link de estudo:
===============

* https://github.com/EddyGiusepe/Learning_Class_in_Python/blob/main/simple_example_of_FastAPI/main.py
    
"""

from typing import Union, Optional
from fastapi import FastAPI
import uvicorn # servidor web ASGI 
import httpx # fornece api para requisições http

app = FastAPI()


async def buscar_dados_da_API_externa():
    # Simula uma requisição para uma API externa
    async with httpx.AsyncClient() as client:
        # Faça uma requisição GET para uma API fictícia
        response =await client.get("https://fakestoreapi.com/products")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        

@app.get("/")
# async def read_root():

async def read_root():
    # Lê dados de uma fonte externa:
    data = await buscar_dados_da_API_externa()
    if data:
        return {"message": "🤗 Dados lidos com sucesso 🤗", "data": data}
    else:
        return {"message": " 😭 Erro ao ler dados externos 😭 "}
    
    
@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}

# Requisição POST envia dados para o servidor
@app.post("/items/")
async def create_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)