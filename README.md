# Proyecto Final Curso DevOps | AIOps
## Idea general del proyecto
Este proyecto permite tener un entorno de monitorización completo, todo gestionado a través de Docker.
## Estructura del proyecto
    |-app/
    |   |-app.py
    |   |-Dockerfile
    |   |-requirments.txt
    |-prometheus.yml
    |-docker-compose.yml
    |-playbook.yml
## Ejecutar el proyecto
### Requisitos previos
Antes de ejecutar el proyecto, se debe de tener instalado antes de ejecutar el playbook.
### Ejecutar el Playbook
- Para poder iniciar todos los servicios, debemos de ejecutar:

		ansible-playbook playbook.yml --tags "start"

- Para poder detener y eliminar todos los servicios, debemos de ejecutar:
	
		ansible-playbook playbook.yml --tags "stop"
## Explicacion del proyecto detalladamente

