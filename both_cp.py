import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNewsletterAndInvalidLogin(unittest.TestCase):

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

    def test_login_incorrecto(self):
        log = "Iniciando prueba de inicio de sesión incorrecto..."
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        boton_login = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")
        boton_login.click()

        # Introduce credenciales incorrectas
        usuario = "abc"
        contraseña = "123"

        log = f"Usuario: {usuario}, Contraseña: {contraseña}"
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        campo_usuario = self.driver.find_element(By.ID, "Email")
        campo_usuario.send_keys(usuario)

        campo_contraseña = self.driver.find_element(By.ID, "Password")
        campo_contraseña.send_keys(contraseña)

        log = "Haciendo click al botón de inicio de sesión..."
        print(f"{self.orden_log} - {log}<br>")
        self.orden_log += 1

        boton_inicio_sesion = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input")
        boton_inicio_sesion.click()

        try:
            time.sleep(3)
            elemento_error = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/span/span"))
            )

            log = "Verificando el mensaje de error..."
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1

            self.assertNotEqual(len(elemento_error.text), 0, "El mensaje de error no se muestra.")

            log = "Mensaje de error: " + elemento_error.text
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1

        except Exception as e:
            log = "No se ha podido encontrar un mensaje de error. Las credenciales son incorrectas."
            print(f"{self.orden_log} - {log}<br>")
            self.orden_log += 1
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/marcos/Documents/pruebasSoftware/Reportes'))
