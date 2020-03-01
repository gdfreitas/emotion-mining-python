# Classificação

Principais conceitos

- Cada registro pertence a uma **classe** que possui um conjunto de **atributos previsores**
- Objetiva-se descobrir um **relacionamento (padrão)** entre os **atributos previsores** e o **atributo meta (classe)**
- O valor do **atributo meta** é conhecido através de **aprendizagem superviosionada**

## Exemplos

### Classificação de Risco de Crédito

Tabela de treinamento onde o esporte foi classificado por um **supervisor**

- **Atributos previsores**: Histórico do Crédito, Divida, Garantias, Renda Anual
- **Atributo meta (classe)**: Risco

| História do Crédito | Dívida | Garantias | Renda anual           | Risco    |
| ------------------- | ------ | --------- | --------------------- | -------- |
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

Tabela de testes

| História do crédito | Dívida | Garantias | Renda anual           |
| ------------------- | ------ | --------- | --------------------- |
| Ruim                | Alta   | Adequada  | < 15.000              |
| Desconhecida        | Alta   | Adequada  | < 15.000              |
| Desconhecida        | Baixa  | Nenhuma   | > 35.000              |
| Boa                 | Alta   | Adequada  | >= 15.000 a <= 35.000 |

### Classificação de Vendas de Livros

Tabela de treinamento onde o esporte foi classificado por um **supervisor**

- **Atributos previsores**: Sexo, País e Idade;
- **Atributo meta (classe)**: Tendência para comprar

| Sexo | País       | Idade | Tendência para comprar |
| ---- | ---------- | ----- | ---------------------- |
| M    | França     | 25    | Sim                    |
| M    | Inglaterra | 21    | Sim                    |
| F    | França     | 23    | Sim                    |
| F    | Inglaterra | 34    | Sim                    |
| F    | França     | 30    | Não                    |
| M    | Alemanha   | 21    | Não                    |
| M    | Alemanha   | 20    | Não                    |
| F    | Alemanha   | 18    | Não                    |
| F    | França     | 34    | Não                    |
| F    | França     | 34    | Não                    |
| M    | França     | 55    | Não                    |
| M    | Inglaterra | 25    | Sim                    |
| M    | Alemanha   | 48    | Sim                    |
| F    | Inglaterra | 23    | Não                    |

Tabela de testes

| Sexo | País       | Idade |
| ---- | ---------- | ----- |
| M    | França     | 38    |
| F    | Inglaterra | 25    |
| M    | Alemanha   | 55    |
| F    | França     | 20    |

### Classificação de Esporte Favorito

Tabela de treinamento onde o esporte foi classificado por um **supervisor**

- **Atributos previsores**: Cor dos olhos, Casado, Sexo e Cabelo;
- **Atributo meta (classe)**: Esporte Favorito

| Cor dos olhos | Casado | Sexo | Cabelo | Esporte Favorito |
| ------------- | ------ | ---- | ------ | ---------------- |
| Castanho      | Sim    | M    | Longo  | Futebol          |
| Azul          | Sim    | M    | Curto  | Futebol          |
| Castanho      | Sim    | M    | Longo  | Futebol          |
| Castanho      | Não    | F    | Longo  | Aeróbica         |
| Castanho      | Não    | F    | Longo  | Aeróbica         |
| Azul          | Não    | M    | Longo  | Futebol          |
| Castanho      | Não    | F    | Longo  | Aeróbica         |
| Castanho      | Não    | M    | Curto  | Futebol          |
| Castanho      | Sim    | F    | Curto  | Aeróbica         |
| Castanho      | Não    | F    | Longo  | Aeróbica         |
| Azul          | Não    | M    | Longo  | Futebol          |
| Azul          | Não    | M    | Curto  | Futebol          |

Tabela de testes

| Cor dos olhos | Casado | Sexo | Cabelo |
| ------------- | ------ | ---- | ------ |
| Castanho      | Sim    | M    | Curto  |
| Castanho      | Não    | M    | Longo  |
| Azul          | Não    | F    | Longo  |
| Azul          | Sim    | M    | Longo  |

### ClassificaçÃo de Tendência a Jogar Tênis

Tabela de treinamento onde a **tendência a jogar tênis** é por um **supervisor**

- **Atributos previsores**: Tempo, Temperatura, Umidade e Vento;
- **Atributo meta (classe)**: Tendência a jogar tênis

| Tempo      | Temperatura | Umidade | Vento | Tendência a jogar tênis |
| ---------- | ----------- | ------- | ----- | ----------------------- |
| Ensolarado | Quente      | Alta    | Fraco | Não                     |
| Ensolarado | Quente      | Alta    | Forte | Não                     |
| Nublado    | Quente      | Alta    | Fraco | Sim                     |
| Chuvoso    | Moderada    | Alta    | Fraco | Sim                     |
| Chuvoso    | Agradável   | Normal  | Fraco | Sim                     |
| Chuvoso    | Agradável   | Normal  | Forte | Não                     |
| Nublado    | Agradável   | Normal  | Forte | Sim                     |
| Ensolarado | Moderada    | Alta    | Fraco | Não                     |
| Ensolarado | Agradável   | Normal  | Fraco | Sim                     |
| Chuvoso    | Moderada    | Normal  | Fraco | Sim                     |
| Ensolarado | Moderada    | Normal  | Forte | Sim                     |
| Nublado    | Moderado    | Alta    | Fraco | Sim                     |
| Nublado    | Quente      | Normal  | Fraco | Sim                     |
| Chuvoso    | Moderado    | Alta    | Forte | Não                     |

Tabela de testes

| Tempo      | Temperatura | Umidade  | Vento |
| ---------- | ----------- | -------- | ----- |
| Tempo      | Temperatura | Humidade | Vento |
| Ensolarado | Moderada    | Normal   | Forte |
| Chuvoso    | Agradável   | Normal   | Fraco |
| Nublado    | Quente      | Normal   | Forte |
| Nublado    | Agradável   | Alta     | Forte |

## Representação da Classificação

### Método indutivo

Fase 1

- Conjunto de exemplos + Atributos Previsores + Atributo Meta
- Sistema de Aprendizado (algoritmos)
- Gera um Classificador (modelo)

Fase 2

- Caso a ser classificado (atributo meta não conhecido)
- Classificador
- Decisão

Exemplo de aprendizagem supervisionada pelo método de indução

Fase 1

- Imagem do Homer Simpson e do Bart Simpson
- Extração de características (cores de roupas, pele, cabelo, etc)
- Algoritmo de aprendizagem (supervisor)
- Modelo aprendido

Fase 2

- Imagem do Bart Simpson
- Extração de caraterísticas
- Modelo aprendido
- Bart Simpson
