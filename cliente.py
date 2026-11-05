import socket
import json

HOST = "127.0.0.1"
PORT = 5000

tarea = {
    "operacion": "sumar",
    "numero": [1, 2, 3, 4, 5]
}

try:
    #Conectarse al servidor
    with socket.create_connection((HOST, PORT)) as cliente:
        #Enviar la tarea como mensaje JSON
        mensaje = json.dumps(tarea) + "\n"
        cliente.sendall(mensaje.encode("utf-8"))

        #Recibir el resultado
        archivo = cliente.makefile("r",encoding="utf-8")
        respuesta = archivo.readline().strip()
        resultado = json.loads(respuesta)

        print(f"Resultado recibido: {resultado}")
except ConnectionRefusedError:
    print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")

except OSError as error:
    print(f"Error de comunicacion socket: {error}")