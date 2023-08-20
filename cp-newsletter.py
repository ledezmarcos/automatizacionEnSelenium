from selenium import webdriver

# Inicializar el controlador del navegador
driver = webdriver.Chrome()

# Abrir el sitio web de demowebshop
driver.get("https://demowebshop.tricentis.com")

# Encontrar el campo de búsqueda e ingresar "Hola Mundo"
campo_busqueda = driver.find_element("id", "newsletter-email")
campo_busqueda.send_keys("marcos@marandu.net")

# Encontrar el botón de suscripción y hacer clic en él
boton_suscripcion = driver.find_element("id", "newsletter-subscribe-button")
boton_suscripcion.click()

input("Presiona Enter para cerrar el navegador...")
# Cerrar el navegador al final
driver.quit()
