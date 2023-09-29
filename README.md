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

```programs
python3
ncbi-blast+
Clustal Omega
Scipy
virtualenv (Opcional)
```

#### Gerando arquivo requirements.txt (Caso necessário atualizar o já existente)

```
pip freeze > requirements.txt
```

### Installing

É recomendado que a instalação dos pacotes necessários seja realizada em um ambiente virtual.

Passos iniciais para criação do ambiente virtual com o virtualenv e instalação das bibs requeridas pelo projeto:
Obs.: A criação do ambiente virtual deve ser realizado dentro da pasta do projeto.

```bash
virtualenv `nome_do_ambiente`
source `nome_do_ambiente`/bin/activate
pip install -r requirements.txt
```

Instalação necessárias feitas em um sistema linux(Caso estaja em outro SO, verifique como realizar a instalação no seu caso):

```bash
- sudo apt install ncbi-blast+
- sudo apt install clustalo
- sudo apt install python3-scipy
```

Após isso é possível abrir e executar os notebooks disponíveis.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
