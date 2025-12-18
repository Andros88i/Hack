from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tus credenciales se quedan aquí, de forma local en tu Termux
EMAIL = "androsgil527@gmail.com"
PASS = "rocaknrrolla1988"

def iniciar_sesion():
    options = webdriver.ChromeOptions()
    # Importante: para que no consuma tantos recursos en Termux
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        print("Accediendo a TeraBox...")
        driver.get("https://www.terabox.com/main?category=all")
        
        wait = WebDriverWait(driver, 15)

        # 1. Esperar a que cargue el campo de email
        # TeraBox usa selectores que a veces cambian, usamos el atributo 'placeholder'
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username/Email/Phone/Account ID']")))
        email_field.send_keys(EMAIL)
        print("Email ingresado...")

        # 2. Ingresar contraseña
        pass_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        pass_field.send_keys(PASS)
        print("Contraseña ingresada...")

        # 3. Click en el botón de entrar
        # Buscamos el botón que tiene el texto de Login
        login_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'login-button')]")
        login_btn.click()
        
        print("Botón presionado. Esperando carga de archivos...")
        
        # Le damos tiempo para que cargue la interfaz principal
        time.sleep(10)
        
        if "main" in driver.current_url:
            print("¡Login exitoso! Ya estás dentro de tus archivos.")
        else:
            print("Es posible que haya aparecido un CAPTCHA visual.")

    except Exception as e:
        print(f"Error: {e}")
    
    return driver

if __name__ == "__main__":
    driver_activo = iniciar_sesion()
    # Mantenemos el driver abierto para que puedas ver o trabajar
    # Si cierras el script, se cierra el navegador.
