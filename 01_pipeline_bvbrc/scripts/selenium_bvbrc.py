import os
import re
import sys
import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Verifica se o nome do arquivo foi fornecido como argumento
if len(sys.argv) < 2:
    print("Por favor, forneça o nome do arquivo .txt como argumento.")
    sys.exit(1)

# Obtém o nome do arquivo a partir do argumento fornecido
nome_arquivo = sys.argv[1]

# Verifica se o arquivo existe
if not os.path.isfile(nome_arquivo):
    print(f"O arquivo {nome_arquivo} não existe.")
    sys.exit(1)

# Lista para armazenar as URLs com problemas
urls_com_problemas = []

# Leitura das URLs do arquivo
with open(nome_arquivo, "r") as arquivo_origem:
    urls = arquivo_origem.readlines()

for url in urls:
    try:
        # Caminho da raiz do sistema até a pasta Downloads
        pasta_downloads = '/home/sharedFolder/dataset_sequences/sequencias_por_lineage/'

        # Obtém a parte final da URL como o nome do arquivo
        url_partes = urlparse(url)
        lineage = re.findall(r'eq[^"]*?"([^"]+)', url_partes.fragment)[-1]
        nova_pasta = pasta_downloads + lineage

        # Cria a pasta de download se ela não existir
        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)
            print(f"PASTA CRIADA EM: {nova_pasta}")

        # Configura as opções do ChromeDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": nova_pasta
        })

        driver = webdriver.Chrome(options=chrome_options)

        # Faz a requisição HTTP abrindo a página
        driver.delete_all_cookies()

        driver.get(url)

        # Espera até que o grid principal esteja completamente carregado e visível
        time.sleep(30)

        # Clica no checkbox para selecionar todas as sequências
        driver.find_element(By.XPATH, '//*[@id="dojoUnique1"]/div/input').click()

        time.sleep(1)
        # Aperta a tecla ESC para fechar o popup
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        time.sleep(5)
        # Clica no botão de download
        driver.find_element(By.XPATH, '//*[@id="uniqName_18_1"]/div[3]/div[1]').click()

        time.sleep(1)
        # Clica nos downloads DNA Fasta e CSV
        driver.find_element(By.XPATH, '//*[@id="dijit_TooltipDialog_9"]/div[1]/div/div/div/table/tr[1]/td[3]/div').click()
        driver.find_element(By.XPATH, '//*[@id="dijit_TooltipDialog_9"]/div[1]/div/div/div/table/tr[1]/td[1]/div[2]').click()

        # Verifica se ainda existem arquivos com extensão '.crdownload' no diretório de downloads
        while any(file.endswith('.crdownload') for file in os.listdir(nova_pasta)):
            time.sleep(1)
        print(f"Downloads do arquivos do genoma {lineage} finalizados...")

    except Exception as e:
        print(f"Erro ao processar a URL {url}")
        urls_com_problemas.append(url)
        with open("urls_problemas.txt", "a") as arquivo_saida:
            arquivo_saida.writelines(urls_com_problemas)



# Encerra o navegador
driver.quit()

print("Processamento concluído. Verifique o arquivo com as URLs com problemas.")
