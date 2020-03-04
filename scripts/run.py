from nltk import corpus, stem, FreqDist, metrics, classify
from nltk.metrics import ConfusionMatrix

from database import base_simples, stop_words

stop_words_nltk = corpus.stopwords.words('portuguese')
stop_words_nltk.extend(['tão', 'vou', 'vai'])
print(f'Carregado conjunto de stop words do NLTK com {len(stop_words_nltk)} palavras em Portugês')

def remove_stop_words(text):
  """
  Remove as "stop words" da text do parâmetro

  Parâmetros:
    text (string): Texto contendo palavras

  Retorna:
    (list): Lista de palavras sem "stop words"
  """
  return [
    word for word in text.split() if word not in stop_words_nltk
  ]

def transform_database_removing_stop_words(database):
  """
  Remove as "stop words" do database

  Parâmetros:
    database (list<tuple>): Lista de tupla (frase, emocao)

  Retorna
    (list<tuple>): Database modificado sem "stop words"
  """
  transformed_database = []

  for (frase, emocao) in database:
    frase_sem_stop_words = remove_stop_words(frase)
    transformed_database.append((' '.join(frase_sem_stop_words), emocao))

  return transformed_database

def transform_words_applying_stemming(text):
  """
  Aplica algoritmo de Stemming para reduzir as palavras da frase do parâmetro até sua base (raiz)
  O resultado apresentado auxilia na identificação do significado da palavra e diminuição de dimensão da base de dados

  Parâmetros:
    text (string): Texto contendo palavras
  """
  # stemmer usado com a linguagem português
  stemmer = stem.RSLPStemmer()
  transformed_words = []

  for word in text.split():
    stemmed_word = stemmer.stem(word)

    if (stemmed_word):
      transformed_words.append(stemmed_word)

  return transformed_words


def transform_words_applying_stemming_database(database):
  """
  Aplica algoritmo de Stemming para reduzir as palavras das frases do database do parâmetro até sua base (raiz)
  O resultado apresentado auxilia na identificação do significado da palavra e diminuição de dimensão da base de dados

  Parâmetros:
    database (list<tuple>): Lista de tupla (frase, emocao)

  Retorna
    (list<tuple>): Database modificado com stemming aplicado
  """
  transformed_database = []

  for (palavras, emocao) in database:
    transformed_words = transform_words_applying_stemming(palavras)
    transformed_database.append((' '.join(transformed_words), emocao))

  return transformed_database

def concat_words_database(database):
  """
  Concatena todas as palavras de todas as frases do database

  Parâmetros:
    database (list<tuple>): Lista de tupla (frase, _emocao)

  Retorna
    (list<string>): Lista de palavras
  """
  all_words = []

  for (frase, _emocao) in database:
    all_words.extend(frase.split())

  return all_words

# Método para identificar a frequência de cada palavra da lista do parâmetro
def find_frequency(words):
  return FreqDist(words)

# Método para identificar a frequência de cada palavra da lista do parâmetro
def find_most_common_words(words, count = 10):
  """
  Obtem as palavras mais frequentes

  Parâmetros:
    words (list<string>): Lista de palavras
    count (number): Numero maximo de palavras a ser exibida (considerando das mais frequentes às menos frequentes)

  Retorna
    (list<tuple>): Lista de tupla com a palavra e sua frequência
  """
  return find_frequency(words).most_common(count)

def find_unique_words(words):
  """
  Obtém as palavras únicas da lista do parâmetro (remove duplicadas)

  Parâmetros:
    words (list<string>): Lista de palavras

  Retorna
    (list<string>): Lista de palavras únidas
  """
  return find_frequency(words).keys()

def find_which_words_is_unique(unique_words, text):
  text_as_set = set(text)
  unique_words_object = {}

  for word in unique_words:
    unique_words_object['%s' % word] = (word in text_as_set)

  return unique_words_object

def print_space_between_logs():
  print('\n', '-'*50)

# Remove stop words em frase simples
# frase_simples = 'eu sou admirada por muitos'
# print(f'A frase "{frase_simples}" sem "stop words" fica "{" ".join(remove_stop_words(frase_simples))}"')

# Remove stop words em database simples
database_without_stop_words = transform_database_removing_stop_words(base_simples)
print(database_without_stop_words)
print_space_between_logs()

# Aplica algoritmo de stemming em frase simples
# frase_com_palavras_flexionadas = 'eu sou admirada por muitos'
# print(transform_words_applying_stemming(frase_com_palavras_flexionadas))

# Aplica algoritmo de stemming em database simples
stemmed_database = transform_words_applying_stemming_database(database_without_stop_words)
print(stemmed_database)
print_space_between_logs()

# Obtem uma lista de todas as palavras de uma base de dados
# print(concat_words_database(base_simples))

# Compara diferença entre quantidade de palavras após remoção de stop words e aplicação de stemming
all_words_original_database = concat_words_database(base_simples)
all_words_transformed_database = concat_words_database(stemmed_database)
print(f'A base original continha {len(all_words_original_database)} palavras')
print(f'A base transformada contém {len(all_words_transformed_database)} palavras')
print_space_between_logs()

# Trabalha com a frequência das palavras, obtendo as 5 mais presentes
print(find_frequency(all_words_transformed_database).most_common(5))
print_space_between_logs()

# Remove palavras duplicadas
all_unique_words = find_unique_words(all_words_transformed_database)
print(all_unique_words)
print(f'A base transformada contém {len(all_unique_words)} palavras **únicas**')
print_space_between_logs()

# Obtem objeto de quais palavras da frase estao na lista de palavras únidas
print(find_which_words_is_unique(all_unique_words, ['admir', 'muit', 'sint']))

print_space_between_logs()

# Utilização do NLTK para classificar a base de dados inteira
def extractor_based_on_all_unique_words(text):
  text_as_set = set(text)
  unique_words_object = {}

  for word in all_unique_words:
    unique_words_object['%s' % word] = (word in text_as_set)

  return unique_words_object

classified_database = classify.apply_features(extractor_based_on_all_unique_words, stemmed_database)
print(classified_database)
