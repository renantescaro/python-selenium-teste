import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BuscaLojaTray:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://www.kidy.com.br/")


    def buscar(self):
        time.sleep(2)
        el_busca = self._driver.find_element_by_id('ico-busca-topo')
        el_busca.click()

        time.sleep(2)
        el_input = self._driver.find_element_by_id('txtBuscaMobile')
        el_input.send_keys("botas")
        el_input.send_keys(Keys.RETURN)

        time.sleep(2)
        el_spot = self._driver.find_element_by_class_name('spot')
        el_spot.click()

        time.sleep(2)
        el_grupo_tamanhos = self._driver.find_element_by_class_name('valorAtributo')
        el_grupo_tamanhos.click()

        time.sleep(2)
        el_comprar = self._driver.find_element_by_class_name('produto-comprar')
        el_comprar.click()


BuscaLojaTray().buscar()
# assert "No results found." not in driver.page_source
# driver.close()