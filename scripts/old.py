import nltk
import database
import impl

frases_com_stemming_treinamento = impl.apply_stemmer(data.base_treinamento)
frases_com_stemming_teste = impl.apply_stemmer(data.base_teste)

palavras_com_stemming_treinamento = impl.concat_words(frases_com_stemming_treinamento)
palavras_com_stemming_teste = impl.concat_words(frases_com_stemming_teste)

frequencias_treinamento = impl.find_frequency(palavras_com_stemming_treinamento)
frequencias_teste = impl.find_frequency(palavras_com_stemming_teste)

palavras_unicas_treinamento = impl.find_unique_words(frequencias_treinamento)
palavras_unicas_teste = impl.find_unique_words(frequencias_teste)

# Método aplica e imprime os resultados
def apply_and_print_results(classificador, texto):
   documento = impl.apply_stemmer_text(texto)
   tabela_probabilistica = words_extractor_treinamento(documento)
   print("\nA frase \"%s\"" % texto, "foi classificada como:",  classificador.classify(tabela_probabilistica))
   impl.print_probabilidade_classificacao(classificador, tabela_probabilistica)

# aplica classificador com base nos métodos implementados anteriores
base_completa_treinamento = nltk.classify.apply_features(words_extractor_treinamento, frases_com_stemming_treinamento)
base_completa_teste = nltk.classify.apply_features(words_extractor_teste, frases_com_stemming_teste)

# constrói a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(base_completa_treinamento)

# exibe precisão do algoritmo
# print(nltk.classify.accuracy(classificador, base_completa_treinamento))
# print(nltk.classify.accuracy(classificador, base_completa_teste))

# exibe os rótulos/classes
# print(classificador.labels())

# exibe as 5 palavras mais informativas e sua probabilidade em relação aos rótulos
# print(classificador.show_most_informative_features(20))

# tabela_probabilistica = words_extractor_treinamento('voce é muito bonita')
# impl.print_probabilidade_classificacao(classificador, tabela_probabilistica)

# classifica e imprime os as classes classificadas erradas pelo algoritmo
# impl.classify_and_test_accurary(classificador, base_completa_teste)
# impl.classify_and_test_accurary(classificador, base_completa_treinamento)

# imprime matriz de confusão, permite verificar os acertos por classe
impl.print_confusion_matrix(classificador, base_completa_teste)

# PERCENTUAL DE ACERTO = soma dos valores da diagonal principal divido pela soma de todos os valores
