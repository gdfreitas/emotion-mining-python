# python-emotion-mining
Estudos sobre mineração de emoção em textos em Python

## Módulos
1. Mineração de textos
2. Mineração de emoções
3. Classificação
4. Classificação em textos

## Mineração de textos
### Diversas formas de armazenamento de textos
- Livros, jornais, revistas, páginas web, blogs, redes sociais, e-mails, PDF, XML e JSON, etc.
- Geralmente não possuem um "esquema" para descrever sua estrutura
- Texto "livre" vs texto "formatado"

### Classificadores
- mensagem (assunto, texto) &rarr; algoritmo classificador &rarr; classe da mensagem (normal, spam, etc)

- texto de notícia &rarr; algorítimo classificador multirrótulo &rarr; tópicos (esporte, rio de janeiro, economia)

### Agrupamentos _Clustering_

- IBGE na descoberta de bairros com nomes similares (`Jardim América` = `Jdim América`)

- Detecção de plágio

### Extração de informação

Texto "livre" &rarr; `{ livro: "Utopia", ano: 1516, pais: "Brasil", autor: "Thomas More"}`

Utilização de ontologias, representando conceitos e relacionamentos em um determinado domínio
`Livro { nome: "Utopia" }` é escrito por `Autor { nome: "Thomas More"}` em `País {nome: "Brasil"}` quando `Data { ano: 1516 }`

NLTK &rarr; ferramentas prontas para identificação de pessoas/empresas em textos