from nltk import tokenize, word_tokenize, pos_tag, chunk

texto = 'Mr. Green killed Coronel Mustard in the study with candlestick. Mr. Green is not a very nice fellow.'

print(texto)

# Separação de frases com split
print(texto.split('.'))

# Separação de frases com o Tokenize do NLTK
print(tokenize.sent_tokenize(texto))

# Obtenção de palavras de uma frase
tokens = word_tokenize(texto)
print(tokens)

# Obtenção de etiquetas dos tokens
# A descrição de cada etiqueta pode ser encontrada em https://cs.nyu.edu/grishman/jet/guide/PennPOS.html
classes = pos_tag(tokens)
print(classes)

# Deteção de entidades
# Requer o "numpy" instalado > "pip install numpy"
entidades = chunk.ne_chunk(classes)
print(entidades)
