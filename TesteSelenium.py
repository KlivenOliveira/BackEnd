import os
import sys
import subprocess
import time

def garantir_selenium():
    try:
        import selenium
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])

garantir_selenium()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

arquivo = os.path.abspath("testes.html")

driver = webdriver.Chrome()
driver.get(f"file:///{arquivo}")

wait = WebDriverWait(driver, 10)

# inputs
wait.until(EC.presence_of_element_located((By.ID, "testeTexto"))).send_keys("FUI PREENCHIDO SOZINHO")
wait.until(EC.presence_of_element_located((By.ID, "testeTexto2"))).send_keys("FUI PREENCHIDO SOZINHO2")
wait.until(EC.presence_of_element_located((By.ID, "testeTexto3"))).send_keys("FUI PREENCHIDO SOZINHO3")
wait.until(EC.presence_of_element_located((By.ID, "testeTexto4"))).send_keys("FUI PREENCHIDO SOZINHO4")

# selects
Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect2")))).select_by_value("1")
Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect")))).select_by_value("2")
Select(wait.until(EC.presence_of_element_located((By.ID, "testeSelect3")))).select_by_value("3")

# checkboxes
for chk_id in ["testeCHK1", "testeCHK2"]:
    chk = wait.until(EC.element_to_be_clickable((By.ID, chk_id)))
    if not chk.is_selected():
        chk.click()

# radios
wait.until(EC.element_to_be_clickable((By.ID, "radio2"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "radio3"))).click()

# zoom
btn_zoom = wait.until(EC.element_to_be_clickable((By.ID, "btnZoomProduto")))
driver.execute_script("arguments[0].click();", btn_zoom)

wait.until(EC.visibility_of_element_located((By.ID, "modalZoom")))

linha_produto = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//tr[@data-cod='P002']"))
)
linha_produto.click()

zoom_input = wait.until(EC.presence_of_element_located((By.ID, "zoomProduto")))
valor = zoom_input.get_attribute("value")
print("Valor do zoom:", valor)
assert "P002" in valor

wait.until(EC.element_to_be_clickable((By.ID, "btnTeste"))).click()

input("ENTER para fechar...")
driver.quit()
