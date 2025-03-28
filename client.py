import socket

def ini_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print("Conectado al servidor en localhost:5000")

    while True:
        mensage = input("Ingresa un mensaje: ").strip()
        client.sendall(mensage.encode('utf-8'))

        if mensage == "DESCONEXION":
            print("Cerrando conexión...")
            client.close()
            break

        answ = client.recv(1024)
        print("Respuesta del servidor:", answ.decode('utf-8'))

if __name__ == "__main__":
    ini_client()