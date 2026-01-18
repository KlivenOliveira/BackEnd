#primeiro preciso abrir o formulario

#dps fazer login autmatizado

#dps reconhecer cada campo, tvz a ordem sirva?


import time
import subprocess
import sys

def instalar_pacote(pacote):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

try:
    import pyautogui
    import pandas
except ImportError:
    instalar_pacote("pyautogui")
    instalar_pacote("pandas")
    import pyautogui
#pyautogui.click
print(pyautogui)
pyautogui.PAUSE = 0.5

largura, altura = pyautogui.size()

    

pyautogui.press('win')
pyautogui.write('google chrome')
pyautogui.press('enter')

time.sleep(3)

# Abrir aba anônima (zera localStorage automaticamente)
pyautogui.hotkey('ctrl', 'shift', 'n')

time.sleep(1)

# Abrir o site
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)


pyautogui.press('tab')
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
time.sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')


tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.press('tab')



    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

   
    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

  
    obs = str(tabela.loc[linha,'obs'])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
  
    time.sleep(1.5)
    for _ in range(8):
     pyautogui.hotkey('tab')

    pyautogui.scroll(5000)
                       