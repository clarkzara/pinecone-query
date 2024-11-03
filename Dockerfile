FROM python:3.8-slim

# Install pinecone-client
RUN pip install pinecone-client

# Copy server.py to the working directory
COPY server.py /app/server.py
WORKDIR /app

# Command to run the server
CMD ["python3", "server.py"]
