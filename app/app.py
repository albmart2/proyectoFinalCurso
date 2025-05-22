from flask import Flask, request, Response
import random
import time
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

VISITAS_PAGINA = Counter(
    'app_visitas_pagina_total',
    'Número total de veces que la página principal ha sido visitada'
)

ULTIMO_NUMERO_ALEATORIO = Gauge(
    'app_ultimo_numero_aleatorio',
    'El último número aleatorio generado por la aplicación'
)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint']
)

ERROR_COUNT = Counter(
    'http_request_errors_total',
    'Total HTTP Request Errors',
    ['method', 'endpoint', 'status']
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    resp_time = time.time() - getattr(request, 'start_time', time.time())
    method = request.method
    endpoint = request.path
    status = response.status_code

    REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=status).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(resp_time)

    if status >= 400:
        ERROR_COUNT.labels(method=method, endpoint=endpoint, status=status).inc()

    return response

@app.route('/')
def home():
    VISITAS_PAGINA.inc()
    numero_aleatorio = random.randint(1, 100)
    ULTIMO_NUMERO_ALEATORIO.set(numero_aleatorio)
    return (
        "<h1>APP Números aleatorios</h1>"
        f"<p>El número aleatorio es: {numero_aleatorio}</p>"
        "<p>Visita <a href='/metrics'>/metrics</a> para ver las métricas.</p>"
        "<p>Prueba también <a href='/error'>/error</a> para ver una ruta de error.</p>"
    )

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/error')
def error():
    return "Esto es un error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
