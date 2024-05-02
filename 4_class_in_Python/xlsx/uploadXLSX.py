#!/usr/bin/env python3

"""

Data Scientist Jr.: Karina Gonçalves Soares


Carregar arquivo EXCEL
======================
Aqui criamos uma classe bem simples para carregar
um arquivo EXCEL e logo transformar em um DataFrame
usando a biblioteca do "pandas".
"""

import pandas as pd

# Carregando_arquivo_excel

class EXCELloader:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
    def read_excel_to_dataframe(self):
         # Carregando o arquivo EXCEL como DataFrame
         try:
             df = pd.read_excel(self.arquivo)
             return df
         
         except FileNotFoundError:
            print("Aquivo não encontrado.")
            return None
        

# Exemplo de uso:

if __name__ == "__main__":
    arquivo = "/home/karinag/karina_python/github/FastAPI/4_class_in_Python/xlsx/dataset.xlsx"
    loader = EXCELloader(arquivo=arquivo)
    
    # Carregando o arquivo CSV como DataFrame
    df = loader.read_excel_to_dataframe()
    
    # Exibindo o DataFrame
    if df is not None:
        print(df)