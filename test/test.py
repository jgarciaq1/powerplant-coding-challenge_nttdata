import json
import requests
import argparse


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def send_post_request(url, data):
    response = requests.post(url, json=data)
    return response


def main():
    parser = argparse.ArgumentParser(description="Enviar datos JSON a un endpoint vía POST.")
    parser.add_argument('json_file', type=str, help="Ruta del archivo JSON que contiene los datos a enviar.")
    args = parser.parse_args()

    json_file = args.json_file

    api_url = 'http://127.0.0.1:8888/productionplan'

    try:
        data = load_data_from_json(json_file)
    except FileNotFoundError:
        print(f"Error: El archivo {json_file} no fue encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo {json_file} no es un archivo JSON válido.")
        return

    response = send_post_request(api_url, data)

    if response.status_code == 200:
        print("Solicitud exitosa, respuesta:", response.json())
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)


if __name__ == "__main__":
    main()
