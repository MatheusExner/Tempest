import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# carregar arquivo csv
data = pd.read_csv('dados.csv')

# Extrair features e a variavel aprovado
X = data.drop('Aprovado', axis=1)  # (todas colunas, menos 'Aprovado')
y = data['Aprovado']  # obter variavel do dataset

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, train_size=0.75, random_state=42)

# Treina a LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

# Define os candidatos a serem avaliados
candidato_1 = {'nota_avaliacao': 6, 'nota_ingles': 7, 'nota_dinamica': 6, 'nota_entrevista': 5, 'monitoria': 0, 'iniciacao_cientifica': 0, 'vulnerabilidades_reportadas': 0}
candidato_2 = {'nota_avaliacao': 6, 'nota_ingles': 9, 'nota_dinamica': 8, 'nota_entrevista': 6, 'monitoria': 1, 'iniciacao_cientifica': 0, 'vulnerabilidades_reportadas': 1}
candidato_3 = {'nota_avaliacao': 7, 'nota_ingles': 8, 'nota_dinamica': 8, 'nota_entrevista': 5, 'monitoria': 0, 'iniciacao_cientifica': 1, 'vulnerabilidades_reportadas': 0}

# Faz a previsao dos candidatos
candidatos = [candidato_1, candidato_2, candidato_3]
predictions = model.predict(pd.DataFrame(candidatos))

# Print dos predictions
for i, candidate in enumerate(candidatos):
    print("Candidato", i+1, ", Aprovado (previsao):", predictions[i])
