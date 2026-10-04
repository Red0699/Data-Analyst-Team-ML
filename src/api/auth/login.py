import requests
from config.settings import BASE_URL


def login(role_id, zone_id, vc):
    url = f"{BASE_URL}/user/auth/login"

    payload = {
        "role_id": role_id,
        "zone_id": zone_id,
        "vc": vc
    }

    try:
        response = requests.post(url, json=payload)
        print("Código de estado:", response.status_code)
        if response.status_code == 200:
            datos = response.json()

            if datos.get("code") == 0:
                return datos

            return datos.get(msg)
        elif response.status == 400:
            return f"StatusCode: {response.status_code} | Datos incorrectos o inexistentes"
        elif response.status_code == 401:
            return f"StatusCode: {response.status_code} | No autorizado"
        else:
            return f"StatusCode: {response.status_code} | Error no controlado"
    except Exception as e:
        print(f"Error: {e}")
        return None




