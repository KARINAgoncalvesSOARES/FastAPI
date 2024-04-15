#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares
Data: 10/4/2024

Link de estudo:

1. https://github.com/arad1367/FastAPI_deployment_Grocery_app
"""

"""
Previsão de aplicativo de mercearia preferível na Hungria 🛒 🇭🇺
============================================================

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
# Previsão simples do aplicativo de supermercado na Hungria (usando FastAPI)

class_App_names = ['FoodPanda', 'Wolt', 'Spar', 'Tesco online', 'myLidl']

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle # Serialização e desserialização
import os

filePath = os.path.join(os.getcwd(), '2_fastapi/data_mercado.csv')

# 1. Abrindo os dados para leitura
data = pd.read_csv(filePath)

# 2. Checando os dados
#print (data.head(7))

#3. Separando os dados em Features & Target
x = data.drop("Apps", axis=1)
y = data["Apps"]

# 4. Separando os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 5. Criando o modelo
clf = RandomForestClassifier()

# 6. Treinando o modelo
clf.fit(x_train, y_train)

# 7. Fanzendo a previsão
y_preds = clf.predict(x_test)

# 8. Calculando a acurácia
acc = accuracy_score(y_test, y_preds)
print(f"A acurácia do modelo é: {round((acc*100),2)}%")

# 9. Salvando o modelo
#filename = "clf_silple.pkl"
#pickle.dump(clf, open(filename, 'wb'))

# 10. carregue o modelo e faça uma previsão
# # no aplicativo fastapi.py

