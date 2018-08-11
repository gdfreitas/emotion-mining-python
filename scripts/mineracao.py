import nltk

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
# print(stop_words_nltk)

def remove_stop_words(text):
   frases = []
   for (palavras, emocao) in text:
      sem_stop = [p for p in palavras.split() if p not in stop_words_nltk] # faz o split da frase em palavras e e desconsidera as stop_words
      frases.append((sem_stop, emocao))
   return frases

#print(remove_stop_words(base))
#print('\n')

def apply_stemmer(text):
   stemmer = nltk.stem.RSLPStemmer()
   frases = []
   for (palavras, emocao) in text:
      com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk] # aplica o stemming nas palavras da frase e desconsidera as stop_words
      frases.append((com_stemming, emocao))
   return frases

frases_stemming = apply_stemmer(base)
#print(apply_stemmer(base))

def find_words(frases):
   all_words = []
   for (palavras, emocao) in frases:
      all_words.extend(palavras)
   return all_words

palavras = find_words(frases_stemming) 

def find_frequency(palavras):
   return nltk.FreqDist(palavras)

frequencia = find_frequency(palavras)
# print(frequencia.most_common(50))

def find_unique_words(frequency):
   return frequency.keys()

unique_words = find_unique_words(frequencia)
print(unique_words)