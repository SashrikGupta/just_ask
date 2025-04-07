from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
# Function to call the Generative AI model

llm = ChatGroq(model = 'llama-3.3-70b-versatile' , api_key="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")

def ask(prompt):
    try:
        response = llm.invoke(prompt)
        return response.content
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
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Call the ask function
        response = ask(prompt)

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    port = int(5000)
    app.run(host='0.0.0.0', port=port, debug=True)

