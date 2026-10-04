import requests
from config.settings import BASE_URL
from utils import session

def logout(jwt):
    url = f"{BASE_URL}/user/auth/logout"

    headers = {
        "Authorization": f"Bearer {jwt}"
    }

    try:
        respuesta = requests.post(
            url,
            headers=headers
        )

        datos = respuesta.json()

        if respuesta.status_code == 200 and datos.get("code") == 0:
            return datos

        return datos

    except Exception as e:
        return str(e)

datos = session.cargar_sesion()

resultado = logout(datos["jwt"])

session.guardar_sesion({
    "jwt": "...",
    "token": "..."
})

