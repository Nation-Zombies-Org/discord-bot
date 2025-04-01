# 📌 Passo 1: Instalar Docker na VPS

Antes de tudo, acesse sua VPS via SSH:

```sh
ssh user@VPS_IP
```

Agora, instale o Docker e o Docker Compose:

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
sudo systemctl enable --now docker
```

Para garantir que o Docker está funcionando:

```sh
docker --version
docker-compose --version
```

Se quiser rodar Docker sem sudo, adicione seu usuário ao grupo docker:

```sh
sudo usermod -aG docker $USER
newgrp docker
```

---

# 📌 Passo 2: Criar um `Dockerfile`

No diretório do seu projeto, crie um arquivo chamado `Dockerfile`:

```sh
nano Dockerfile
```

Adicione o seguinte conteúdo:

```sh
# Usa a imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do bot
RUN pip install --no-cache-dir -r requirements.txt

# Define as variáveis de ambiente (pode ser sobrescrita no docker-compose)
ENV DISCORD_BOT_TOKEN="SEU_TOKEN_AQUI"

# Comando para rodar o bot
CMD ["python", "src/bot.py"]
```

---

# 📌 Passo 3: Criar um arquivo .dockerignore

Para evitar copiar arquivos desnecessários para o container, crie um .dockerignore:

```sh
nano .dockerignore
```

Adicione:

```sh
__pycache__/
venv/
.env
.git
.DS_Store
```

Isso evita que arquivos temporários e credenciais sensíveis sejam incluídos.

---

# 📌 Passo 4: Criar um docker-compose.yml

Se quiser gerenciar o container de forma mais prática, crie um docker-compose.yml:

```sh
nano docker-compose.yml
```

Adicione:

```sh
version: "3.8"

services:
  discord-bot:
    build: .
    container_name: discord-bot
    restart: always
    environment:
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
    volumes:
      - .:/app
```

Esse arquivo define um serviço chamado `discord-bot`, que:

- Constrói o container com base no Dockerfile

- Reinicia automaticamente se o bot cair

- Define variáveis de ambiente para evitar expor o token diretamente no código

---

# 📌 Passo 5: Criar um .env (Opcional, mas recomendado)

Crie um arquivo `.env` para armazenar o token do bot sem expô-lo no código:

```sh
nano .env
```

Adicione:

```sh
DISCORD_BOT_TOKEN=SEU_TOKEN_AQUI
```

Agora, o `docker-compose.yml` usará essa variável automaticamente.

---

# 📌 Passo 6: Construir e rodar o container

Agora é hora de construir e rodar o bot no Docker.

1️⃣ Se estiver usando docker-compose:

```sh
docker-compose up -d --build
```

- `-d`: roda o container em segundo plano

- `--build`: força a reconstrução da imagem

Verifique se o container está rodando:

```sh
docker ps
```

2️⃣ Se estiver usando `docker` diretamente:

```sh
docker build -t discord-bot .
docker run -d --name discord-bot --env-file .env discord-bot
```

---

# 📌 Passo 7: Monitorar e Gerenciar o Bot

Agora que o bot está rodando, aqui estão alguns comandos úteis:

✅ **Ver logs do bot:**

```sh
docker logs -f discord-bot
```

✅ **Reiniciar o bot:**

```sh
docker restart discord-bot
```

✅ **Parar o bot:**

```sh
docker stop discord-bot
```

✅ **Remover o container:**

```sh
docker rm -f discord-bot
```

✅ **Remover a imagem (caso precise recriar):**

```sh
docker rmi discord-bot
```

✅ **Atualizar código do bot e reiniciar:**

```sh
git pull origin main
docker-compose up -d --build
```

---

# 📌 Passo 8: Iniciar automaticamente na VPS

Se quiser que o bot inicie automaticamente quando a VPS ligar, adicione o Docker ao boot:

```sh
sudo systemctl enable docker
```

Caso tenha usado docker-compose, crie um serviço systemd:

```sh
sudo nano /etc/systemd/system/discord-bot.service
```

Adicione:

```sh
[Unit]
Description=Discord Bot
After=network.target

[Service]
User=seu-usuario
WorkingDirectory=/caminho/para/seu-bot
ExecStart=/usr/bin/docker-compose up -d --build
Restart=always

[Install]
WantedBy=multi-user.target
```

Habilite e inicie o serviço:

```sh
sudo systemctl daemon-reload
sudo systemctl enable discord-bot
sudo systemctl start discord-bot
```

Agora o bot sempre iniciará automaticamente!

---

# 🚀 Resumo Final

- 1️⃣ **Instalar Docker e Docker Compose**
- 2️⃣ **Criar `Dockerfile`, `.dockerignore` e `docker-compose.yml`**
- 3️⃣ **Configurar `.env` para armazenar o token**
- 4️⃣ **Construir e rodar o container (`docker-compose up -d --build`)**
- 5️⃣ **Gerenciar o bot com `docker ps`, `docker logs -f discord-bot`, etc.**
- 6️⃣ **Configurar para iniciar automaticamente com `systemd`**

---

# Autor:

[Desenvolvedor - < ᵈᵉᵛZen />](https://github.com/zeneiltongpdev)