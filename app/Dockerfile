# Usar una imagen base oficial de Python. python:3.9-slim es una buena opción por ser ligera.
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos al directorio de trabajo
COPY requirements.txt ./

# Instalar las dependencias de Python definidas en requirements.txt
# --no-cache-dir reduce el tamaño de la imagen al no guardar el caché de pip
# --trusted-host pypi.python.org es útil si hay problemas con SSL en entornos corporativos o con proxies
RUN pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

# Copiar el resto del código de la aplicación (app.py) al directorio de trabajo
COPY app.py ./

# Exponer el puerto 8080, que es el puerto en el que la aplicación Flask escuchará
EXPOSE 8080

# El comando que se ejecutará cuando el contenedor inicie
CMD ["python", "app.py"]

