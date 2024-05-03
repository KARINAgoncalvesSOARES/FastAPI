#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares

Carregar arquivo JSON
=====================
Aqui criamos uma classe bem simples para apenas carregar
um arquivo JSON e logo transformar para um DataFrame usando
a biblioteca do "pandas".

"""
import pandas as pd

class UploadJSON:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
    def read_json_to_dataframe(self):
        """
        Carrega o arquivo JSON e retorna um DataFrame do Pandas.
        """
        try:
            df = pd.read_json(self.arquivo)
            return df
        except ValueError as ve:
            print(f"Erro ao ler o arquivo JSON: {ve}")
            return None
        except Exception as e:
            print(f"Erro desconhecido: {e}")
            return None

# Exemplo de uso:

if __name__ == "__main__":
    arquivo = "/home/karinag/karina_python/github/FastAPI/4_class_in_Python/json/pokemonDB_dataset.json"
    loader = UploadJSON(arquivo=arquivo)
    df = loader.read_json_to_dataframe()
    
    if df is not None: 
        print("DataFrame carregado com sucesso:")
        print(df.head())
    else:
        print("Erro ao carregar o arquivo JSON.")

                    