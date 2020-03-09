from nltk import corpus, stem, FreqDist, metrics, classify, NaiveBayesClassifier
from nltk.metrics import ConfusionMatrix

from database import base_simples, base_treinamento,stop_words

def print_space_between_logs():
  print('\n', '-' * 20, '\n')

def remover_stop_words(text):
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

def imprimir_base_frase_classe(base_frase_classe):
  """
  Imprime uma lista de tuplas no formato (frase, classe)
  """
  for (frase, classe) in base_frase_classe:
    print(f'"{frase}": "{classe}"')

def remover_stop_words_base_frase_classe(database):
  """
  Remove as "stop words" do database

  Parâmetros:
    database (list<tuple>): Lista de tupla (frase, emocao)

  Retorna
    (list<tuple>): Database modificado sem "stop words"
  """
  transformed_database = []

  for (frase, emocao) in database:
    frase_sem_stop_words = remover_stop_words(frase)
    transformed_database.append((' '.join(frase_sem_stop_words), emocao))

  return transformed_database

def aplicar_stemming(text):
  """
  Aplica algoritmo de Stemming para reduzir as palavras da frase do parâmetro até sua base (raiz)
  O resultado apresentado auxilia na identificação do significado da palavra e diminuição de dimensão da base de dados

  Parâmetros:
    text (string): Texto contendo palavras

  Retorna:
    list<string>: Lista de palavras com stemming aplicado
  """
  # stemmer usado com a linguagem português
  stemmer = stem.RSLPStemmer()
  transformed_words = []

  for word in text.split():
    stemmed_word = stemmer.stem(word)

    if (stemmed_word):
      transformed_words.append(stemmed_word)

  return transformed_words


def aplicar_stemming_database(database):
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
    transformed_words = aplicar_stemming(palavras)
    transformed_database.append((' '.join(transformed_words), emocao))

  return transformed_database

