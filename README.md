# Proyecto Final Curso DevOps | AIOps
## Idea general del proyecto
Este proyecto permite tener un entorno de monitorización completo, todo gestionado a través de Docker.
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

2. Verificar la disponibilidad de ansible-galaxy:

	```bash
	ansible-galaxy --help
	```

### Ejecutar Docker
Para poder crear la imagen de Docker, debemos de ejecutar:
```
docker compose up -d
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

