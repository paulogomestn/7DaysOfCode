import pandas as pd

# URL para o arquivo Parquet
url = 'https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet'

# Ler o arquivo Parquet
try:
    dados_exemplares = pd.read_parquet(url)
    print(dados_exemplares.head())
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
