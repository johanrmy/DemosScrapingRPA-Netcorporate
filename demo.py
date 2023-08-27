from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class RpaSeleniumTest:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()), options=options)

    def login(self, username, password):
        try:
            self.driver.get('https://pywombat.com/login/')
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.CLASS_NAME, "cursor-pointer").click()
        except Exception as e:
            self.driver.quit()
            print("Error in the login function:", str(e))

    def get_auth_data(self):
        try:
            self.driver.get('https://pywombat.com/my/exercises/')
            # Wait for the page to load
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//td/div/a/p[@class="font-lg"]')))

            table = self.driver.find_element(By.CLASS_NAME, "table-auto")
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            num_rows = len(rows)
            data = []
            # Extract data
            for x in range(num_rows):
                nombre = rows[x].find_element(By.XPATH, './td[1]/div/a/p').text
                nivel = rows[x].find_element(By.XPATH, './td[2]/p').text
                fecha = rows[x].find_element(By.XPATH, './td[3]/p').text
                rows[x].find_element(By.XPATH, './td/div/a').click()
                time.sleep(0.6)

                solucion = self.driver.find_element(By.TAG_NAME, "textarea").text
                self.driver.back()
                info = {'nombre': nombre, 'nivel': nivel, 'fecha': fecha, 'solucion': solucion}
                data.append(info)

            return data
        except Exception as e:
            print("Error in the get_auth_data function:", str(e))
        finally:
            self.driver.quit()

if __name__ == "__main__":
    # Replace USERNAME and PASSWORD with your actual login credentials
    USERNAME = "johanem"
    PASSWORD = "soccer30py"

    rpa_test = RpaSeleniumTest()
    rpa_test.login(USERNAME, PASSWORD)
    data = rpa_test.get_auth_data()
    print(data)
