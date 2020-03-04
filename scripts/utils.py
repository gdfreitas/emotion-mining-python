from nltk.metrics import ConfusionMatrix

# Método imprime a probabilidade de cada palavra
def print_probabilidade_classificacao(classificador, tabela):
   print("classificacão mais alta: ", classificador.classify(tabela))
   distribuicao = classificador.prob_classify(tabela)
   for classe in distribuicao.samples():
      print("%s: %f" % (classe, distribuicao.prob(classe)))

# Método classifica cada frase novamente e imprime as que estão classificadas errado
def classify_and_test_accurary(classificador, base):
   erros = []
   for (frase, classe) in base:
      resultado = classificador.classify(frase)
      if resultado != classe:
         erros.append((classe, resultado, frase))

   for (classe, resultado, frase) in erros:
      print(classe, resultado) #, frase)

def print_confusion_matrix(classificador, base):
   esperado = []
   previsto = []
   for (frase, classe) in base:
      resultado = classificador.classify(frase)
      previsto.append(resultado)
      esperado.append(classe)
   print(ConfusionMatrix(esperado, previsto))
