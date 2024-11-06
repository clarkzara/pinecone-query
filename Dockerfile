# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
RUN pip install --upgrade pinecone pinecone-plugin-assistant

# Expose port 8080 for Render
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

