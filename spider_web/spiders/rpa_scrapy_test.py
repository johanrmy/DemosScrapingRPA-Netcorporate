import scrapy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from ..vars import *

class RpaScrapyTestSpider(scrapy.Spider):
    name = "rpa_scrapy_test"
    allowed_domains = ["pywombat.com"]
    start_urls = ["https://pywombat.com/login/"]

    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()), options=options)

    def parse(self, response):
        try:
            if response.status == 200:
                # Utilizar el controlador de Selenium para iniciar sesión
                self.login()

                # Obtener las cookies del controlador de Selenium después de iniciar sesión
                cookies = self.driver.get_cookies()

                # Convertir las cookies en un diccionario para usar en Scrapy
                cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
                yield scrapy.Request(url='https://pywombat.com/my/exercises/', cookies=cookies_dict,
                                     callback=self.get_auth_data)
            else:
                self.logger.warning(f'La página no está disponible. Status: {response.status}')
        except Exception as e:
            self.driver.quit()
            self.logger.error("Error en la solicitud : %s", str(e))

    def login(self):
        try:
            self.driver.get('https://pywombat.com/login/')
            self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
            self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
            self.driver.find_element(By.CLASS_NAME, "cursor-pointer").click()
        except Exception as e:
            self.driver.quit()
            self.logger.error("Error en la función login: %s", str(e))

    def get_auth_data(self, response):
        try:
            # definir tiempo de carga a la página
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, '//td/div/a/p[@class="font-lg"]')))

            table = self.driver.find_element(By.CLASS_NAME, "table-auto")
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            num_rows = len(rows)
            data = []
            # extraer datos
            for x in range(num_rows):
                nombre = rows[x].find_element(By.XPATH, './td[1]/div/a/p').text
                nivel = rows[x].find_element(By.XPATH, './td[2]/p').text
                fecha = rows[x].find_element(By.XPATH, './td[3]/p').text
                rows[x].find_element(By.XPATH, './td/div/a').click()
                time.sleep(600/1000)
                solucion = self.driver.find_element(By.TAG_NAME, "textarea").text
                self.driver.back()
                info = {'nombre': nombre, 'nivel': nivel, 'fecha': fecha, 'solucion': solucion}
                data.append(info)
            self.driver.quit()
            return data
        except Exception as e:
            self.driver.quit()
            self.logger.error("Error en la función get_auth_data: %s", str(e))
