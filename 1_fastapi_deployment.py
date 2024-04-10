#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares
Data: 10/4/2024

Link de estudo:

1. https://github.com/arad1367/FastAPI_deployment_Grocery_app
"""

"""
Previsão de aplicativo de mercearia preferível na Hungria
=========================================================

Este aplicativo FastAPI foi projetado para prever o aplicativo de mercearia preferível na Hungria com base nas informações do usuário,
como idade, sexo, nível de escolaridade, anos de experiência com compras on-line e anos de experiência no uso de aplicativos de mercearia.

COMANDO PARA EXECUÇÃO:
uvicorn FastAPI:app --reload

ACESSO A DOCUMENTAÇÃO INTERATIVA DA API:
http://localhost:8000/docs
         OU
http://localhost:8000/redoc


API Endpoints
=============

* GET /: Retorna informações sobre o projeto, incluindo objetivo, versão e autor.

* GET /predict: Endpoint para prever o aplicativo de supermercado preferível com base nas entradas do usuário. 
Requer os seguintes parâmetros:

    * age: Idade do usuário.

    * gender: Gênero do usuário (1 para homem, 2 para mulher).

    * education: Nível de escolaridade do usuário (1 para licenciatura, 2 para associado, 3 para bacharelado, 4 para mestrado, 5 para doutorado).

    * exp_online: Anos de experiência com compras online.

    * exp_app: Anos de experiência no uso de aplicativos de supermercado.
"""