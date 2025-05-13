from flask import Flask, Response
import random
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

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
    VISITAS_PAGINA.inc()

    numero_aleatorio = random.randint(1, 100)

    ULTIMO_NUMERO_ALEATORIO.set(numero_aleatorio)

    return f"<h1>Texto sencillo</h1><p>El número aleatorio es: {numero_aleatorio}</p><p>Visita <a href='/metrics'>/metrics</a> para ver las métricas.</p>"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
