# Use a imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /src

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o bot
CMD ["python", "src/bot.py"]