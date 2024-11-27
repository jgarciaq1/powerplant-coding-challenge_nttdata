def real_cost(plant, fuels):
    """
   Lógica para calcular el coste del MWh en función del tipo de planta y de su eficiencia, incluyendo el coste de co2.
   """
    if plant["type"] == "gasfired":
        return (fuels["gas(euro/MWh)"] + fuels["co2(euro/ton)"] * 0.3) / plant["efficiency"]
    elif plant["type"] == "turbojet":
        return fuels["kerosine(euro/MWh)"] / plant["efficiency"]
    elif plant["type"] == "windturbine":
        return 0
    else:
        return float('inf')


def power_distribution(load, fuels, plants):
    """
    Lógica para distribuir la carga entre las plantas.
    """
    distribution = []
    remaining_load = load

    # Se recorren todas las plantas ordenadas por coste real
    for plant in sorted(plants, key=lambda x: real_cost(x, fuels)):
        plant_name = plant["name"]
        plant_type = plant["type"]
        pmin = plant["pmin"]
        pmax = plant["pmax"]
        min_validator = False

        #Se calcula la produccion maxima y minima para las plantas eolicas
        if plant_type == "windturbine":
            pmax = pmax * (fuels.get("wind(%)", 0) / 100)
            pmin = pmin * (fuels.get("wind(%)", 0) / 100)

        #Se comprueba si con lo que ya se ha inlcuido se ha satisfecho toda la demanda
        if remaining_load != 0:
            # Se indica la potencia requerida para la planta entre el valor restante, la potencia maxima y la minima
            power = min(pmax, remaining_load)
            if power < pmin:
                power = pmin
                min_validator = True

            remaining_load -= power

            # Se comprueba si el valor minimo que produce la planta es mayor que el restante, en ese caso se añade el
            # minimo y se sustrae de la anterior la cantidad correspondiente para evitar generar mas energia de la solicitada
            if remaining_load < 0 and distribution[-1]["p"] != 0:
                last_power = distribution[-1]["p"] + remaining_load
                distribution[-1]["p"] = last_power if last_power >= 0 else 0

            # Se añade la planta con la cantidad de energia que debe producir
            distribution.append({
                "name": plant_name,
                "p": round(power, 1)
            })

            if min_validator:
                remaining_load = 0
        # Se añaden las plantas que no tienen que generar energia con valor cero
        else:
            distribution.append({
                "name": plant_name,
                "p": 0
            })
    # En caso de que la cantidad solicitada sea mayor que la cantidad máxima posible, se devuleve un error
    if remaining_load > 0:
        raise ValueError("No fue posible satisfacer toda la carga con las plantas disponibles")

    return distribution
