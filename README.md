# Proyecto powerplant-coding-challenge

Este proyecto contiene una API construida con Flask que distribuye la carga de energía entre diferentes plantas de energía, en función de los costos y la eficiencia de cada planta.

## Requisitos previos

Para ejecutar este proyecto, asegúrate de tener instalado Python 3.8+ en tu sistema.

## 1. Entorno virtual (venv)

Junto al proyecto se ha añdido un entorno virtual para poder ejecutarlo.

### En sistemas Unix (Linux/macOS)

1. Navega a la carpeta raíz de tu proyecto en la terminal.
2. Ejecuta el siguiente comando para crear el entorno virtual:

    ```bash
    python3 -m venv venv
    ```

3. Para activar el entorno virtual, ejecuta:

    ```bash
    source venv/bin/activate
    ```

### En sistemas Windows

1. Navega a la carpeta raíz de tu proyecto en la terminal.
2. Ejecuta el siguiente comando para crear el entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Para activar el entorno virtual, ejecuta:

    ```bash
    venv\Scripts\activate
    ```


## 2. Instalar las dependencias desde `requirements.txt`

Una vez que el entorno virtual esté activo, necesitas instalar las dependencias necesarias para ejecutar el proyecto. 

1. Asegúrate de estar en el entorno virtual activado.
2. Ejecuta el siguiente comando para instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

Esto instalará Flask.

## 3. Ejecutar el servidor con `run.py`

Una vez que las dependencias estén instaladas, puedes ejecutar el servidor de Flask para iniciar la aplicación.

1. Asegúrate de estar en el entorno virtual activado y en la carpeta raíz del proyecto.
2. Ejecuta el siguiente comando para iniciar la aplicación:

    ```bash
    python run.py
    ```

Esto iniciará el servidor Flask en el puerto `8888`. La API estará disponible en `http://127.0.0.1:8888/productionplan` para recibir solicitudes POST.

## 4. Probar la API

Puedes probar la API usando herramientas como **Postman** o **cURL**. Un ejemplo de cómo hacer una solicitud POST con `cURL` sería:

```bash
curl -X POST http://127.0.0.1:8888/productionplan -H "Content-Type: application/json" -d '{
  "load": 910,
  "fuels": {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    }
  ]
}'
```

### Probar api con python.
En el proyecto se incluye un proyecto que permite leer un fichero json y enviarlo como solicitud al api, para usarlo, de deber configurar el entorno virtual e instalar las dependencias igual que en el proyecto principal.

A continuación, se ejecuta el archivo test.py, indicandole como parámetro la ruta donde está el fichero que se quiere enviar.

 ```bash
    python test.py "ruta/al/fichero.json"
```