def extrair_todas_palavras_base(database):
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
    (list<string>): Lista de palavras únicas
  """
  return find_frequency(words).keys()

def construir_linha_tabela_probabilidade(unique_words, words):
  """
  Monta tabela verdade com suas "colunas" sendo "unique_words" para as palavras em "words"

  Parâmetros:
    unique_words (list<string>): Lista de palavras únicas
    words (list<string>): Lista de palavras para verificar verdade na tabela

  Retorna:
    object: Tabela verdade
  """
  words_as_set = set(words)
  unique_words_object = {}

  for word in unique_words:
    unique_words_object['%s' % word] = (word in words_as_set)

  return unique_words_object


print_space_between_logs()

stop_words_nltk = corpus.stopwords.words('portuguese')
stop_words_nltk.extend(['tão', 'vou', 'vai'])

print(f'Carregado conjunto de stop words do NLTK com {len(stop_words_nltk)} palavras em Português')

print_space_between_logs()

# Remove stop words em frase simples
frase_simples = 'eu sou admirada por muitos'
print(f'A frase "{frase_simples}" sem stop words fica {remover_stop_words(frase_simples)}')

print_space_between_logs()

# Aplica stemming em frase simples
print(f'A frase "{frase_simples}" aplicando stemming fica {aplicar_stemming(frase_simples)}')

print_space_between_logs()

# Base simples (frase, classe) original
print('Base simples (frase, classe) original: \n')
imprimir_base_frase_classe(base_simples)
print_space_between_logs()

# Base simples (frase, classe) sem stop words
print('Base simples (frase, classe) sem stop words: \n')
base_simples_sem_stop_words = remover_stop_words_base_frase_classe(base_simples)
imprimir_base_frase_classe(base_simples_sem_stop_words)
print_space_between_logs()

# Base simples (frase, classe) sem stop words e com stemming aplicado
print('Base simples (frase, classe) sem stop words e com stemming aplicado: \n')
base_simples_sem_stop_words_stemmed = aplicar_stemming_database(base_simples_sem_stop_words)
imprimir_base_frase_classe(base_simples_sem_stop_words_stemmed)
print_space_between_logs()

# Estatísticas de palavras sobre a base de dados
print('Estatísticas de palavras sobre a base de dados\n')
todas_palavras_base_simples = extrair_todas_palavras_base(base_simples)
palavras_mais_frequentes_base_simples = find_frequency(todas_palavras_base_simples).most_common(5)
palavras_unicas_base_simples = find_unique_words(todas_palavras_base_simples)

todas_palavras_base_tratada = extrair_todas_palavras_base(base_simples_sem_stop_words_stemmed)
palavras_mais_frequentes_base_tratada = find_frequency(todas_palavras_base_tratada).most_common(5)
palavras_unicas_base_tratada = find_unique_words(todas_palavras_base_tratada)

print(f'A base original contém {len(todas_palavras_base_simples)} palavras')
print(f'Sendo as 5 mais comuns {palavras_mais_frequentes_base_simples}')
print(f'Removendo duplicadas, temos {len(palavras_unicas_base_simples)} palavras únicas')

print(f'\nA base tratada contém {len(todas_palavras_base_tratada)} palavras')
print(f'Sendo as 5 mais comuns {palavras_mais_frequentes_base_tratada}')
print(f'Removendo duplicadas, temos {len(palavras_unicas_base_tratada)} palavras únicas')
print_space_between_logs()

# Construção da tabela verdade
# Obtem tabela verdade de quais palavras da frase estao na lista de palavras únicas
frase_simples_tratada = aplicar_stemming(' '.join(remover_stop_words(frase_simples)))
print(f'Construindo uma linha de uma tabela de probabilidade para a frase "{frase_simples}" ({frase_simples_tratada})\n')
print(construir_linha_tabela_probabilidade(palavras_unicas_base_tratada, frase_simples_tratada))

print_space_between_logs()

# Define método que será utilizado pelo classificador do NLTK para extração montagem da tabela verdade da base inteira
def extrator_linha_nltk(frase):
  """
    Obtem uma frase e retorna um objeto de "tabela verdade" indicando true ou false correspondendo
    a existentica de cada palavra na lista de palavras da base de dados em "palavras_unicas_base_tratada"
  """
  palavras_da_frase = frase.split(' ')
  palavras_unicas_da_frase = set(palavras_da_frase)
  resultado_linha_palavra = {}

  for palavra_unica_base_tratada in palavras_unicas_base_tratada:
    resultado_linha_palavra['%s' % palavra_unica_base_tratada] = (palavra_unica_base_tratada in palavras_unicas_da_frase)

  # print(f'{frase}: {palavras_unicas_da_frase} : {resultado_linha_palavra}\n')

  return resultado_linha_palavra

# Base classificada
base_classificada = classify.apply_features(extrator_linha_nltk, base_simples_sem_stop_words_stemmed)

# Constrói classificador de probabilidade do Naive Bayes
classificador = NaiveBayesClassifier.train(base_classificada)

# Estatísticas do Classificador
print(f'As classes existentes na base classificada são {classificador.labels()}\n')
print(f'As 5 principais características são:')
classificador.show_most_informative_features(5)

print_space_between_logs()

# Utilizando o classificador
print(f'Utilizando classificador Naive Bayes para obter a classe\n')

def imprimir_classificacao_frase(frase):
  frase_tratada = ' '.join(aplicar_stemming(' '.join(remover_stop_words(frase))))
  linha_nova_frase_tratada = extrator_linha_nltk(frase_tratada)
  resultado_classe_frase_tratada = classificador.classify(linha_nova_frase_tratada)
  print(f'Para a frase "{frase}" ("{frase_tratada}") a classe é "{resultado_classe_frase_tratada}"')


imprimir_classificacao_frase('estou com muito medo')
imprimir_classificacao_frase('eu sinto amor por você')
imprimir_classificacao_frase('hoje é um belo dia')

print_space_between_logs()

# Obtendo valores de distribuição do classificador
print('Utilizando classificador Naive Bayes para obter os valores de distribuição das classes\n')

def imprimir_distribuicao_frase(frase):
  frase_tratada = ' '.join(aplicar_stemming(' '.join(remover_stop_words(frase))))
  linha_nova_frase_tratada = extrator_linha_nltk(frase_tratada)
  distribuicao = classificador.prob_classify(linha_nova_frase_tratada)
  print(f'Para a frase "{frase}" ("{frase_tratada}") obtemos a distribuição:\n')

  for classe in distribuicao.samples():
    print(f'> "{classe}" probabilidade de "{distribuicao.prob(classe)}"')

imprimir_distribuicao_frase('estou com muito medo')
print_space_between_logs()
imprimir_distribuicao_frase('eu sinto amor por você')
print_space_between_logs()
imprimir_distribuicao_frase('hoje é um belo dia')
print_space_between_logs()
imprimir_distribuicao_frase('eu te amo')
print_space_between_logs()
imprimir_distribuicao_frase('amor')
