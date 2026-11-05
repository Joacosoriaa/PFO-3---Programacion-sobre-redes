
# PFO 3 - Sistema Distribuido

## Objetivo
Implementar una arquitectura cliente-servidor
utilizando sockets TCP y programacion concurrente
en Python.

## Diagrama de arquitectura

El siguiente diagrama representa la arquitectura propuesta para el sistema distribuido.
![Diagrama del sistema distribuido](diagrama_arquitectura.png)

## Componentes
- Cliente Python: envia tareas y recibe resultados.
- Servidor TCP: recibe y responde solicitudes.
- ThreadingTCPServer: atiende conexiones concurrentes.
- ThreadPoolExecutor: distribuye tareas entre hilos.
- JSON: formato de intercambio de datos.

## Requisitos
- Python 3.9 o superior.

## Ejecucion
1. Abrir una terminal y ejecutar:
   python servidor.py

2. Abrir otra terminal y ejecutar:
   python cliente.py

## Ejemplo
El cliente envia una lista de numeros.
El servidor calcula la suma y devuelve el resultado.

## Arquitectura futura
Se propone incorporar Nginx o HAProxy,
RabbitMQ, PostgreSQL y almacenamiento S3.
