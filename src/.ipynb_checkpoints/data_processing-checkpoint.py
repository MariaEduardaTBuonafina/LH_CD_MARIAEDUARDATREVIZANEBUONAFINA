#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Primeiro aqui eu vou importar duas bibliotecas que vou usar nessa parte
import pandas as pd
import numpy as np


# In[2]:


def load_and_clean_data(filepath):
    """
    Essa função é para carregar o arquivo CSV e dentro dela eu fiz uma limpeza básica nos dados.
    Eu fiz assim porque o arquivo ele tem algumas colunas com texto que precisam virar números,
    e tem valores faltando que podem atrapalhar a análise se não tratar.
    """
    # Aqui eu carreguei o arquivo CSV com pandas
    df = pd.read_csv(filepath)

    
    # A coluna 'Runtime' veio com texto tipo '120 min', então eu tirei o ' min' para ficar só o número
    # E depois eu converti para número inteiro, porque assim dá pra usar em análise e modelo
    df['Runtime'] = df['Runtime'].str.replace(' min', '')
    df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')  
    # Esse 'coerce' ele transforma erros em NaN
    
    
    # A coluna 'Gross' ela tem valores com vírgula, tipo '1,234,567', então eu tirei as vírgulas
    # E depois eu converti para número, e os valores que não deram certo viraram NaN
    df['Gross'] = df['Gross'].astype(str).str.replace(',', '', regex=False)
    df['Gross'].replace('nan', np.nan, inplace=True)
    df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
    
    
    # Aqeui eu preenchi os valores faltantes em 'Meta_score' e 'Gross' com a mediana,
    # porque a mediana ela é menos afetada por valores que são muito altos ou baixos
    df['Meta_score'].fillna(df['Meta_score'].median(), inplace=True)
    df['Gross'].fillna(df['Gross'].median(), inplace=True)
   
    
    # Na coluna 'Certificate' (que é a classificação etária), eu preenchi os valores faltantes com 'Não foi informado'
    # porque ela é uma informação categórica e não podemos deixar vazia
    df['Certificate'].fillna('Não foi informado', inplace=True)

    
    # Aqui eu removi as linhas que ficaram com 'Runtime' vazio, porque não dá pra usar sem essa informação
    df = df.dropna(subset=['Runtime'])
    
    
    # E aqui por último eu retornei o dataframe limpo para usar depois
    return df

