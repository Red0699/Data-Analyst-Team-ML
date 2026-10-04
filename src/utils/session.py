import json

def cargar_sesion():
    with open("config/session.json", "r") as archivo:
        return json.load(archivo)

def guardar_sesion(datos_actualizados):
    with open("config/session.json", "r") as archivo:
        datos = json.load(archivo)

    datos.update(datos_actualizados)

    with open("config/session.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)




