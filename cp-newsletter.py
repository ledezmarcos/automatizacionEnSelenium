import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador del navegador
driver = webdriver.Chrome()

# Abrir el sitio web de demowebshop
driver.get("https://demowebshop.tricentis.com")

# Solicitar al usuario que ingrese su correo electrónico
correo_electronico = input("Por favor ingrese su correo electrónico: ")

# Encontrar el campo de búsqueda e ingresar el correo electrónico del usuario
campo_busqueda = driver.find_element("id", "newsletter-email")
campo_busqueda.send_keys(correo_electronico)

# Encontrar el botón de suscripción y hacer clic en él
boton_suscripcion = driver.find_element("id", "newsletter-subscribe-button")
boton_suscripcion.click()

# Esperar a que la página cargue completamente
time.sleep(3)

# Esperar a que aparezca el elemento de confirmación o la excepción
try:
    elemento_confirmacion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newsletter-result-block"))
    )
    # Verificar si el elemento de confirmación está vacío
    if len(elemento_confirmacion.text) == 0:
        print("El correo electrónico ingresado es inválido.")
    else:
        # Imprimir el mensaje de confirmación
        print(elemento_confirmacion.text)
except:
    # Manejar la excepción TimeoutException
    print("No se pudo encontrar el elemento de confirmación. Verifica que el correo electrónico sea válido.")
finally:
    # Esperar a que el usuario presione Enter antes de cerrar el navegador
    input("Presiona Enter para cerrar el navegador...")
    # Cerrar el navegador al final
    driver.quit()