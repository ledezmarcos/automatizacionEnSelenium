import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNewsletterSubscription(unittest.TestCase):

    def setUp(self):
        self.orden_log = 1
        self.driver = webdriver.Chrome()
        self.driver.get("https://demowebshop.tricentis.com")

    def test_newsletter_subscription(self):
        log = "Cargando página..."
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        correo_electronico = "test@example.com"

        log = f"Email ingresado: {correo_electronico}"
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        campo_busqueda = self.driver.find_element(By.ID, "newsletter-email")
        campo_busqueda.send_keys(correo_electronico)

        log = "Haciendo click al botón de suscribir..."
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        boton_suscripcion = self.driver.find_element(By.ID, "newsletter-subscribe-button")
        boton_suscripcion.click()

        try:
            time.sleep(3)
            elemento_confirmacion = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "newsletter-result-block"))
            )
            
            log = "Verificando el mensaje de confirmación..."
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1

            self.assertNotEqual(len(elemento_confirmacion.text), 0, "El email ingresado es inválido.")

            log = "Mensaje de confirmación: " + elemento_confirmacion.text
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1

        except Exception as e:
            log = "No se ha podido encontrar un mensaje de confirmación. Por favor verifica que el email es válido."
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/marcos/Documents/pruebasSoftware/Reportes'))

