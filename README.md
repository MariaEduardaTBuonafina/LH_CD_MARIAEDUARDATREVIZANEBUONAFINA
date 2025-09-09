# Desafio Indicium - Ciência de Dados

Este projeto é a minha solução para o desafio de Ciência de Dados proposto pela Indicium, com foco na análise de dados cinematográficos de um estúdio fictício chamado PProductions.

---

## Objetivo

O principal objetivo foi analisar um conjunto de dados sobre filmes, identificar padrões que influenciam o faturamento e a avaliação do público, e fornecer recomendações para ajudar a PProductions a tomar decisões mais estratégicas sobre quais tipos de filmes produzir.

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/MariaEduardaTBuonafina/LH_CD_MARIAEDUARDATREVIZANEBUONAFINA.git
cd LH_CD_MARIAEDUARDATREVIZANEBUONAFINA
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```bash
pip install -r requirements.txt
```

### 3. Rode o Jupyter Notebook

```bash
jupyter notebook
```

Ele abrirá automaticamente uma página no navegador com um endereço parecido com:

```bash
http://localhost:8888/?token=algumacodigosecreto
```

Esse token é um código de segurança gerado automaticamente para proteger o acesso ao Jupyter.

### Como acessar

No terminal ou PowerShell onde você executou o comando, será exibido um link completo contendo o token.  
Copie esse link inteiro e cole na barra de endereços do seu navegador para acessar a interface do Jupyter.

O endereço localhost significa que o Jupyter está rodando localmente na sua máquina.


Depois, navegue até a pasta `notebooks/` e abra os arquivos de análise exploratória, modelagem e recomendações.

---

## Estrutura do Projeto

```plaintext
├── data/           # Arquivos CSV com os dados originais e enriquecidos
├── models/         # Modelo treinado (.pkl)
├── notebooks/      # Notebooks com análise, modelagem e insights finais e um relatório final completo
├── reports/        # Relatório EDA em HTML
├── src/            # Scripts Python com funções reutilizáveis
├── requirements.txt
└── README.md
```

---

## Sobre os dados

O conjunto de dados inclui diversas variáveis sobre filmes:

- Título do filme
- Ano de lançamento
- Classificação etária (certificate)
- Duração (runtime)
- Gênero
- Sinopse (overview)
- Avaliação do IMDB
- Meta Score
- Elenco principal (Star1, Star2, etc.)
- Diretor
- Número de votos
- Faturamento (gross)

---

## Enriquecimento com a OMDb API

O projeto utiliza a OMDb API para enriquecer o conjunto de dados com informações adicionais como:

- País de origem (Country)
- Premiações recebidas (Awards)
- Gênero fornecido pela OMDb (Genre_OMDb)
- Idiomas (Language)
- Duração oficial (Runtime_OMDb)
- Diretor e elenco (confirmação)
- Meta score atualizado
- Número de votos no IMDB (imdbVotes)

---

## Como utilizar a OMDb API

1. Crie uma conta gratuita em:  
   https://www.omdbapi.com/apikey.aspx

2. Gere sua chave de API no plano gratuito.

3. No arquivo `src/buscar_dados_omdb.py`, insira sua chave:

```python
API_KEY = 'Sua_Chave'
```

4. Execute o script para enriquecer os dados:

```bash
python src/buscar_dados_omdb.py
```

Um novo arquivo será criado automaticamente:

```
data/desafio_indicium_imdb_enriquecido.csv
```

> **Observação**: esse arquivo já está incluído no repositório, mas você pode gerar novamente se quiser atualizar os dados ou testar com outra chave da API.

---

## Limites da API

- A versão gratuita da OMDb permite até 1.000 requisições por dia.
- Para evitar bloqueios, o script inclui uma pausa de `0.2 segundos` entre cada requisição.
- Caso o limite seja atingido, a seguinte mensagem será exibida:

```
Ultrapassou o limite de requisições da API. Vou parar o script.
```


---

## Contato

**Maria Eduarda Trevizane Buonafina**  
E-mail: [meduardatb7@gmail.com](mailto:meduardatb7@gmail.com)  
GitHub: [MariaEduardaTBuonafina](https://github.com/MariaEduardaTBuonafina)
