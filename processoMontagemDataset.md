## Passo a passo da montagem do dataset das sequências de genomas baixadas do site BV_BRC

1. Inicialmente foi verificado que o site possuía a opção de download de genomas com a seleção por vários filtros.
2. Para o download de várias sequências por vez, o site possuía uma limitação de 10k/download
3. Como era necessário realizar o download de todas as sequências do site, o processo manual se tornou inviável
4. Foi verificado que o site BV-BRC possuía um servidor FTP, e que o recomendava que grandes downloads fossem realizados através deste meio. Após a criação de scripts para download das pelo FTP, foi verificado que as sequências de SARS-COV-2 não puderam eram encontradas através do seu ID no servidor FTP. Foi realizada a tentativa de contato com a BV-BRC para entender o por quê do problema, mas a tentativa foi sem sucesso.
5. Para realizar o download das sequências foram realizadas as tentativas a seguir:
   1. Criação de um script em python para criar urls do site BV-BRC com o máximo de filtros selecionados até o limite de 10k sequências.
      1. Realizada a abertura das urls(por volta de 70) manualmente no navegador para realização do processo de download. OBS: Os downloads foram concluídos com sucesso, mas após conversa com o orientador se viu necessário realizar o download das sequências agrupadas em um único tipo/lineage. Assim o processo realizado foi descartado.
   2. Criação de um script em python para realizar o download de forma automatizada com o framework Selenium, uma ferramenta de testes de aplicativos web.
      1. Após várias versões do script a versão final e funcional contou com as seguintes características:
         1. O script é executado recebendo como parâmetro de execução um arquivo contendo as urls com os filtros a serem baixadas (É possível utilizar o primeiro script de criação de urls para criar as urls individuais para cada lineage de SARS-COV-2)
         2. Como o número de urls foi consideravelmente grande(por volta de 1100 urls), foram criados dois outros scripts:
            1. Um script em python para separar as urls em vários arquivos com a mesma quantidade de urls/arquivo
            2. Um script em bash para executar o script de download automatizado das urls de todos os arquivos txt encontrados em determinada pasta
         3. Esse processo foi realizado para facilitar e agilizar o download da grande quantidade de sequências. Foram criadas pastas que continham x arquivos .txt. Então foi fácil rodar o script simultaneamente apontando cada execução para uma pasta específica.
6. O script de download automatizado das sequências cria um arquivo nomeado como urls.problemas.txt, onde são salvas todas as urls em que o download não obteve exito. Dessa forma o script poderia ser executado posteriormente apontando para esse arquivo e baixando somente as sequências restantes.
7. É possível informar o caminho onde os downloads serão executados. Cada lineage será baixado em uma pasta com o seu nome para identificação. Dentro da pasta existirá dois arquivos: um arquivo .fasta que contém todas as sequências de nucleotídeos e um arquivo .csv que contém todos as informações disponíveis em relação a cada sequência
8. OBSs:
   1. Se a página fechar antes do download finalizar é necessário excluir os arquivos com .crdownload no final do seu nome, pois o mesmo é utilizado como checagem para manter a página criada pelo selenium aberta.
   2. Se for reiniciar o processo séria interessante limpar tanto a pasta onde serão realizados os downloads como o arquivo urls_problemas.txt
   3. Para download só foram selecionados os lineages com no mínimo 50 sequências