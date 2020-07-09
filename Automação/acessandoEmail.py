from selenium import webdriver #Importa o webdriver da biblioteca selenium
from selenium.webdriver.common.keys import Keys
import time #Importa a iblioteca time

# Atribuição de Variaveis
email = "lucasdutrabraz@hotmail.com"
senha = "1L2u3c4a5s"

destinatario = "lucasdutrabraz@gmail.com"
assunto = "Robozão"
mensagem = "FAAAALAAAAAAA! Aqui é o jarvizinho."

driver = webdriver.Chrome("C:/Users/Batman/Desktop/Robos/chromedriver")

print("Iniciando nosso robô...\n")
print("Acessando o E-mail...\n")
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1577374220&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3daa57a245-477d-79b2-a551-c56ef790d8cb&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&uaid=9cee1c622fa6445f8481783ad20fa4ab&pid=0&contextid=64D5FCDB32E4EB18&bk=1577374251&aup=1&lc=1046")

#LOGIN
print("Realizando login...\n")
login = driver.find_element_by_id("i0116")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element_by_name("passwd")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login realizado...\n")

time.sleep(6)
print("Abrindo caixa de email...\n")
button = driver.find_element_by_id("id__3")
button.click()
time.sleep(6)

print("Escrevendo o email...\n")
receptor = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input")
receptor.send_keys(destinatario)

time.sleep(2)

titulo = driver.find_element_by_id("subjectLine0")
titulo.send_keys(assunto)

time.sleep(2)

texto = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]")
texto.send_keys(mensagem)

print("Enviando o email...\n")
time.sleep(2)

enviar = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/button[1]/span")
enviar.click()

time.sleep(2)

print("Email enviado!!!\n")

driver.close()

