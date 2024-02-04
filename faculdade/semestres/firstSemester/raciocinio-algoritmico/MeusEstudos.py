# Importando as bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregando o conjunto de dados iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividindo o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Criando um modelo de árvore de decisão
modelo = DecisionTreeClassifier()

# Treinando o modelo com os dados de treinamento
modelo.fit(X_train, y_train)

# Fazendo previsões com os dados de teste
y_pred = modelo.predict(X_test)

# Calculando a precisão do modelo
precisao = accuracy_score(y_test, y_pred)

# Exibindo a precisão do modelo
print("Precisão: ", precisao)
