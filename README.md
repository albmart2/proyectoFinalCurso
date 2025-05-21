# Proyecto Final Curso DevOps | AIOps
## Idea general del proyecto
Este proyecto permite tener un entorno de monitorización completo, todo gestionado a través de Ansible.
## Estructura del proyecto

	proyectoFinalCurso/
	├── app/
	│   ├── app.py
	│   ├── Dockerfile
	│   └── requirements.txt
	├── prometheus.yml
	├── docker-compose.yml
	└── playbook.yml

## Ejecutar el proyecto
### Requisitos previos
Antes de ejecutar el proyecto, se debe de tener instalado antes de ejecutar el playbook.
### Instalacion Ansible en Linux (Debian/Ubuntu)
1. Instalar Ansible:

	```bash
	sudo apt update
	```

	```bash
	sudo apt install ansible -y
	```

2. Verificar la disponibilidad de ```ansible-galaxy```:

	```bash
	ansible-galaxy --help
	```

### Ejecutar el Playbook
- Para poder iniciar todos los servicios, debemos de ejecutar:

	```bash
	ansible-playbook playbook.yml --tags "start"
	```

- Para poder detener y eliminar todos los servicios, debemos de ejecutar:
	
	```bash
	ansible-playbook playbook.yml --tags "stop"
	```

## Explicacion del proyecto detalladamente

### /app/app.py

Contiene el código Python de la web, expone las rutas, genera los números aleatorios y publica las métricas para Prometheus.

### /app/requirements.txt

Indica los paquetes que deben instalarse (por ejemplo, Flask y prometheus_client) para que la aplicación funcione correctamente.

### /app/Dockerfile

Define cómo construir el contenedor de la app Flask (instala dependencias, copia el código, expone el puerto, etc.).

### prometheus.yml

Indica a Prometheus qué endpoints debe monitorizar (scrape), con qué frecuencia y bajo qué nombre.

### docker-compose.yml

Define y coordina todos los servicios del proyecto: la app Flask, Prometheus, Grafana y sus volúmenes/redes.

### playbook.yml

Automatiza tareas como levantar o parar los servicios definidos en Docker Compose.
