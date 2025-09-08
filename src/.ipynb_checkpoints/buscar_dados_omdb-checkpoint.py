#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Aqui eu começei importando algumas bibliotecas 
import requests  # para fazer requisições na API da OMDb
import pandas as pd # para ler e manipular os dados do CSV
import time # para colocar uma pausa entre as requisições
from urllib.parse import quote # para formatar os nomes dos filmes direito na URL


# Atenção: No código abaixo tem que eu colocar a sua chave
API_KEY = 'Sua_Chave'  

# Aqui é a função que busca os dados na API da OMDb
def buscar_dados_omdb(titulo, ano):
    # Aqui eu ajusto o título do filme pra funcionar na URL (espaços, etc)
    titulo_formatado = quote(titulo)

    # Aqui eu monto a URL pra consultar na API
    url = f'http://www.omdbapi.com/?t={titulo_formatado}&y={ano}&apikey={API_KEY}'

    try:
        resposta = requests.get(url)

        # Aqui eu tento transformar a resposta em JSON, mesmo que dê erro
        dados = resposta.json()

        # Verifico se foi erro de limite da API
        if dados.get('Error') == 'Request limit reached!':
            print('Ultrapassou o limite de requisições da API. O script vai parar.')
            exit()

        # Se o filme for encontrado
        if dados.get('Response') == 'True':
            return {
                'Director': dados.get('Director'),
                'Country': dados.get('Country'),
                'Awards': dados.get('Awards'),
                'Genre_OMDb': dados.get('Genre'),
                'Runtime_OMDb': dados.get('Runtime'),
                'Language': dados.get('Language'),
                'imdbVotes': dados.get('imdbVotes'),
                'Metascore': dados.get('Metascore')
            }
        else:
            # Aqui é quando a API respondeu mas não achou o filme
            print(f"Filme não encontrado: {titulo} ({ano}) - Erro: {dados.get('Error')}")

    except Exception as e:
        print(f"Erro ao acessar a API para: {titulo} ({ano}) - Detalhes: {e}")

    # Se nada deu certo, retorna None
    return None


# Essa é a função principal do meu script
def main():
    # Aqui eu leio o arquivo CSV original (pegando só os 10 primeiros pra testar)
    df = pd.read_csv('../data/desafio_indicium_imdb.csv')
    print(df.columns)

    # Aqui eu adiciono as colunas novas com os dados que eu vou buscar da API
    colunas_novas = ['Director', 'Country', 'Awards', 'Genre_OMDb', 'Runtime_OMDb', 'Language', 'Metascore', 'imdbVotes']
    for col in colunas_novas:
        df[col] = None

    # Aqui eu passo por cada filme do DataFrame
    for i, linha in df.iterrows():
        titulo = linha['Series_Title']  # Nome do filme
        ano = linha['Released_Year']    # Ano de lançamento

        print(f'Buscando dados para: {titulo} ({ano})')

        dados = buscar_dados_omdb(titulo, ano)
        if dados:
            for col in colunas_novas:
                df.at[i, col] = dados.get(col)
        else:
            print(f'Dados não encontrados para: {titulo} ({ano})')

        # Aqui eu coloco uma pausa entre cada requisição
        time.sleep(0.2)

    # Aqui eu salvo o novo CSV com os dados da API já incluídos
    df.to_csv('../data/desafio_indicium_imdb_enriquecido.csv', index=False)
    print('Arquivo com dados externos criado: desafio_indicium_imdb_enriquecido.csv')


# Aqui eu rodo a função principal quando eu executo esse script
if __name__ == '__main__':
    main()

