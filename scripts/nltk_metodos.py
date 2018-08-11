import nltk
#nltk.download()

texto = 'Mr. Green killed Coronel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.'
#print(texto.split('.'))

frases = nltk.tokenize.sent_tokenize(texto)
#print(frases)

tokens = nltk.word_tokenize(texto)
#print(tokens)

classes = nltk.pos_tag(tokens)
#print(classes)

entidades = nltk.chunk.ne_chunk(classes)
#print(entidades)
