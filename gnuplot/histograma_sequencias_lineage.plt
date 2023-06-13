set title 'Histograma Lineage'

set style data histogram
set grid
set xlabel 'Lineage'
set ylabel 'Quantidade'
set xrange [0:1200]

set bmargin 4

set terminal 'png'
set output 'lineage.png'

plot 'dados_lineage_maior_50.txt' using 2