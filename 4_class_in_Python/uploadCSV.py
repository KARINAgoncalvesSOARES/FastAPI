#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares


Link de estudo: https://github.com/EddyGiusepe/Learning_Class_in_Python/tree/main/1_ML_Real_Estate_Price_Prediction

Carregar arquivo CSV
====================
Aqui criamos uma classe bem simples para carregar
um arquivo CSV e logo transformar em um DataFrame
usando a biblioteca do "pandas".

"""

import pandas as pd

# Carregando_arquivo_csv
class CSVLoader:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
    def read_csv_to_dataframe(self):
        # Carregando o arquivo CSV como DataFrame
        try:
            df = pd.read_csv(self.arquivo)
            return df
        
        except FileNotFoundError:
            print("Aquivo não encontrado.")
            return None
        
# Exemplo de uso:
if __name__ == "__main__":
    arquivo = "/home/karinag/karina_python/github/FastAPI/4_class_in_Python/Real_Estate.csv"
    loader = CSVLoader(arquivo=arquivo)
    
    # Carregando o arquivo CSV como DataFrame
    df =  loader.read_csv_to_dataframe()
    
    # Exibindo o DataFrame
    if df is not None:
        print(df)
        
    