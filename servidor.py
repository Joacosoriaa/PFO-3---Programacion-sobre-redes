import socketserver
import json
import time
from concurrent.futures import ThreadPoolExecutor

#Pool de 4 hilos para procesar tareas
pool = ThreadPoolExecutor(max_workers=4)

def procesar_tarea(tarea):
    #Funcion ejecutada por los hilos workers
    operacion = tarea.get("operacion")
    numeros = tarea.get("numero")

    if operacion != "sumar":
        return {"error": "Operacion no soportada"}

    if not isinstance(numeros, list) or not numeros:
        return {"error": "Debes enviar una lista de numeros"}

    if any(type(n) not in [int, float] for n in numeros):
        return {"error": "Todos los elementos de la lista deben ser numeros"}

    # Simula una tarea que tarda en procesarse
    time.sleep(2)

    resultado = sum(numeros)
    return {
        "mensaje": "Operacion realizada con exito",
        "resultado": resultado
    }

class Manejador(socketserver.StreamRequestHandler):
    def handle(self):
        # Recibe la tarea del cliente
        try:
            datos = self.rfile.readline().strip()

            if not datos:
                return

            tarea = json.loads(datos.decode("utf-8"))
            print(f"Recibida tarea: {tarea}")

            #Enviar la tarea al pool de hilos para procesarla
            futuro = pool.submit(procesar_tarea, tarea)

            # Espera a que la tarea se complete y obtiene el resultado
            resultado = futuro.result()  

            #Devolver el resultado al cliente
            respuesta = json.dumps(resultado) + "\n"
            self.wfile.write(respuesta.encode("utf-8"))

            print(f"Resultado enviado: {resultado}")
        except (json.JSONDecodeError, UnicodeDecodeError):
            error_respuesta = {"error": "Mensaje JSON no valido"}
            self.wfile.write((json.dumps(error_respuesta) + "\n").encode("utf-8"))

class Servidor(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 5000

    with Servidor((HOST, PORT), Manejador) as servidor:
        print(f"Servidor escuchando en el puerto {PORT}")

        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("Servidor detenido por el usuario")
        finally:
            pool.shutdown(wait=True)