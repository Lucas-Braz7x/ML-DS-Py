from selenium import webdriver #Necessário para abir o navegador e controlar ele
from selenium.webdriver.common.keys import Keys #Para controlar teclas
import time
import xlrd #Para acessar e ler arquivos

print("Iniciando o processo... \n")
arq = open("resultados.txt", 'w') # Cria um txt e diz que é possível editar

dominios = []

#Leia do excel
workbook = xlrd.open_workbook("dominio.xlsx")# Acessa a planilha do excel
sheet = workbook.sheet_by_index(0) # Acessa a planilha 1 do arquivo

for linha in range(0,10): #Range estancia os valores da linha
    for coluna in range(0,2):
        print(sheet.cell_value(linha,coluna))
        dominios.append(sheet.cell_value(linha,coluna))

driver = webdriver.Chrome("C:/Users/Batman/Desktop/Robos/chromedriver") #Determina o navegador
driver.get("https://registro.br/")#Determina o Site

for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")  # Reconhece a barra de pesquisa pelo id
    pesquisa.clear()  # Limpa a barra de pesquisa
    pesquisa.send_keys(dominio) #Elemento a ser pesquisados
    pesquisa.send_keys(Keys.RETURN) #Aperta a tecla enter
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong") #Enconra os elementos em negrito
    #print("Domínio %s %s" %(dominio, resultados[4].text) )
    texto = "Domínio %s %s\n" %(dominio, resultados[4].text) #Recebe os resultados da pesquisa
    arq.write(texto) #Escreve no documento

#import pdb; pdb.set_trace() #Pausa o programa para possibilar a interação

arq.close()
time.sleep(5) #Dormir x segundos
driver.close() #Fecha o site