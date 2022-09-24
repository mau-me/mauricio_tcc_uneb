# Anotações Gerais da Monografia

### O trabalho apresenta a analise, através de ferramentas de bioinformática e do algoritmo PSRM, de quais genes o Sars-Cov-2 utiliza para codigicar suas proteinas e assim poder entender como funciona sua evolução

## Intrudução

- Importância das árvores filogenéticas para a visualização dos descendentes partindo de ancestrais comuns
- Cladogênese
- Grupos monofiléticos
- Codon Based Unsupervised (CBUC)
  Consegur agrupar as sequências em famílias de forma semelhante ao agrupamento tradicional feito pela árvore filogenética
  Objetivo: Conseguir classificar de forma mais rápida e menos custosa uma nova sequência em um grupo monofilético. Confontrar dados do CBUC com os da filogenia tradicional
- PSRM
- Se o vírus quiser se replicar de forma eficiente, ele precisa sintetizar moléculas de mRNA com estruturas e códons aos quais a célula hospedeira produz eficientemente
- tRNA isoacceptor
- Proteína Spike do Sars-Cov-2
- GenBank
- Ferramenta de coleta de sequências e armazenamento em BD
- Implementação do Algoritmo PSRM em Python. (No meu caso, em linguagem C)

## Fundamentação Teórica

- Biologia Molecular
- Bioinformática
  - Coletar e interpretar dados biológicos
  - Análises
    - Genomica
    - Proteômica
    - Transcriptômica
  - Árvore Filogenética
    - Busca de um ancestral comum
  - Inferência Hennigiana
    - Primeiro método formal para reconstrução de filogenia (Não mais utilizado)
  - Critério de Maximum Parsimony
  - Abordagem baseada em modelos matemáticos
    - Modelos de Markov
    - Modelo Jukes-Cantor
    - Métodos de dostância
    - Maximum Likelihood
      - Determinar o likelihood da árvore
    - Inferência Bayesiana
      - Método de análise Markov Chain Monte Carlo (MCMC)
      - Análise Nomparametric Bootstrap
        - Avaliar a força de um clado
        - bootstrap score
  - PSRM
    - Etapa de Treinamento
      - Etapa de Partição
      - Etapa Aglomerativa
    - Etapa pós-treino
    - Operação e re-treino
    - Pré-processamento
      - Serial
      - Paralela
      - Híbrida

## Trabalhos Correlatos

- Frequências de uso de códos sinônimos com métodos estatísticos
  - Adaptação Relativa de Códon (RCA)
  - Uso Relativo de Códon Sinônimos (RSCU)
  - Índice de Adaptação de Códon (CAI)
  - Número efetivo de Códons (ENC)
  - Índice de Similaridade (SiD)

## Metodologia

- Pesquisa Quantitativa
  - Identificar a amostra
  - Definir os instrumentos de coleta de dados
  - Definir os procedimentos de análise de dados

### Amostragem

- Sequências da proteína spike do Sars-Cov-2

### Coleta e tratamento da amostra

- Modelagem do banco
  - Banco de dados MongoDB
    - Dados Armazenados:
      - Nome da Sequência
      - Nome do Organismo
      - Genoma Completo
      - País
      - Hospedeiro
      - Data de Colta da Sequência
      - Início e Fim da Proteína Spike
      - Observações

### Coleta e armazenamento das sequências

- Script TypeScript com a bib puppeteer
  - Lê arquivo CSV e Busca no GenBank a sequência pelo nome

### Amostra de dados e tratamento da amostra

- São selecionadas no máximo 10 sequências de cada país
- Criação de arquivo no formato FASTA
- Alinhamento das sequencias com o MUSCLE do software MEGA X

## Análise de Dados

- Utilizando o algoritmo PSRM
- Algoritmo foi implementado com a linguagem python
- Algoritmo recebe arquivo FASTA alinhado e editado com o MEGA X

## Resultados Parciais

### Resultados do PSRM

- Árvore filogenética gerada com o alg Maximum Likelihood

## Considerações Parciais

- PSRM conseguiu calcular a frequência dos códons, identificar os padrões e classifica-los
