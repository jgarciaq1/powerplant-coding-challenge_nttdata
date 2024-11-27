from flask import Blueprint, request, jsonify

from app.utils import power_distribution

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/productionplan', methods=['POST'])
def production_plan():
    data = request.get_json()
    # Si no se encuentran las estructuras principales se devuelve un error
    if not data or "load" not in data or "fuels" not in data or "powerplants" not in data:
        return jsonify({"error": "Datos inválidos o incompletos"}), 400

    try:
        # Parsear los datos principales
        load = data["load"]
        fuels = data["fuels"]
        powerplants = data["powerplants"]

        # Aplicar lógica de distribución
        result = power_distribution(load, fuels, powerplants)

        # Devolver el resultado
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Error procesando la solicitud: {str(e)}"}), 500

