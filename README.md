# python-emotion-mining

Curso sobre mineração de emoção em textos utilizando a linguagem Python.

## Seções

1. Mineração de textos e classificação
2. Pré-processamento dos textos
3. Detectando emoções em textos com Naive Bayes
4. Avaliação do algoritmo
5. Considerações finais

### 1. Mineração de textos e classificação

#### Formas de armazenamento de textos

- Livros, jornais, revistas, páginas web, blogs, redes sociais, e-mails, PDF, XML e JSON, etc.
- Geralmente não possuem um "esquema" para descrever sua estrutura
- Texto "livre" vs texto "formatado"

#### Classificadores

- mensagem (assunto, texto) &rarr; algoritmo classificador &rarr; classe da mensagem (normal, spam, etc)

- texto de notícia &rarr; algorítimo classificador multirrótulo &rarr; tópicos (esporte, rio de janeiro, economia)

#### Agrupamentos _(Clustering)_

- IBGE na descoberta de bairros com nomes similares (`Jardim América` = `Jdim América`)

- Detecção de plágio

#### Extração de informação

Texto "livre" &rarr; `{ livro: "Utopia", ano: 1516, pais: "Brasil", autor: "Thomas More"}`

Utilização de ontologias, representando conceitos e relacionamentos em um determinado domínio
`Livro { nome: "Utopia" }` é escrito por `Autor { nome: "Thomas More"}` em `País {nome: "Brasil"}` quando `Data { ano: 1516 }`

NLTK &rarr; ferramentas prontas para identificação de pessoas/empresas em textos

### 2. Pré-processamento dos textos

_Sem conteúdo ainda_.

### 3. Detectando emoções em textos com Naive Bayes

_Sem conteúdo ainda_.

### 4. Avaliação do algoritmo

_Sem conteúdo ainda_.

### 5. Considerações finais

_Sem conteúdo ainda_.

## Referências

- [Mineração de Emoção em Textos com Python e NLKT @ Udemy](https://www.udemy.com/mineracao-de-emocao-em-textos-com-python-e-nltk)