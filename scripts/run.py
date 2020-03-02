from nltk import corpus, stem, FreqDist, metrics
from nltk.metrics import ConfusionMatrix

from database import base_simples, stop_words

stop_words_nltk = corpus.stopwords.words('portuguese')
stop_words_nltk.extend(['tão', 'vou', 'vai'])
print(f'Carregado conjunto de stop words do NLTK com {len(stop_words_nltk)} palavras em Portugês')

def remove_stop_words(text):
  return [
    p for p in text.split() if p not in stop_words_nltk
  ]

# Remove "stop words" do texto do parâmetro
def remove_stop_words_database(database):
   frases = []

   for (frase, emocao) in database:
      frase_sem_stop_words = remove_stop_words(frase)
      frases.append((frase_sem_stop_words, emocao))

   return frases
