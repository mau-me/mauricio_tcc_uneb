import os

def split_file(input_file, lines_per_file):
    with open(input_file, 'r') as file:
        # Leitura de todas as linhas do arquivo
        lines = file.readlines()

        # Cálculo do número total de arquivos a serem gerados
        num_files = len(lines) // lines_per_file

        # Criação dos arquivos com as linhas correspondentes
        for i in range(num_files):
            output_file = f"output/output_{i + 1:02}.txt"  # Utiliza :02 para formatar o número com duas casas decimais
            start_index = i * lines_per_file
            end_index = start_index + lines_per_file

            with open(output_file, 'w') as output:
                output.writelines(lines[start_index:end_index])

            print(f"Arquivo {output_file} criado com sucesso.")

        # Verificação se há linhas restantes para criar o último arquivo
        if len(lines) % lines_per_file != 0:
            output_file = f"output/output_{num_files + 1:02}.txt"  # Utiliza :02 para formatar o número com duas casas decimais
            start_index = num_files * lines_per_file

            with open(output_file, 'w') as output:
                output.writelines(lines[start_index:])

            print(f"Arquivo {output_file} criado com sucesso.")

    print("Processamento concluído.")

# Nome do arquivo de entrada
input_file = "input.txt"

# Número de linhas por arquivo
lines_per_file = 10

# Chamada da função para dividir o arquivo
split_file(input_file, lines_per_file)