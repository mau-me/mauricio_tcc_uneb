# Trabalho de Conclusão de Curso - Implementações

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
<!-- - [Contributing](../CONTRIBUTING.md) -->

## About <a name = "about"></a>

Está branch versionará todas as implementações realizadas no desenvolvimento do TCC.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

É necessário ter os seguintes programas instalados:

```
python3
ncbi-blast+
Clustal Omega
virtualenv (Opcional)
```

#### Gerando arquivo requirements.txt

```
pip freeze > requirements.txt
```

### Installing

É recomendado que a instalação dos pacotes necessários seja realizada em um ambiente virtual.

Passos iniciais para criação do ambiente virtual com o virtualenv e instalação das bibs requeridas pelo projeto:

```
virtualenv `nome_do_ambiente`
source `nome_do_ambiente`/bin/activate
pip install -r requirements.txt
```

Instalação necessárias feitas em um sistema linux(Caso estaja em outro SO, verifique como realizar a instalação no seu caso):

```
- sudo apt install ncbi-blast+
- sudo apt install clustalo
```

Após isso é possível abrir e executar os notebooks disponíveis.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
