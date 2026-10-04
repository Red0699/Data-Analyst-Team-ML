from config.settings import BASE_URL
import requests

def enviar_codigo_verificacion(role_id, zone_id):
    url = f"{BASE_URL}/user/auth/send-vc"

    payload = {
        "role_id": role_id,
        "zone_id": zone_id
    }

    try:
        respuesta = requests.post(url, json=payload)

        print("Código de estado:", respuesta.status_code)

        #Validaciones
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
        elif respuesta.status_code == 400:
            return f"StatudCode:{respuesta.status_code} | Datos incorrectos o inexistentes "
        elif respuesta.status_code == 401:
            return f"StatudCode:{respuesta.status_code} | No autorizado"
    except Exception as e:
        print(f"Error: {e}")
        return None
