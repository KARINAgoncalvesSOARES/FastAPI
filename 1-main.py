"""
Data Scientist Jr.: Karina Gonçalves Soares

Objetivo:A seguir iremos executar um código simples usando o framework FastAPI 
         para a criação de uma API básica no Python.
versão:1.0.0
Data: 31/01/2024
Método de execução:


Antes de executar o código certifique-se de ter o FastAPI e o servidor ASGI instalados:
        $pip install fastapi uvicorn

ASGI significa "Asynchronous Server Gateway Interface" e é uma especificação para servidores web em Python que suportam comunicação assíncrona. 
O ASGI foi projetado para lidar melhor com operações assíncronas e casos de uso em tempo real, como WebSockets.

Em termos simples, o ASGI permite que os aplicativos web lidem com solicitações de maneira assíncrona, 
o que é particularmente útil para situações em que o servidor precisa lidar com um grande número de conexões simultâneas, 
como em aplicações de chat, streaming em tempo real ou notificações.

No contexto do exemplo anterior usando FastAPI, o servidor ASGI é necessário para executar o aplicativo de forma assíncrona.
O servidor ASGI mais comum usado com o FastAPI é o Uvicorn. 
Ao executar o comando uvicorn nome_do_arquivo:app --reload, você está usando o Uvicorn como o servidor ASGI para lidar com solicitações para o seu aplicativo FastAPI.

"""

from fastapi import FastAPI

"""
A instância do FastAPI, muitas vezes denominada app por convenção, 
é um objeto da classe FastAPI que representa a aplicação web criada com o framework FastAPI. 
Essa instância é essencial para definir rotas, manipular solicitações HTTP e configurar diversos aspectos do aplicativo.

"""

# Criar uma instância do FastAPI
app= FastAPI(title= 'Código simples usando FastAPI ☺️',
             version='1.0',
             description='A seguir iremos executar um código simples usando o framework FastAPI para a criação de uma API básica no Python')


# Definir uma rota padrão
@app.get("/")
def read_root():
    return {"mensagem": "HEllo, FastAPI"}

# Definir uma rota com parâmetros / usar a url http://127.0.0.1:8000/greet para rodar
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


"""
Em um framework web como o FastAPI, uma rota é uma associação entre uma URL específica e a função (ou método) Python 
que deve ser executada quando essa URL é acessada.
As rotas são fundamentais para definir como a aplicação web irá responder às diferentes solicitações HTTP recebidas.

No contexto do FastAPI, você pode criar rotas usando decoradores,
que são funções especiais que modificam o comportamento da função que segue o decorador.
O FastAPI fornece decoradores para os principais métodos HTTP, como @app.get, @app.post, @app.put, @app.delete, entre outros.
""" 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
Comando de execução:
                    $ uvicorn 1-main:app

OBSERVAÇÃO: COLOCAR /docs depois da URL
EXEMPLO: http://127.0.0.1:8000/docs
"""