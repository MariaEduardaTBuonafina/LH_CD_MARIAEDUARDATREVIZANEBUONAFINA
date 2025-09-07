#!/usr/bin/env python
# coding: utf-8

# In[1]:


def split_genres(df):
    """
    Aqui eu criei uma função para transformar a coluna 'Genre' que vem como texto
    separado por vírgula em uma lista de gêneros. Isso ajuda a analisar os gêneros
    individualmente depois.
    """

    # Aqui eu usei o split para separar os gêneros em uma lista
    df['Genre_list'] = df['Genre'].str.split(', ')
    return df


# In[3]:


def extract_main_genre(df):
    """
    Como alguns filmes tem vários gêneros, eu criei essa função para pegar só o 
    primeiro gênero que foi listado e que geralmente é o principal. Isso facilita
    a fazer os gráficos e as análisis por gênero.
    """

    # Aqui eu pego o primeiro gênero da lista se ele existir
    df['Main_Genre'] = df['Genre_list'].apply(lambda x: x[0] if isinstance(x, list) else None)
    return df


# In[ ]:




