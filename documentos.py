import streamlit as st
import os
import json
import pandas as pd

df_documentos = pd.DataFrame()
directory = 'json_docs'
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        df_temp = pd.DataFrame([data])
        df_documentos = pd.concat([df_documentos,df_temp])

def doc():
    # Cria o dataframe de documentação
    df_documentos = pd.DataFrame()
    directory = 'json_docs'
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            df_temp = pd.DataFrame([data])
            df_documentos = pd.concat([df_documentos,df_temp])

    sistemas = df_documentos['Sistema'].unique()
    option_sistema = st.selectbox(
        "Selecione o sistema que deseja visualizar a documentação resumida",
        (sistemas),
    )

    df_sistema = df_documentos[df_documentos['Sistema'] == option_sistema]

    doc_sistema = df_sistema['Sistema'].iloc[0]
    doc_alias = df_sistema['Alias'].iloc[0]
    doc_descricao = df_sistema['Descrição'].iloc[0]
    doc_desenvolvedor = df_sistema['Desenvolvedor'].iloc[0]
    doc_dt_prod = df_sistema['Data de produtização'].iloc[0]
    doc_algoritmo = df_sistema['Algoritmo'].iloc[0]


    st.title(doc_sistema)
    st.write('Alias: '+doc_alias)
    st.divider()
    
    st.markdown(f'''
                #### :blue[Descrição]
                ##### {doc_descricao}
    ''')
    st.markdown(f'''
                #### :blue[Desenvolvedor]
                ##### {doc_desenvolvedor}
    ''')
    st.markdown(f'''
                #### :blue[Data de produtização]
                ##### {doc_dt_prod}
    ''')
    st.markdown(f'''
                #### :blue[Algoritmo]
                ##### {doc_algoritmo}
    ''')

   
