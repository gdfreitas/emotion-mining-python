# emotion-mining-python

Mineração de emoção em textos utilizando a linguagem Python.

## Mineração de textos

Atualmente temos inúmeras fontes de armazenamento de textos:

- Livros
- Jornais
- Revistas
- Páginas Web
- Blogs
- **Redes Sociais**
- E-mails
- Arquivos em PDF, XML e JSON
- ... etc

Estas fontes são ricas para se encontrar e extrair padrões de textos.

Uma característica importante é que estes tipos de dados normalmente não possuem um esquema para descrever sua estrutura de armazenamento, eles estão armazenados em diversos formatos, o que dificulta a interpretação do dado.

Há basicamente dois tipos de textos

- **Formatado**: possuem _tags_ que definem onde que está o título, os autores, etc.
  - Ex: Arquivo XML, JSON, HTML, etc
- **Livre**: não possuem indicadores explícitos, estão num formato puro
  - Ex: O corpo de um e-mail, uma postagem de rede social, etc.

## Técnicas de Mineração de Textos

### Classificação

É utilizada para reconhecer padrões que **descrevem** o grupo ao qual um determinado item pertence. Chega numa saída por meio do exame dos itens já classificados e pela inferência de um conjunto de regras.

#### Classificação Exemplo 1

Pode ser usado para **classificação de mensagens de spam** através mensagens recebidas em caixas de e-mails como Gmail, Outlook para determinar e-mails de spam

1. **Entrada**: Mensagem (assunto, texto)
1. **Classificador**
1. **Saída**: Classe da Mensagem (normal, spam, etc)

#### Classificação Exemplo 2

Pode ser utilizado para **classificação de notícia**, onde um jornalista cadastra um texto de uma notícia e o mesmo é processado para determinar automáticamente os tópicos para indexação da notícia.

1. **Entrada**: Texto da notícia
1. **Classificador Multirrótulo**
1. **Saída**: Tópicos (esporte, rio de janeiro, economia, etc)

> ℹ️ Outros exemplos mais aprofundados podem ser encontrados em [`docs/classificacao.md`](docs/classificacao.md)

### Agrupamento _(Clustering)_

É semelhante a **Classificação** só que para grupos ainda não definidos.

#### Agrupamento Exemplo 1

Pode ser utilizado numa fonte como o IBGE para a **descoberta de bairros similares** (Jardim Angélica e Jdim Angélica), evitando problemas como erros de digitação

#### Agrupamento Exemplo 2

É utilizado por revistas científicas para **detecção de plágio** na submissão de artigos com frases e palavras similares à outros já publicados.

### Extração de Informação

Ter um texto livre e extrair atributos que estão descritos neste texto.

#### Extração de Informação Exemplo 1

Dado o **texto**:

> "Apesar de ter sido escrito em 1516, Utopia continua sendo um dos mais interessantes livros sobre pensamento político. A obra de Thomas More descreve uma ilha imaginária onde não existe propriedade privada e todos se preocupam com o bem da coletividade. A nova edição foi lançada pela Editora XYZ e está sendo vendida por R$ 9,90"

Pode ser extraído o **template** abaixo:

- Livro: Utopia
- Ano: 1516
- País: -
- Autor: Thomas More
- Editora: XYZ
- Preço: 9,90

#### Extração de Informação Exemplo 2

Baseado no exemplo acima, é possível ainda fazer a utilização de **ontologias** para representar **conceitos e relacionamentos** em um determinado domínio (a biblioteca NLTK possui algumas funcionalidades para trabalhar com isso)

Exemplo de um relacionamento de entidades:

> `Livro {nome: "Utopia"}` é escrito por `Autor {nome: "Thomas More"}` em `País {nome: "Brasil"}` quando `Data {ano: 1516}`

### Associação

É utilizada para se obter a correlação entre palavras

Nesta técnica temos um exemplo clássico, do Walmart, onde foi identificado que sempre que se vendia fralda também se vendia cerveja, fazendo-os reposicionar fisicamente os objetos nos supermercados para aprimorar vendas.

#### Associação Exemplo 1

Dado que:

> 60% dos textos que contêm a palavra 'Internacional' também contêm a palavra 'Grêmio'. 3% de todos os textos contêm ambas as palavras

