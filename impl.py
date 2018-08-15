import nltk

stop_words_nltk = nltk.corpus.stopwords.words('portuguese')

# adiciona stop words customizadas às do nltk
stop_words_nltk.extend(['tão', 'vou', 'vai'])

# Método para remover as "stop words" do texto do parâmetro.
# "stop words" são palavras que não possuem relevância para o entendimento do contexto
def remove_stop_words(text):
   frases = []
   for (palavras, emocao) in text:
      sem_stop = [p for p in palavras.split() if p not in stop_words_nltk]
      frases.append((sem_stop, emocao))
   return frases

# Método para reduzir palavras "flexionadas" até sua base/raiz, que é o suficiente para o entendimento
# "text_and_class" deve ser um objeto com a frase e a emoção classificada
def apply_stemmer(text_and_class):
   stemmer = nltk.stem.RSLPStemmer()  # stemmer usado com a linguagem português
   frases = []
   for (palavras, emocao) in text_and_class:
      com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk] # aplica o stemming nas palavras da frase e desconsidera as stop_words
      frases.append((com_stemming, emocao))
   return frases

# Método para reduzir palavras "flexionadas" até sua base/raiz, que é o suficiente para o entendimento
# "text" deve ser um texto
def apply_stemmer_text(text):
   stemmer = nltk.stem.RSLPStemmer() # stemmer usado com a linguagem português
   palavras_result = []
   for (palavras) in text.split():
      com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk] # aplica o stemming nas palavras da frase e desconsidera as stop_words
      if (com_stemming):
         palavras_result.append(str(com_stemming[0]))
   return palavras_result

# Método para separar concatenar todas as palavras da lista de frases do parâmetro
def concat_words(frases):
   all_words = []
   for (palavras, emocao) in frases:
      all_words.extend(palavras)
   return all_words

# Método para identificar a frequência de cada palavra da lista do parâmetro
def find_frequency(palavras):
   return nltk.FreqDist(palavras)

# Método para encontrar as palavras únicas conforme a frequência
def find_unique_words(palavras):
   return find_frequency(palavras).keys()

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
   from nltk.metrics import ConfusionMatrix
   esperado = []
   previsto = []
   for (frase, classe) in base:
      resultado = classificador.classify(frase)
      previsto.append(resultado)
      esperado.append(classe)
   print(ConfusionMatrix(esperado, previsto))