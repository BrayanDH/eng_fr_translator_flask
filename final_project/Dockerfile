# Usa la imagen base de Python con la versión que necesites
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) al directorio /app del contenedor
COPY requirements.txt /app/

# Instala las dependencias necesarias dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual (que contiene tu aplicación Flask) al directorio /app del contenedor
COPY . /app/

# Expone el puerto 8080 que es el puerto por defecto para Flask
EXPOSE 8080

# Comando para ejecutar la aplicación Flask
CMD ["python", "server.py"]
