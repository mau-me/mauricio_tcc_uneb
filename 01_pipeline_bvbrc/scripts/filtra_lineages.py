# Abrir o arquivo de origem
with open("../dados_lineage.txt", "r") as arquivo_origem:
    linhas = arquivo_origem.readlines()

# Filtrar as linhas que contêm o padrão e copiar a primeira coluna
coluna_filtrada = []

for linha in linhas:
    colunas = linha.strip().split(" ")
    if (int(colunas[1]) > 50):
        coluna_filtrada.append(" ".join(colunas))

# Salvar as colunas filtradas em um novo arquivo
with open("dados_lineage_maior_50.txt", "w") as arquivo_filtrado:
    arquivo_filtrado.write('\n'.join(coluna_filtrada))
