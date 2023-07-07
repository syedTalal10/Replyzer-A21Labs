from flask import Flask, request, jsonify
from flask_cors import CORS
import requests as req
import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get('API_KEY')

@app.route("/")
def get_answer():
    context = request.args.get('context')
    question = request.args.get('question')

    if not context or not question:
        return jsonify({'error': 'Both "context" and "question" parameters are required.'}), 400

    url = "https://api.ai21.com/studio/v1/experimental/answer"

    payload = {
        "context": context,
        "question": question
    }

    headers = {
        "accept": "application/json",
        "content-type" : "application/json",
        "Authorization" : f'Bearer {API_KEY}'
    }

    response = req.post(url, json=payload, headers=headers)
    return response.text

if __name__ == '__main__':
    app.run()
