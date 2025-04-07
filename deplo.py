from flask import Flask, request, jsonify
from langchain_groq import ChatGroq

# Function to call the Generative AI model
def ask(prompt, api_key):
    try:
        llm = ChatGroq(model='llama-3.3-70b-versatile', api_key=api_key)
        response = llm.invoke(prompt)
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}

# Initialize Flask app
app = Flask(__name__)

# Define the /ask endpoint
@app.route('/ask', methods=['POST'])
def ask_endpoint():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        api_key = data.get("api_key")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        if not api_key:
            return jsonify({"error": "API key is required"}), 400

        # Call the ask function with user-provided API key
        response = ask(prompt, api_key)

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
