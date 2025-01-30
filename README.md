Aquí tienes un ejemplo de cómo podrías estructurar el archivo `README.md` para que puedas hacer todo el proceso siempre que lo necesites:

```markdown
# Proyecto de WhatsApp Automation

Este proyecto permite enviar mensajes automáticos de WhatsApp a una lista de contactos utilizando Selenium y el driver de Chrome. A continuación, se detallan los pasos necesarios para configurar y ejecutar el proyecto.

## Requisitos previos

1. **Python 3.12.11** (u otra versión compatible).
2. **Google Chrome** (versión compatible con el ChromeDriver).
3. **ChromeDriver**: Descarga el archivo `chromedriver-win64` desde la [página oficial de ChromeDriver](https://sites.google.com/chromium.org/driver/). Asegúrate de descargar la versión correcta que coincida con tu versión de Chrome.

    Los archivos que deberías tener dentro de la carpeta `chromedriver-win64` son:
    - `chromedriver.exe`
    - `LICENSE.chromedriver`
    - `THIRD_PARTY_NOTICES.chromedriver`

4. **Instalar las dependencias necesarias**:
    - Abre la terminal en la raíz del proyecto.
    - Ejecuta el siguiente comando para instalar las librerías necesarias:

    ```bash
    pip install -r requirements.txt
    ```

    Si no tienes el archivo `requirements.txt`, crea uno con el siguiente contenido:

    ```
    selenium
    webdriver-manager
    ```

    Luego, instala las dependencias con el comando anterior.

## Estructura del proyecto

El proyecto debe tener la siguiente estructura de carpetas y archivos:

```
/ProyectoWhatsAppAutomation
    /chromedriver-win64
        chromedriver.exe
        LICENSE.chromedriver
        THIRD_PARTY_NOTICES.chromedriver
    /venv
        /Include
        /Lib
    main.py
    requirements.txt
    .gitignore
    README.md
```

## Pasos para ejecutar el proyecto

### 1. Clona el repositorio

Si aún no tienes el proyecto en tu máquina, clónalo desde GitHub con el siguiente comando:

```bash
git clone https://github.com/TuUsuario/WA_bot.git
```

### 2. Configura el entorno virtual (opcional pero recomendado)

Si quieres trabajar con un entorno virtual, sigue estos pasos:

1. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - En **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```

   - En **Mac/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### 3. Modifica los números de contacto

En el archivo `main.py`, dentro de la función `main()`, modifica la lista de contactos con los números de teléfono a los que deseas enviar los mensajes.

```python
contactos = ["3207414792", "3243747129"]
```

### 4. Configura el archivo `.gitignore`

Asegúrate de que las carpetas `chromedriver-win64` y `venv` no se suban a GitHub. Para ello, agrega las siguientes líneas al archivo `.gitignore`:

```
# Ignorar carpeta de chromedriver
chromedriver-win64/

# Ignorar carpeta virtualenv
venv/
```

### 5. Ejecuta el programa

1. Abre la terminal en la carpeta raíz del proyecto.
2. Ejecuta el siguiente comando para iniciar el programa:

   ```bash
   python main.py
   ```

3. El programa abrirá WhatsApp Web y te pedirá que escanees el código QR con tu teléfono.
4. Una vez escaneado el código QR, el programa comenzará a enviar los mensajes a los contactos especificados.

### 6. Tiempo de envío de los mensajes

El tiempo que toma enviar cada mensaje se mostrará en la terminal, en segundos, después de cada envío. El programa realiza una pausa aleatoria entre 5 y 15 segundos entre cada mensaje.

### 7. Subir cambios a GitHub (si es necesario)

Si realizas cambios en tu proyecto y deseas subirlos a GitHub, sigue estos pasos:

1. Agrega los cambios:

   ```bash
   git add .
   ```

2. Haz un commit de los cambios:

   ```bash
   git commit -m "Descripción de los cambios realizados"
   ```

3. Sube los cambios a GitHub:

   ```bash
   git push origin <nombre-de-tu-rama>
   ```

## Notas

- Asegúrate de que tu versión de Google Chrome sea compatible con el `chromedriver` que estás utilizando.
- Si necesitas actualizaciones o cambios en las dependencias, recuerda actualizar el archivo `requirements.txt`.

## Contribuciones

Si deseas contribuir al proyecto, haz un fork del repositorio, realiza tus cambios y abre un pull request.



