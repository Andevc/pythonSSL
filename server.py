import socket
import ssl

CERTFILE = 'ssl/tcp/server_tcp.crt'
KEYFILE = 'ssl/tcp/server_tcp.key'

HOST = 'localhost'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

ssl_sock = context.wrap_socket(sock, server_side=True)

print(f"Servidor escuchando en https://{HOST}:{PORT}")

while True:
    conn, addr = ssl_sock.accept()
    print(f"Conexión establecida con {addr}")
    
    # Recibir mensaje del cliente
    mensaje = conn.recv(1024).decode("utf-8")
    print(f"Mensaje recibido: {mensaje}")

    # Enviar respuesta al cliente
    respuesta = "Hola, cliente. Conexión segura establecida."
    conn.send(respuesta.encode("utf-8"))

    conn.close()