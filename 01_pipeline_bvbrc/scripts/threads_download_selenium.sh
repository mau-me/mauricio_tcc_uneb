#!/bin/bash

# Verifica se o diretório foi fornecido como argumento
if [ $# -eq 0 ]; then
  echo "Por favor, forneça o nome do diretório contendo os arquivos .txt como argumento."
  exit 1
fi

# Obtém o nome do diretório a partir do argumento fornecido
diretorio=$1

# Verifica se o diretório existe
if [ ! -d "$diretorio" ]; then
  echo "O diretório $diretorio não existe."
  exit 1
fi

# Loop para processar cada arquivo .txt no diretório
for arquivo in "$diretorio"/*.txt; do
  echo "Processando arquivo: $arquivo"

  # Comando para executar o script Python com o arquivo atual
  python3 downloadSelenium.py "$arquivo"
done

echo "Processamento concluído."