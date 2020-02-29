# Classificação

- Cada registro pertence a uma classe que possui um conjunto de atributos previsores;
- Objetiva-se descobrir um relacionamento entre os atributos previsores e o atributo meta;
- O valor do atributo meta é conhecido através de aprendizagem superviosionada;

## Tabela de treinamento (Classificação de risco de crédito)

Atributos previsores: histórica do crédito, divida, garantias, renda anual;
Atributo meta (classe): risco.

| História do crédito | Dívida | Garantias | Renda anual           | Risco    |
|---------------------|--------|-----------|-----------------------|----------|
| Ruim                | Alta   | Nenhuma   | < 15.000              | Alto     |
| Desconhecida        | Alta   | Nenhuma   | >= 15.000 a <= 35.000 | Alto     |
| Desconhecida        | Baixa  | Nenhuma   | >= 15.000 a <= 35.000 | Moderado |
| Desconhecida        | Baixa  | Nenhuma   | < 15.000              | Alto     |
| Desconhecida        | Baixa  | Nenhuma   | > 35.000              | Baixo    |
| Desconhecida        | Baixa  | Adequada  | > 35.000              | Baixo    |
| Ruim                | Baixa  | Nenhuma   | < 15.000              | Alto     |
| Ruim                | Baixa  | Adequada  | > 35.000              | Moderado |
| Boa                 | Baixa  | Nenhuma   | > 35.000              | Baixo    |
| Boa                 | Alta   | Adequada  | > 35.000              | Baixo    |
| Boa                 | Alta   | Nenhuma   | < 15.000              | Alto     |
| Boa                 | Alta   | Nenhuma   | >= 15.000 a <= 35.000 | Moderado |
| Boa                 | Alta   | Nenhuma   | > 35.0000             | Baixo    |
| Ruim                | Alta   | Nenhuma   | >= 15.000 a <= 35.000 | Alto     |

## Tabela de testes (Classificação de risco de crédito)

| História do crédito | Dívida | Garantias | Renda anual           |
|---------------------|--------|-----------|-----------------------|
| Ruim                | Alta   | Adequada  | < 15.000              |
| Desconhecida        | Alta   | Adequada  | < 15.000              |
| Desconhecida        | Baixa  | Nenhuma   | > 35.000              |
| Boa                 | Alta   | Adequada  | >= 15.000 a <= 35.000 |

## Tabela de treinamento (Classificação de vendas de livros)

Atributos previsores: sexo, país, idade;
Atributo meta (classe): comprar.

| Sexo | País       | Idade | Comprar |
|------|------------|-------|---------|
| M    | França     | 25    | Sim     |
| M    | Inglaterra | 21    | Sim     |
| F    | França     | 23    | Sim     |
| F    | Inglaterra | 34    | Sim     |
| F    | França     | 30    | Não     |
| M    | Alemanha   | 21    | Não     |
| M    | Alemanha   | 20    | Não     |
| F    | Alemanha   | 18    | Não     |
| F    | França     | 34    | Não     |
| F    | França     | 34    | Não     |
| M    | França     | 55    | Não     |
| M    | Inglaterra | 25    | Sim     |
| M    | Alemanha   | 48    | Sim     |
| F    | Inglaterra | 23    | Não     |

## Tabela de testes (Classificação de vendas de livros)

| Sexo | País       | Idade |
|------|------------|-------|
| M    | França     | 38    |
| F    | Inglaterra | 25    |
| M    | Alemanha   | 55    |
| F    | França     | 20    |

## Representação da classificação

- Método indutivo:
  - Fase 1: conjunto de exemplos + atributos previsores + atributo meta > sistema de aprendizado (algoritmos) > gera um classificador (modelo).
  - Fase 2: caso a ser classificado (atributo meta não conhecido) > classificador > decisão.

- Aprendizagem supervisionada (indução):
  - Fase 1: uma imagem do Homer Simpson e do Bart Simpson > extração de características (cores de roupas, pele, cabelo, etc) > algoritmo de aprendizagem (supervisor) > modelo aprendido.
  - Fase 2: imagem do Bart Simpson > extração de caraterísticas > modelo aprendido > Bart Simpson;

## Classificação em textos

| Frase                      | Classe  |
|----------------------------|---------|
|Me sinto completamente amado| Alegria |
|Eu estou muito bem hoje     | Alegria |
|Isso me deixa apavorada     | Medo    |
|Este lugar é apavorante     | Medo    |

Como ficaria uma base de dados da classificação acima:

Todas as características (atributos previsores) estão dispostas nas colunas, eliminando duplicidades, eliminando stop words (Ex: "é"). É comum em uma base real de trabalho possuir mais de 70.000 características.

| Me | Sinto | Completamente | Amado | Eu | Estou | Muito | Bem | Hoje | Isso | Deixa | Apavorada | Este | Lugar | Apavorante |  Classe |
|:--:|:-----:|:-------------:|:-----:|:--:|:-----:|:-----:|:---:|:----:|:----:|:-----:|:---------:|:----:|:-----:|:----------:|:-------:|
|  S |   S   |       S       |   S   |  N |   N   |   N   |  N  |   N  |   N  |   N   |     N     |   N  |   N   |      N     | Alegria |
|  N |   N   |       N       |   N   |  S |   S   |   S   |  S  |   S  |   N  |   N   |     N     |   N  |   N   |      N     | Alegria |
|  S |   N   |       N       |   N   |  N |   N   |   N   |  N  |   N  |   S  |   S   |     S     |   N  |   N   |      N     |   Medo  |
|  N |   N   |       N       |   N   |  N |   N   |   N   |  N  |   N  |   N  |   N   |     N     |   S  |   S   |      S     |   Medo  |
