import nltk
import data
import impl

frases_com_stemming = impl.apply_stemmer(data.base_treinamento)
palavras_com_stemming = impl.concat_words(frases_com_stemming)
frequencias = impl.find_frequency(palavras_com_stemming)
palavras_unicas = impl.find_unique_words(frequencias)

# método para verificar se as palavras do documento do parâmetro está na lista de palavras únicas
def words_extractor(documento):
   doc = set(documento)
   caracteristicas = {}
   for word in palavras_unicas:
      caracteristicas['%s' % word] = (word in doc)
   return caracteristicas

# Método aplica e imprime os resultados
def apply_and_print_results(classificador, texto):
   documento = impl.apply_stemmer_text(texto)
   tabela_probabilistica = words_extractor(documento)
   print("\nA frase \"%s\"" % texto, "foi classificada como:",  classificador.classify(tabela_probabilistica))
   impl.print_probabilidade_classificacao(classificador, tabela_probabilistica)

# aplica classificador com base nos métodos implementados anteriores
base_completa = nltk.classify.apply_features(words_extractor, frases_com_stemming)

# constrói a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(base_completa)

# exibe os rótulos/classes
# print(classificador.labels())

# exibe as 5 palavras mais informativas e sua probabilidade em relação aos rótulos
# print(classificador.show_most_informative_features(20))

tabela_probabilistica = words_extractor('voce é muito bonita')
impl.print_probabilidade_classificacao(classificador, tabela_probabilistica)