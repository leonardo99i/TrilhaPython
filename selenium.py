import selenium
from selenium import webdriver

driver = webdriver.Chrome() #Isso vai iniciar o navegador Chrome
driver.get('https://www.python.org/') #Isso ira acessar a URL especifica
driver.find_element_by_css_selector('#id-search-field').send_keys("python") #Digita o texto "python" no input
driver.find_element_by_css_selector('#submit').click() #Clica no botão submit
driver.quit() #Isso ir