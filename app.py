from flask import Flask, request, jsonify
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
import os
import datetime

app = Flask(__name__)

# Initialize Pinecone client
pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

# Create Assistant object
assistant = pc.assistant.Assistant(assistant_name=os.environ.get('ASSISTANT_NAME'))

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

def serialize_value(value):
    if isinstance(value, datetime.datetime):
        return value.isoformat() + 'Z'
    elif isinstance(value, (str, int, float, bool, type(None))):
        return value
    elif isinstance(value, list):
        return [serialize_value(item) for item in value]
    elif isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    elif hasattr(value, '__dict__'):
        return {k: serialize_value(v) for k, v in value.__dict__.items() if not k.startswith('_')}
    else:
        return str(value)

@app.route('/list', methods=['GET'])
def list_files():
    try:
        response = assistant.list_files()
        file_dicts = [serialize_value(file) for file in response]
        return jsonify({"files": file_dicts}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
