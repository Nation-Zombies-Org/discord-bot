# Uses the official Python image
FROM python:3.12-slim

# Defines the work directory inside the container
WORKDIR /src

# Copy the project files into the container
COPY . .

# Install Bot Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "src/bot.py"]
