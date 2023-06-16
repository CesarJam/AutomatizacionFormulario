from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random




a = 1
while a < 100:
    driver = webdriver.Chrome()
    driver.get("https://forms.gle/5nFq1kpQb65MRDQKA")
    print(driver.title)
    driver.maximize_window()
    time.sleep(1)



    #pregunta 1
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div'

    radiobutton1 = driver.find_element('xpath',res)
    radiobutton1.click()

    #pregunta 2
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div'

    radiobutton2 = driver.find_element('xpath',res)
    radiobutton2.click()


    #pregunta 3
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton3 = driver.find_element('xpath',res)
    radiobutton3.click()


    #pregunta 4
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton4 = driver.find_element('xpath',res)
    radiobutton4.click()

    #pregunta 5
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton5 = driver.find_element('xpath',res)
    radiobutton5.click()

    #pregunta 6
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton6 = driver.find_element('xpath',res)
    radiobutton6.click()

    #pregunta 7
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton7 = driver.find_element('xpath',res)
    radiobutton7.click()

    #pregunta 8

    respuestaAleatoria = random.randint(0, 3)
    print(respuestaAleatoria)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label'
    if respuestaAleatoria == 1:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label'
    if respuestaAleatoria == 2:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label'   
    if respuestaAleatoria == 3:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label'

    radiobutton8 = driver.find_element('xpath',res)
    radiobutton8.click()

    #pregunta 9
    respuestaAleatoria = random.randint(0, 1)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label'
    else:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label'

    radiobutton9 = driver.find_element('xpath',res)
    radiobutton9.click()

    #pregunta 10
    respuestaAleatoria = random.randint(0, 5)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label'
    if respuestaAleatoria == 1:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label'
    if respuestaAleatoria == 2:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label'
    if respuestaAleatoria == 3:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[4]/label'
    if respuestaAleatoria == 4:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[5]/label'
    if respuestaAleatoria == 5:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[6]/label'

    radiobutton10 = driver.find_element('xpath',res)
    radiobutton10.click()

    #pregunta 11
    respuestaAleatoria = random.randint(0, 3)
    if respuestaAleatoria == 0:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label'
    if respuestaAleatoria == 1:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[2]/label'
    if respuestaAleatoria == 2:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[3]/label'
    if respuestaAleatoria == 3:
        res='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[4]/label'

    radiobutton11 = driver.find_element('xpath',res)
    radiobutton11.click()

    #text = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')
    #text.send_keys('mejor atencion y rapido cobro')

    submitbutton = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submitbutton.click()
    a =a+1
    time.sleep(1)
    driver.close()