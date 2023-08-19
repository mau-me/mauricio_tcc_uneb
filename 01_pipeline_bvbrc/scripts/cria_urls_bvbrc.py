# Abrir o arquivo de origem
with open("dados_lineage_filtrados_menor_10k.txt", "r") as arquivo_origem:
    linhas = arquivo_origem.readlines()

urlBase = 'https://www.bv-brc.org/view/Taxonomy/2697049#view_tab=genomes&filter=and(eq(genome_status,"Complete"),or('
urlFinal = urlBase
lineageString = 'eq(lineage,'
lineageFinal = ''

urlsProntas = []
total = 0

# and(eq(genome_status,"Complete"),or(eq(lineage,"A.23.1"),eq(lineage,"A.2.2"),eq(lineage,"A.1"),eq(lineage,"A"),eq(lineage,"AY.100")))

for linha in linhas:
    colunas = linha.strip().split(" ")
    if((total + int(colunas[1])) < 10000):
        total += int(colunas[1])
        lineageFinal += ',' + lineageString + '"' + colunas[0] + '")'
    else:
        urlFinal = (urlBase + lineageFinal + '))')
        urlsProntas.append(urlFinal)
        lineageFinal = ''
        urlFinal = urlBase
        total = 0

# Salvar as colunas filtradas em um novo arquivo
with open("urlsDownloads_02.txt", "w") as arquivo_filtrado:
    arquivo_filtrado.write('\n'.join(urlsProntas))
