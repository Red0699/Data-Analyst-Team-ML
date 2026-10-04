from api.auth import enviar_codigo_verificacion, login
from utils import session

def main():

    datos = session.cargar_sesion()

    enviar_codigo_verificacion(
        role_id=datos["role_id"],
        zone_id=datos["zone_id"]
    )

    while True:
        codigo = input("Ingrese el código recibido: ")

        if len(codigo) != 4:
            print("Código no válido")
            continue

        break

    respuesta = login(
        role_id=datos["role_id"],
        zone_id=datos["zone_id"],
        vc=codigo
    )

    if respuesta and respuesta["code"] == 0:

        session.guardar_sesion({
            "jwt": respuesta["data"]["jwt"],
            "token": respuesta["data"]["token"]
        })

        print("Login exitoso")

    else:
        print("Login fallido")


if __name__ == "__main__":
    main()