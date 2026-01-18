from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("file:///C:/backend/testes.html")

wait = WebDriverWait(driver, 10)

# input
texto = wait.until(EC.presence_of_element_located((By.ID, "testeTexto")))
texto.send_keys("FUI PREENCHIDO SOZINHO")

texto2 = wait.until(EC.presence_of_element_located((By.ID, "testeTexto2")))
texto2.send_keys("FUI PREENCHIDO SOZINHO2")

texto3 = wait.until(EC.presence_of_element_located((By.ID, "testeTexto3")))
texto3.send_keys("FUI PREENCHIDO SOZINHO3")

texto4 = wait.until(EC.presence_of_element_located((By.ID, "testeTexto4")))
texto4.send_keys("FUI PREENCHIDO SOZINHO4")


# selects
Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect2")))).select_by_value("1")
Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect")))).select_by_value("2")

Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect3")))).select_by_value("3")

# checkbox
checkbox = wait.until(EC.element_to_be_clickable((By.ID, "testeCHK1")))
if not checkbox.is_selected():
    checkbox.click()

checkbox2 = wait.until(EC.element_to_be_clickable((By.ID, "testeCHK2")))
if not checkbox2.is_selected():
    checkbox2.click()

# radio (escolhendo o radio2)
radio = wait.until(EC.element_to_be_clickable((By.ID, "radio2")))
radio.click()

radio2 = wait.until(EC.element_to_be_clickable((By.ID, "radio3")))
radio2.click()


btn_zoom = wait.until(
    EC.presence_of_element_located((By.ID, "btnZoomProduto"))
)

driver.execute_script("arguments[0].click();", btn_zoom)

# 2️⃣ Esperar o modal aparecer
wait.until(
    EC.visibility_of_element_located((By.ID, "modalZoom"))
)

# 3️⃣ Clicar no produto desejado (ex: P002)
linha_produto = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//tr[@data-cod='P002']"
    ))
)
linha_produto.click()

# 4️⃣ Validar se o campo foi preenchido
zoom_input = wait.until(
    EC.presence_of_element_located((By.ID, "zoomProduto"))
)

valor = zoom_input.get_attribute("value")
print("Valor do zoom:", valor)

assert "P002" in valor



time.sleep(1)
btn = wait.until(EC.element_to_be_clickable((By.ID, "btnTeste")))
btn.click()


input("ENTER para fechar...")
driver.quit()
