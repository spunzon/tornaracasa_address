# Usar una imagen base de Python 3.12
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar poetry
RUN pip install poetry

# Copiar los archivos de configuración de poetry
COPY pyproject.toml poetry.lock* ./

# Configurar poetry para no crear un entorno virtual dentro del contenedor
RUN poetry config virtualenvs.create false

# Instalar dependencias
RUN poetry install --no-dev --no-interaction --no-ansi

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto que usa FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
