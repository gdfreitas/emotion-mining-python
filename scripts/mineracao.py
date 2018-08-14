import nltk

## Base de dados original
base = [
   ('eu sou admirada por muitos','alegria'),
   ('me sinto completamente amado','alegria'),
   ('amar e maravilhoso','alegria'),
   ('estou me sentindo muito animado novamente','alegria'),
   ('eu estou muito bem hoje','alegria'),
   ('que belo dia para dirigir um carro novo','alegria'),
   ('o dia está muito bonito','alegria'),
   ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
   ('o amor e lindo','alegria'),
   ('nossa amizade e amor vai durar para sempre', 'alegria'),
   ('estou amedrontado', 'medo'),
   ('ele esta me ameacando a dias', 'medo'),
   ('isso me deixa apavorada', 'medo'),
   ('este lugar e apavorante', 'medo'),
   ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
   ('tome cuidado com o lobisomem', 'medo'),
   ('se eles descobrirem estamos encrencados', 'medo'),
   ('estou tremendo de medo', 'medo'),
   ('eu tenho muito medo dele', 'medo'),
   ('estou com medo do resultado dos meus testes', 'medo')
]

stop_words = [
   'a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
   'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
   'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou'
]

stop_words_nltk = nltk.corpus.stopwords.words('portuguese')

# Método para remover as stop words que são palavras que não possuem relevância para o entendimento do contexto, se é uma emoção de alegria ou de medo.
def remove_stop_words(text):
   frases = []
   for (palavras, emocao) in text:
      sem_stop = [p for p in palavras.split() if p not in stop_words_nltk] # faz o split da frase em palavras e e desconsidera as stop_words
      frases.append((sem_stop, emocao))
   return frases

# Método para remover o radical das palavras
def apply_stemmer(text):
   stemmer = nltk.stem.RSLPStemmer() # stemmer usado com a linguagem português
   frases = []
   for (palavras, emocao) in text:
      com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk] # aplica o stemming nas palavras da frase e desconsidera as stop_words
      frases.append((com_stemming, emocao))
   return frases

def apply_stemmer_phrase_only(text):
   stemmer = nltk.stem.RSLPStemmer() # stemmer usado com a linguagem português
   palavras_result = []
   for (palavras) in text.split():
      com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk] # aplica o stemming nas palavras da frase e desconsidera as stop_words
      if (com_stemming):
         palavras_result.append(str(com_stemming[0]))
   return palavras_result

frases_stemming = apply_stemmer(base)

# Método para buscar todas as palavras que existem na base de dados
def find_words(frases):
   all_words = []
   for (palavras, emocao) in frases:
      all_words.extend(palavras)
   return all_words

palavras = find_words(frases_stemming) 

# Método para buscar a frequência das palavras
def find_frequency(palavras):
   return nltk.FreqDist(palavras)

frequencia = find_frequency(palavras)

# Método para encontrar as palavras únicas conforme a frequência
def find_unique_words(frequency):
   return frequency.keys()

unique_words = find_unique_words(frequencia)

# Método para verificar se as palavras do parâmetro existem ou não na unique_words
def words_extractor(documento):
   doc = set(documento)
   caracteristicas = {}
   for word in unique_words:
      caracteristicas['%s' % word] = (word in doc)
   return caracteristicas

caracteristicas = words_extractor(['am', 'nov', 'dia'])

def print_probabilidade_classificacao(tabela):
   distribuicao = classificador.prob_classify(tabela)
   for classe in distribuicao.samples():
      print("%s: %f" % (classe, distribuicao.prob(classe)))

# Aplica classificador com base nos métodos implementados anteriores
base_completa = nltk.classify.apply_features(words_extractor, frases_stemming)

# Constrói a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(base_completa)

# Exibe os rótulos/classes
# print(classificador.labels())

# Exibe as 5 palavras mais informativas e sua probabilidade em relação aos rótulos
# print(classificador.show_most_informative_features(5))

def apply_and_print_results(texto):
   texto_stemmed = apply_stemmer_phrase_only(texto)
   
   tabela_probabilistica = words_extractor(texto_stemmed)
   print("\nA frase \"%s\"" % texto, "foi classificada como:",  classificador.classify(tabela_probabilistica))
   print(texto_stemmed)
   print_probabilidade_classificacao(tabela_probabilistica)

apply_and_print_results('estou com medo')
apply_and_print_results('eu sinto amor por você')
apply_and_print_results('hoje meu dia está feliz')
apply_and_print_results('eu te amo')