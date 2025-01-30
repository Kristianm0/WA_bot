#Importamos 
# webdriver para automatizar chrome
from selenium import webdriver
#Services controla el servicio de ChromeDriver
from selenium.webdriver.chrome.service import Service
# Option abre el navegador o ejecuta una accion dentro de el mismo
from selenium.webdriver.chrome.options import Options
#By controla elementos dentro de una pagina
from selenium.webdriver.common.by import By
#Para esperar que la pagina carge
from selenium.webdriver.support.ui import WebDriverWait
#Verifica si esta o no un elemento
from selenium.webdriver.support import expected_conditions as EC
#Manejo de errores
from selenium.common.exceptions import TimeoutException
#Administra automaticamente el ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
#Tiempo
import time
#Convierte datos en URL
import urllib.parse
import random

#Funcion para configurar chrome
def setup_driver():
    """Configurar el driver de Chrome con opciones optimizadas"""
    #Objero para configuraciones del navegador
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1100,700")
    chrome_options.add_argument("--disable-notifications")
    
    #Descarga la version correcta de ChromeDriver
    service = Service(ChromeDriverManager().install())
    #Devuelde un objeto
    return webdriver.Chrome(service=service, options=chrome_options)

#Formato al numero
def format_number(phone):
    """Asegura que el número tenga el formato correcto"""
    # Eliminar espacios y caracteres no numéricos
    phone = ''.join(filter(str.isdigit, phone))
    
    # Si no empieza con +57 y tiene 10 dígitos, agregar +57
    if len(phone) == 10 and not phone.startswith('57'):
        phone = '57' + phone
    # Si no empieza con +, agregar +
    if not phone.startswith('+'):
        phone = '+' + phone
    
    return phone

#Envia el mensaje de whatsapp
def send_whatsapp_message(driver, phone, message):
    try:
        # Codificar el mensaje para la URL
        encoded_message = urllib.parse.quote(message)
        
        # Abrir el chat
        url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"
        print(f"Abriendo chat para: {phone}")
        driver.get(url)
        
        # Esperar más tiempo para que cargue
        wait = WebDriverWait(driver, 60)
        
        # Nuevo selector específico para el SVG del botón de enviar
        svg_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-icon='send']"))
        )
        
        # Obtener el elemento padre que es el botón clickeable
        send_button = svg_button.find_element(By.XPATH, ".//..")
        
        print("Esperando 3 segundos...")
        time.sleep(random.randint(5, 15))
        
        print("Intentando enviar mensaje...")
        driver.execute_script("arguments[0].click();", send_button)
        
        print("Esperando confirmación...")
        time.sleep(3)
        
        return True, "Mensaje enviado exitosamente"
    
    except Exception as e:
        print(f"Error detallado: {str(e)}")
        print(f"Tipo de error: {type(e).__name__}")
        return False, f"Error al enviar: {str(e)}"

#Numeros de contactos, mensaje
def main():
    # Lista de contactos
    contactos = ["3207414792", "3243747129"]
    mensaje = "¿Mensaje Automatico 3?"
    
    print("🥷 Iniciando el programa...")
    driver = setup_driver()
    
    try:
        print("Abriendo WhatsApp Web...🟢")
        driver.get("https://web.whatsapp.com/")
        
        print("\nPor favor, sigue estos pasos:")
        print("1. Espera a que aparezca el código QR")
        print("2. Escanea el código con tu WhatsApp")
        print("3. Espera a que WhatsApp Web cargue completamente")
        input("4. Presiona Enter cuando estés listo...")
        
        # Procesar cada contacto
        for i, contacto in enumerate(contactos, 1):
            contacto_formateado = format_number(contacto)
            #Numero de oferta
            mensaje = f"Titulo oferta de Kimba {i}"
            print(f"\nProcesando contacto {i}/{len(contactos)}: {contacto_formateado}")
            
            #Medir el tiempo tottal
            star_time = time.time()
            success, message = send_whatsapp_message(driver, contacto_formateado, mensaje)
            
            end_time = time.time()
            elapsed_time = end_time - star_time
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
                print("Continuando con el siguiente contacto...")

            print(f"Tiempo de envío del mensaje: {elapsed_time:.2f} segundos")

            # Pequeña pausa entre mensajes
            time.sleep(random.randint(5, 15))

    
    except Exception as e:
        print(f"\n❌ Error general: {str(e)}")
    
    finally:
        print("\nPresiona Enter para cerrar el navegador...")
        input()
        driver.quit()

if __name__ == "__main__":
    main()
