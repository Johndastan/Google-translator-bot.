import os
import re

from selenium import webdriver #importa el paquete de Selenium WebDriver, instala: pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.binary_location = "C:\\SeleniumDrivers\\chrome-win64\\chrome.exe"
service = Service("C:\\SeleniumDrivers\\chromedriver-win64\\chromedriver.exe")
driver= webdriver.Chrome(service=service, options=options)# Crea un controlador

driver.set_window_position(0,0)#Coloca la posicion de la ventana
driver.set_window_size(1024,720)#Crea una resolucion con la que la ventana se muestra

driver.get("https://translate.google.com.mx/?sl=es&tl=en&op=translate")

textarea_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[@aria-label='Texto de origen']")
    )
)

captions_dir= "files\\captions"#Esta es la ruta de los subtitulos que esta dentro de files,otra carpeta captions y dentro el archivo vtt
translations_dir= "files\\translations"#Ruta de la carpeta dentro de files de la traduccion donde se creara el archivo que tenga los subtitulos traducidos al ingles.
files_list= []#La lista que se crea a partir de lo que se traduce, si falla se imprime en blanco
def get_files_list(captions_dir, files_list) -> list:
    for f in os.scandir(captions_dir):
        if f.is_dir():
            get_files_list(f.path, files_list)
        else:
            files_list.append(f.path)
    return files_list
file_paths= get_files_list(captions_dir, files_list)
print(file_paths)

for file_path in file_paths[0:1]:
    print("\nTraduciendo el archivo:", file_path)
    print("Ruta absoluta:", os.path.abspath(file_path))
    print("Tamaño:", os.path.getsize(file_path), "bytes")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    translation_path= file_path.replace(captions_dir, translations_dir)
    os.makedirs(os.path.dirname(translation_path), exist_ok=True)
    print(lines)

    regular_exp = re.compile(r'[0-9]{2}:[0-9]{2}\.[0-9]{3} --> [0-9]{2}:[0-9]{2}\.[0-9]{3}')
    
    textarea_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
            (By.XPATH, "//*[@aria-label='Texto de origen']")
        )
    )
    
for i, tmp_line in enumerate(lines):

    try:
        print(f"Procesando línea {i}: {tmp_line}")

        tmp_line = tmp_line.strip()

        if not regular_exp.match(tmp_line) and tmp_line != "":#Esto evitara errores por lineas vacias en el video.

            textarea_element.send_keys(tmp_line)

            translation_element = WebDriverWait(driver,10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "span[jsname='W297wb']")
                )
            )

            print("Traducción:", translation_element.text)
            
            lines[i] = translation_element.text + "\n"

            textarea_element.clear()
            WebDriverWait(driver, 5).until(
                lambda d: textarea_element.get_attribute("value") == ""
            )#En caso de que Google transalte si .clear() no termina rápido, se espera a que el textarea esté vacío antes de continuar.
            
            if i > 0 and i % 20 == 0:#Guardar progreso cada 20 lineas traducidas por si el video dura mas de 2 horas.
                with open(translation_path, "w", encoding="utf-8") as f:
                    f.writelines(lines)

    except Exception as e:
        print(f"Error en línea {i}: {e}")
        

print(lines) 

with open(translation_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
driver.quit()