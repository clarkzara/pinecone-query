# Use a lightweight Python image
FROM python:3.9-slim

# Install required packages
RUN pip install flask pinecone-client

# Set the working directory
WORKDIR /app

# Copy the app files into the container
COPY . /app

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the Flask app in app.py
CMD ["python", "app.py"]
