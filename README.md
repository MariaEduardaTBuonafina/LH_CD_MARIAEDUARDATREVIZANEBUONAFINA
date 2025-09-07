# Desafio Indicium - Ciência de Dados

Este projeto é a solução do desafio de ciência de dados que foi proposto pela Indicium que é a análise dos dados cinematográficos do estúdio PProductions.

## Objetivo

É analisar um banco de dados de filmes para orientar a PProductions sobre qual tipo de filme desenvolver, considerando fatores que influenciam o faturamento e a avaliação desses filmes.

## Como executar o projeto

1. Clone o repositório:
   https://github.com/MariaEduardaTBuonafina/LH_CD_MARIAEDUARDATREVIZANEBUONAFINA.git
2. Entre na pasta do projeto:
   cd LH_CD_MARIAEDUARDATREVIZANEBUONAFINA
3. Instale as dependências:
   pip install -r requirements.txt
4. Abra o Jupyter Notebook
5. Navegue até a pasta notebooks e abra o arquivo principal.

## Estrutura do projeto

- `data`: Dados brutos do arquivo csv do desafio
- `notebooks/`: Notebooks com análise exploratória e modelagem que foi feita
- `src/`: Scripts Python com funções reutilizáveis
- `models/`: Modelo treinado salvo (.pkl)
- `reports/`: Relatório em HTML e PDF com as análises e conclusões

## Sobre os dados

O arquivo de dados contém informações sobre filmes, incluindo título, ano de lançamento, classificação etária, duração, gênero, nota do IMDB, sinopse, meta score, diretor, elenco principal, número de votos e faturamento.

# Enriquecimento de Dados com a API da OMDb

Este projeto utiliza dados externos da OMDb API (Open Movie Database)
 para enriquecer o dataset original com informações adicionais como: diretor, país de origem, premiações, duração, idiomas, entre outras.

# O que é necessário para rodar essa parte do projeto:

- Criar uma conta gratuita no site da OMDb:

Acesse: https://www.omdbapi.com/apikey.aspx

Preencha os dados solicitados

Escolha o plano Free (gratuito)

Após confirmar o e-mail, sua chave de API (API Key) será gerada

Adicionar a sua chave da OMDb ao script:

Vá até o arquivo enriquecimento_omdb.py (ou o nome correspondente que você estiver usando)

Substitua a variável API_KEY com a sua chave:

API_KEY = 'Sua_Chave'


- Executar o script de enriquecimento:

Certifique-se de que o arquivo original (desafio_indicium_imdb.csv) está localizado na pasta data/

Rode o script:

python src/buscar_dados_omdb.py

- Resultado:

O script irá buscar os dados na API e criar um novo arquivo na pasta data/ chamado:

desafio_indicium_imdb_enriquecido.csv

# Aviso sobre o arquivo desafio_indicium_imdb_enriquecido.csv

Este projeto inclui um arquivo chamado desafio_indicium_imdb_enriquecido.csv localizado na pasta /data. Ele já foi gerado utilizando a API da OMDb para enriquecer os dados originais com informações adicionais sobre os filmes, como:

- País de origem (Country)
- Premiações (Awards)
- Gênero segundo a OMDb (Genre_OMDb)
- Idioma (Language)
- Votos no IMDb (imdbVotes)
- Metascore, entre outros.

# Importante: 
O script src/buscar_dados_omdb.py ainda está disponível no projeto. Ele pode ser executado novamente a qualquer momento para gerar um novo arquivo enriquecido, especialmente se você quiser:

- Testar com uma nova chave da OMDb.
- Atualizar os dados.
- Rodar o projeto completo do 0
  
Para isso, você pode executar:
- python src/buscar_dados_omdb.py

Isso irá gerar novamente o arquivo data/desafio_indicium_imdb_enriquecido.csv.


Caso deseje rodar esse script, será necessário gerar uma chave da API OMDb, conforme explicado mais acima neste README.

# Observações importantes:

A versão gratuita da OMDb API permite até 1.000 requisições por dia.

Para evitar ultrapassar o limite, o script faz uma pequena pausa (0.2 segundos) entre cada requisição.

Caso o limite seja ultrapassado, o script será encerrado e você verá a mensagem:

Ultrapassou o limite de requisições da API. Vou parar o script.

## Contato

Maria Eduarda Trevizane Buonafina - meduardatb7@gmail.com