Temos a **Representação de Correlação: {"Internacional"} <-> {"Grêmio}**

#### Associação Exemplo 2

Dado que:

> A presença do termo 'Pelé' aumenta 5 vezes a chance de ocorrência dos termos 'Copa' e '1970'

Temos a **Representação de Correlação: {"Pelé"} <-> {"Copa", "1970"}**

### Casamento de Esquemas

Pode ser utilizado para entender correspondências semânticas (mesmos significados)

#### Casamento de Esquemas Exemplo 1

Migração de dados entre duas bases de dados, onde possuem tabela origem e destino porém com a **primary_key** com nomes diferentes. É usado então entender automáticamente o de-para dos campos.

#### Casamento de Esquemas Exemplo 2

Através de um algorítimo de correspondência **(matcher)** permitir que um usuário esquema uma consulta em linguagem natural e a mesma ser convertida para um select no banco de dados.

Consulta do usuário:

> Encontre os livros do Robert C. Martin ***via texto ou voz com técnicas de processamento de linguagem natural (PLN)***

Saída:

```sql
SELECT titulo, ano, resumo FROM publicacoes WHERE autor like '%Robert C. Martin%' and tipo = 'livro'
```

### Recuperação da Informação

É utilizada para **localizar e ranquear** documentos relevantes em uma coleção de documentos. Esta técnica é utilizada pela ferramenta **Apache Lucene**

Onde podemos ter uma tabela hash de palavras que apontam para documentos que a contenham.

| Palavra    | Ponteiro 1      | Ponteiro 2      | Ponteiro 3   | Ponteiro 4   |
| ---------- | --------------- | --------------- | ------------ | ------------ |
| "goleador" | Documento 3     | Documento 12    |              |              |
| "goleiro"  | Documento 7     | **Documento 1** | Documento 27 | Documento 19 |
| "gol"      | **Documento 1** | **Documento 2** |              |              |

**Documento 1**: "... um belo **gol** no segundo tempo..."

**Documento 2**: "Não aconteceu nenhum **gol** por conta de ..."

### Sumarização de Documentos

É aplicado algoritmo de sumarização em um texto com bastante linhas e obtêm-se um **resumo do texto** com os principais pontos em poucas linhas.

## Abordagens para Mineração de Texto

1. **Estatística**: Frequência dos termos, ignorando informações semânticas.
1. **Processamento de Linguagem Natural (PLN)**:
   - Interpretação sintática e semântica das frases.
   - Fazer o computador entender textos escritos em linguagem humana.

## Mineração de Emoção

A **mineração de emoção em textos** faz parte da **mineração de textos** e é utilizado a técnica de **classificação**

Em que cenários se faz útil?

- Monitoramento de marcas, entidades, figuras sociais
  - Ex: uma pessoa compra uma televisão, e faz um review na Internet, dependendo da emoção transmitida a empresa pode tomar uma decisão, como por exemplo, caso não esteja insatisfeito é bastante provavel que a emoção seja **raiva**
- Gestão de crises;
- Entender o que as pessoas pensam;

### Classificação por Polaridade

Também chamada de **valência** é submetido um texto em um algoritmo e recebe-se uma categoria dessas três: "Positivo", "Neutro" e "Negativo".

### Classificação por Emoção (Paul Ekman)

Segundo estudo do Paul Ekman, o ser humano consegue expressar 6 emoções bases:

1. Supresa
2. Alegria
3. Tristeza
4. Medo
5. Disgosto
6. Raiva

## Classificação em Textos

- **Atributos previsores**: As próprias palavras
- **Atributo meta (classe)**: Emoção (alegria e medo)

| Frase                        | Classe  |
| ---------------------------- | ------- |
| Me sinto completamente amado | Alegria |
| Eu estou muito bem hoje      | Alegria |
| Isso me deixa apavorada      | Medo    |
| Este lugar é apavorante      | Medo    |

Abaixo, temos como ficaria uma base de dados da classificação acima.

Todas as características (atributos previsores) são dispostas nas colunas, **eliminando duplicados**, **eliminando stop words**.

> É comum em uma base real de trabalho possuir mais de 70.000 características.

> **"stop words"** são palavras que não são utilizadas devido ao seu baixo valor de relevância, diminuindo assim dimensão da base de dados (Ex: "a", "é", "ou", "e", "do", "deu")
> Há também outras técnicas como **"stemming"** que remove os radicais das palavras também para diminuir a dimensão da base de dados (Ex: livro, livrinho, livreto, livretiol) [Estrutura e Formação das Palavras - Morfologia - Raiz/Radical](https://www.soportugues.com.br/secoes/morf/morf2.php)

| Me  | Sinto | Completamente | Amado | Eu  | Estou | Muito | Bem | Hoje | Isso | Deixa | Apavorada | Este | Lugar | Apavorante | Classe  |
| --- | ----- | ------------- | ----- | --- | ----- | ----- | --- | ---- | ---- | ----- | --------- | ---- | ----- | ---------- | ------- |
| S   | S     | S             | S     | N   | N     | N     | N   | N    | N    | N     | N         | N    | N     | N          | Alegria |
| N   | N     | N             | N     | S   | S     | S     | S   | S    | N    | N     | N         | N    | N     | N          | Alegria |
| S   | N     | N             | N     | N   | N     | N     | N   | N    | S    | S     | S         | N    | N     | N          | Medo    |
| N   | N     | N             | N     | N   | N     | N     | N   | N    | N    | N     | N         | S    | S     | S          | Medo    |

## Ambiente em Python

- Instalar o Python `python v3+`
- Instalar dependências `pip install -r requirements.txt`

### Natural Language ToolKit - NLTK

É uma biblioteca para processamento de linguagem natural, escrita em Python

Possui varios recursos, como: classificação, tokenização, *stemming*, *tagging*, *parsing* e raciocínio semântico.

Um script de atualização da biblioteca pode ser encontrado em [`scripts/nltk_gui_update.py`](scripts/nltk_gui_update.py)

Criar um script em python para atualizar as coleções do NLTK

### Naive Bayes

É um algoritmo de abordagem probabilística (Teorema de Bayes)

É bastante utilizado em:

- Filtros de spam em e-mails, analizando a probabilidade das palavras do seu conteúdo estarem relacionadas a e-mails de spam.
- Mineração de emoções, área de computação afetiva (sub área de inteligência artificial), dado um texto é identificado a emoção do texto, podendo ser usado para avaliar o grau de satisfação dos clientes por comentários relativos a um produto.

Exemplo em [./docs/naive_bayes.md](./docs/naive_bayes.md)

## Scripts

Exemplos práticos em no diretório [`./scripts`](`./scripts`)

## Avaliação do algoritmo

- Base de dados de teste
- Base de dados de treinamento (bem maior que a de testes)

Ambas já possuem registros classificados, onde serão aplicados cada registro da base de teste num algoritmo da base de treinamento, e os erros e acertos serão medidos. É importante que os **registros das bases sejam diferentes**, para não influenciar no teste do algoritmo, um cenário de exemplo é um professor passar 10 questões no quadro para revisão um dia antes da prova, e no dia da prova, passar as mesmas 10 questões, isso não irá de fato medir o conhecimento.

### Características para se levar em consideração antes do uso

1. Cenário
2. Número de classes (com as 6 emoções, o algoritmo alcançou acerto de 39%)
3. "zero-rules" dependendo da aplicação este método é mais aplicável (classifica todas as frases com base na classe mais utilizada)

## Referências

- [Top Five Emotion / Sentiment Analysis APIs for understanding user sentiment trends.](https://medium.com/@Mandysidana/top-five-emotional-sentiment-analysis-apis-116cd8d42055)
- [Mineração de Emoção em Textos com Python e NLKT @ Udemy](https://www.udemy.com/mineracao-de-emocao-em-textos-com-python-e-nltk)
- [Introdução ao NLTK na Prática](https://www.youtube.com/watch?v=siVUal-TeMc)
- [NLTK em Português](http://www.nltk.org/howto/portuguese_en.html)
- [Penn Part of Speech Tags](https://cs.nyu.edu/grishman/jet/guide/PennPOS.html)
- [Estrutura e formação de palavras - Raiz e radical](https://www.soportugues.com.br/secoes/morf/morf2.php)
- [Stemming words with NLTK](https://pythonprogramming.net/stemming-nltk-tutorial/)
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables)
