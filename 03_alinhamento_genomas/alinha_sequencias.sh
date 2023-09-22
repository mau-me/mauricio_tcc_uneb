#!/bin/bash

# Obter a data da execução
data_execucao=$(date +"%Y-%m-%d %H:%M:%S")

# Obter informações do sistema usando neofetch e redirecionar a saída para uma variável
info_sistema=$(neofetch)

# Extrair informações específicas do neofetch (por exemplo, Nome do Host)
nome_host=$(echo "$info_sistema" | grep "Host" | awk -F ':' '{print $2}' | sed 's/^[[:space:]]*//')

# Extrair informações específicas do neofetch (por exemplo, Sistema Operacional)
sistema_operacional=$(echo "$info_sistema" | grep "OS" | awk -F ':' '{print $2}' | sed 's/^[[:space:]]*//')

# Extrair informações específicas do neofetch (por exemplo, Informações do Processador)
processador_info=$(echo "$info_sistema" | grep "CPU" | awk -F ':' '{print $2}' | sed 's/^[[:space:]]*//')

# Obter quantidade de memória (RAM)
memoria_info=$(free -h | awk '/^Mem/{print "Total de Memória: " $2}')

# Tempo de início do script
start_time=$(date +%s)

# Inicializa a variável de contagem de sequências
sequencias_processadas=0

# Diretório principal que contém as pastas com os arquivos _unique_sequences.fasta
diretorio_principal="/home/maume/UnEB/TCC/Dataset/sequencias_por_lineage"
referencia="/home/maume/UnEB/TCC/Dataset/genome_reference.fasta"

# Itera sobre todas as pastas dentro do diretório principal
for pasta in "$diretorio_principal"/*/; do
    # Verifica se a pasta contém o arquivo _unique_sequences.fasta
    if [ -e "$pasta"_unique_sequences.fasta ]; then
        # Define o caminho completo para o arquivo de sequência
        sequencia="$pasta"_unique_sequences.fasta

        # Define o caminho completo para o arquivo de saída .sam
        arquivo_sam="$pasta"mysam.sam

        # Executa o primeiro comando para gerar o arquivo .sam e redireciona a saída para /dev/null
        minimap2 -a -x asm5 --cs --sam-hit-only --secondary=no -t 10 "$referencia" "$sequencia" -o "$arquivo_sam" > /dev/null 2>&1

        # Verifica se o arquivo .sam foi gerado com sucesso
        if [ -e "$arquivo_sam" ]; then
            # Define o caminho completo para o arquivo de saída sequencias_alinhadas.fasta
            arquivo_alinhado="$pasta"sequencias_alinhadas.fasta

            # Executa o segundo comando para gerar o arquivo sequencias_alinhadas.fasta e redireciona a saída para /dev/null
            gofasta sam toMultiAlign -s "$arquivo_sam" -t 10 --reference "$referencia" > "$arquivo_alinhado" 2> /dev/null

            # Verifica se o arquivo sequencias_alinhadas.fasta foi gerado com sucesso
            if [ -e "$arquivo_alinhado" ]; then
                # echo "Processamento da pasta $pasta concluído com sucesso."
                # Aumenta a contagem de sequências processadas
                ((sequencias_processadas++))
            else
                echo "Erro ao gerar o arquivo sequencias_alinhadas.fasta na pasta $pasta."
            fi
        else
            echo "Erro ao gerar o arquivo .sam na pasta $pasta."
        fi
    else
        echo "Pasta $pasta não contém o arquivo _unique_sequences.fasta."
    fi
done

# Tempo de término do script
end_time=$(date +%s)

# Calcula o tempo total de execução do script em segundos
elapsed_time=$((end_time - start_time))

# Exibe informações adicionais
echo "Data da execução: $data_execucao"
echo "Nome do host: $nome_host"
echo "Sistema Operacional: $sistema_operacional"
echo "Informações do Processador:$processador_info"
echo "$memoria_info"

# Exibe o número total de sequências processadas
echo "Número total de sequências processadas: $sequencias_processadas"

# Exibe o tempo total de execução
echo "Tempo total de execução do script: $elapsed_time segundos"
