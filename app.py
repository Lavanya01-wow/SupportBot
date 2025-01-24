from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask():
    # Get the user question from the request body
    user_question = request.json.get('question', '')
    if not user_question:
        return jsonify({'error': 'No question provided'}), 400

    # Create a prompt for ChatGPT
    prompt = f"You are an expert in Segment, mParticle, Lytics, and Zeotap. Answer the following question:\n\n{user_question}"

    try:
        # Get the response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
