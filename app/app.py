from flask import Flask, Response
import random
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Métricas Prometheus
VISITAS_PAGINA = Counter(
    'app_visitas_pagina_total',
    'Número total de veces que la página principal ha sido visitada'
)
ULTIMO_NUMERO_ALEATORIO = Gauge(
    'app_ultimo_numero_aleatorio',
    'El último número aleatorio generado por la aplicación'
)

@app.route('/')
def home():
    # Incrementar el contador de visitas
    VISITAS_PAGINA.inc()

    # Generar un número aleatorio
    numero_aleatorio = random.randint(1, 100)

    # Establecer el valor del último número aleatorio para la métrica Gauge
    ULTIMO_NUMERO_ALEATORIO.set(numero_aleatorio)

    # Devolver el HTML
    return f"<h1>Texto sencillo</h1><p>El número aleatorio es: {numero_aleatorio}</p><p>Visita <a href='/metrics'>/metrics</a> para ver las métricas.</p>"

@app.route('/metrics')
def metrics():
    # Exponer las métricas en el formato que Prometheus espera
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    # Ejecutar la aplicación en el host 0.0.0.0 para que sea accesible desde fuera del contenedor
    # y en el puerto 8080, que es el que expondremos.
    app.run(host='0.0.0.0', port=8080)
