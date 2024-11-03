# Use a lightweight Python image
FROM python:3.8-slim

# Install pinecone-client
RUN pip install pinecone-client

# Simple command to keep the container running
CMD ["python3", "server.py"]
