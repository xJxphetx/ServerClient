import socket

def ini_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()
    print("Servidor escuchando en localhost:5000")

    while True:
        client, address = server.accept()
        print(f"Cliente conectado: {address}")

        while True:
            datos = client.recv(1024)
            if not datos:
                break
            mensage = datos.decode('utf-8').strip()
            print(f"Mensaje recibido: {mensage}")

            if mensage == "DESCONEXION":
                print("Cerrando conexión con el cliente")
                client.close()
                break
            else:
                answ = mensage.upper()
                client.sendall(answ.encode('utf-8'))

if __name__ == "__main__":
    ini_server()
