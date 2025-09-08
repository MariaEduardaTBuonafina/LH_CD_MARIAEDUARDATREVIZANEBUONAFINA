# Desafio Indicium - Ciência de Dados

Este projeto é a minha solução para o desafio de Ciência de Dados proposto pela Indicium, com foco na análise de dados de filmes do estúdio fictício PProductions.

- Objetivo

O principal objetivo foi analisar um conjunto de dados sobre filmes, entender os padrões que influenciam a avaliação do público e o faturamento, e com isso ajudar a PProductions a decidir quais tipos de filmes podem ter melhor desempenho.

- Como executar o projeto

Clone o repositório:

git clone https://github.com/MariaEduardaTBuonafina/LH_CD_MARIAEDUARDATREVIZANEBUONAFINA.git


Entre na pasta do projeto:

cd LH_CD_MARIAEDUARDATREVIZANEBUONAFINA


Instale as dependências:

pip install -r requirements.txt


Abra o Jupyter Notebook:

jupyter notebook


Vá até a pasta notebooks/ e abra os arquivos de análise exploratória e modelagem.

- Estrutura do projeto

data/: Arquivos CSV com os dados originais e enriquecidos

notebooks/: Notebooks com a análise e a modelagem

src/: Scripts Python com funções reutilizáveis (data processing, modelagem etc)

models/: Modelo de predição salvo (.pkl)

reports/: Relatório final em HTML com conclusões do projeto

- Sobre os dados

O conjunto de dados inclui:

Nome do filme, ano de lançamento e classificação etária

Duração (em minutos), gênero e sinopse

Avaliação no IMDB e no Metascore

Elenco principal e diretor

Número de votos e faturamento

- Enriquecimento com a OMDb API

O projeto também inclui uma etapa de enriquecimento de dados externos, usando a OMDb API
 para buscar informações adicionais sobre cada filme:

Diretor

País de origem

Premiações recebidas

Idiomas

Gênero (pela OMDb)

Metascore

Número de votos (imdbVotes)

Duração oficial (Runtime_OMDb)

- O que você precisa para rodar essa parte:

Criar uma conta gratuita na OMDb:

Acesse: https://www.omdbapi.com/apikey.aspx

Escolha o plano gratuito e gere sua chave de API

Adicione sua chave no script src/buscar_dados_omdb.py:

API_KEY = 'Sua_Chave'


Rode o script:

python src/buscar_dados_omdb.py


Resultado:

Um novo arquivo CSV será criado na pasta data/ com o nome:

desafio_indicium_imdb_enriquecido.csv

- Sobre o arquivo enriquecido

O arquivo desafio_indicium_imdb_enriquecido.csv já está incluído na pasta /data para facilitar a execução do projeto.

Mas, se preferir, você pode executar o script src/buscar_dados_omdb.py novamente para:

Atualizar os dados

Testar com outra chave da API

Rodar o projeto do zero

- Observações importantes

A versão gratuita da OMDb API permite até 1.000 requisições por dia.

Para evitar bloqueios, o script faz uma pausa de 0.2 segundos entre cada requisição.

Caso o limite diário seja atingido, o script irá parar com a mensagem:

Ultrapassou o limite de requisições da API. Vou parar o script.

## Contato

Maria Eduarda Trevizane Buonafina - meduardatb7@gmail.com