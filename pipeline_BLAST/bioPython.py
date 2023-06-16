from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
from Bio import SeqIO
import tempfile
import os
from io import StringIO

fname = "/home/m_souza/Desktop/BVBRC_genome_sequence.fasta"

multiple_genomes = []
with open(fname) as handle:
    for values in SeqIO.FastaIO.SimpleFastaParser(handle):
        multiple_genomes.append(values)

Nseq = len(multiple_genomes)
print("number of sequences in file ", fname, " = ", Nseq)

def buscar_posicao_gene(sequencia_gene, genoma):
    # Executar o BLAST para buscar a posição do gene no genoma
    comando_blast = NcbiblastnCommandline(query=sequencia_gene, subject=genoma, outfmt=5)
    stdout, stderr = comando_blast()

    # Analisar o resultado XML do BLAST
    resultado_blast = NCBIXML.read(StringIO(stdout))
    if len(resultado_blast.alignments) == 0:
        print('O gene não foi encontrado no genoma.')
        return

    alinhamento = resultado_blast.alignments[0]
    hsp = alinhamento.hsps[0]

    posicao_inicio = hsp.sbjct_start
    posicao_fim = hsp.sbjct_end

    print(f'O gene foi encontrado na posição {posicao_inicio}-{posicao_fim}.')

# Sequência do gene
sequencia_gene = '/home/m_souza/Desktop/refSpike.fasta'

# Caminho para o arquivo do genoma
genoma = '/home/m_souza/Desktop/_unique_sequences.fasta'

# Chamar a função para buscar a posição do gene
buscar_posicao_gene(sequencia_gene, genoma)

# Obter a sequência de DNA do genoma
genoma_seq = multiple_genomes[0][1]

# Criar um arquivo temporário para armazenar a sequência de DNA
temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
temp_file.write(f">{multiple_genomes[0][0]}\n{genoma_seq}")

# Caminho para o arquivo temporário do genoma
genoma_temp_file = temp_file.name

# Chamar a função para buscar a posição do gene
buscar_posicao_gene(sequencia_gene, genoma_temp_file)

# Remover o arquivo temporário
os.remove(genoma_temp_file)

temp_file.close()

print("Busca concluída.")
