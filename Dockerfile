# Imagem base com Python 3.9
FROM python:3.9.18-slim

# Define o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copia os arquivos de requirements
COPY requirements.txt ./

# Instala dependências do sistema para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia todo o conteúdo do projeto para o container
COPY . .

# Expõe a porta da aplicação Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
