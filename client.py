import socket
import ssl

from config import HOST, PORT, CERTFILE

# Crear el socket del cliente
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Envolver el socket con SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(CERTFILE)

ssl_sock = context.wrap_socket(sock, server_hostname=HOST)

# Conectar al servidor
ssl_sock.connect((HOST, PORT))
print(f"Conectado al servidor https://{HOST}:{PORT}")

# Enviar mensaje al servidor
mensaje = "Hola, servidor. Esto es seguro."
ssl_sock.send(mensaje.encode("utf-8"))

# Recibir respuesta del servidor
respuesta = ssl_sock.recv(1024).decode("utf-8")
print(f"Respuesta del servidor: {respuesta}")

ssl_sock.close()
