#!/usr/bin/env bash

# Verifica se o diretório foi fornecido como argumento
if [ -z "$1" ]; then
  >&2 echo "Por favor, forneça o nome do diretório contendo as pastas e arquivos .fasta como argumento."
  exit 1
fi

# Obtém o nome do diretório a partir do argumento fornecido
diretorio=$1

# Verifica se o diretório existe
if [ ! -d "$diretorio" ]; then
  >&2 echo "O diretório $diretorio não existe."
  exit 1
fi

# Loop para processar cada pasta dentro do diretório
for pasta in "$diretorio"/*/; do
  echo "Processando pasta: $pasta"

  # Verifica se a pasta contém arquivos .fasta
  if [ -z "$(ls -A "$pasta"/*.fasta 2>/dev/null)" ]; then
    echo "A pasta $pasta não contém arquivos .fasta."
  else
    # Loop para processar cada arquivo .fasta na pasta
    for arquivo in "$pasta"/*.fasta; do
      echo "Processando arquivo: $arquivo"

      # Comando para executar o script Python com o arquivo atual
      python3 filtra_new.py -i "$arquivo" -o "$pasta"_unique_sequences.fasta -l "$pasta"

      # Verifica o código de saída do comando python3
      if [ $? -ne 0 ]; then
        >&2 echo "Erro ao executar o script Python para o arquivo: $arquivo"
      fi
    done
  fi
done

echo "Processamento concluído."
