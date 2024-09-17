import os
import json
import pandas as pd

df_documentos = pd.DataFrame()
directory = 'json_docs'

# Lista todos os arquivos no diretório
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        # Lê o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        df_temp = pd.DataFrame([data])
        df_documentos = pd.concat([df_documentos,df_temp])

df_documentos.columns

lista = df_documentos['Sistema'].to_list()
string_sistemas = ', '.join(f'"{item}"' for item in lista)

