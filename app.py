import sys
print("Python version:", sys.version)

from flask import Flask, request, jsonify
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message  # Adjust if `pinecone_plugins` is the correct module
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Pinecone client with API key from environment variables
pinecone_api_key = os.getenv('PINECONE_API_KEY')
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY is not set in environment variables.")

pc = Pinecone(api_key=pinecone_api_key)
assistant = pc.assistant.Assistant(assistant_name=os.getenv('ASSISTANT_NAME'))

def chat_with_assistant(question):
    chat_context = [Message(content=question)]
    response = assistant.chat_completions(messages=chat_context)
    return response.choices[0].message.content

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({"error": "No question provided"}), 400

    question = data['question']
    answer = chat_with_assistant(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
