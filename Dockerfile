# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set the default value for the API key build argument
ARG OPENAI_API_KEY=default-api-key

# Set the environment variable for the OpenAI API key
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Command to run the Flask application
CMD ["python", "app.py"]
