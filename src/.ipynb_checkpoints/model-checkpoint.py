#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle # Esse import ele é usado para salvar e carregar objetos python (como modelos treinados) em arquivos .pkl (como foi peço no desafio) 
from sklearn.linear_model import LinearRegression # Aqui ele importa o modelo de regressão linear da biblioteca scikit-learn
from sklearn.model_selection import train_test_split # Essa é uma função que vai dividir os dados em conjuntos de treino e teste
from sklearn.metrics import mean_squared_error, r2_score # O mean_squared_error vai calcular o erro médio ao quadrado entre o valor previsto e o valor real, e quanto menor melhor.
# O r2_score ele vai retornar um valor entre 0 e 1 que mostra o quão bem o modelo explica os dados, e quanto mais próximo de 1 melhor.


# In[2]:


def train_model(df, features, target):
    """
    Essa função ela serve para treinar um modelo de regressão linear simples.
    Eu usei a regressão linear porque é mais fácil de entender e ela serve para
    prever números, que no caso é o que a gente quer que é a nota do IMDB.
    """

    # Aqui eu separei as variáveis independentes (que são as features) e a variávei que eu quero prever (que é o target)
    x = df[features]
    y = df[target]

    # Aqui agora eu dividi os dados em treino e teste para avaliar o modelo depois
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Aqui eu criei o modelo de regressão linear e treinei com os dados de treino
    model = LinearRegression()
    model.fir(X_train, y_train)

    # Agora aqui eu fiz a previsão com os dados de teste para ver como o modelo se saiu
    y_pred = model.predict(X_test)

    # Aqi eu calculei o erro médio quadrático raiz (o RMSE) para medir o erro das previsões
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Agora aqui eu calculei o R2 para ver quanto da variação da nota o modelo explica (como eu disse la em cima quanto mais perto de 1 melhor)
    r2 = r2_score(y_test, y_pred)

    # Aqui por fim dessa função eu retornei o modelo treinado e as métricas para analisar depois
    return model, rmse, r2


# In[3]:


def save_model(model, filepath):
    """
    Usei essa função para salvar o modelo treinado em um arquivo .pkl (que é um
    dos critérios do desadio, pois assim a gente pode usar ele depois sem 
    precisar treinar tudo de novo.
    """

    with open(filepath, 'wb') as f:
        pickle.dump(model, f)


# In[4]:


def load_model(filepath):
    """
    Usei essa função para carregar o modelo que foi salvo em um arquivo .pkl
    para usar em previsões futuras.
    """

    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

