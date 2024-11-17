from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure the Generative AI model
genai.configure(api_key="AIzaSyBcBNW3moG8nFwpqCe7IiPAWqzMJx3WNK0")
model = genai.GenerativeModel("gemini-1.5-pro")

# Function to call the Generative AI model
def ask(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
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
    app.run(debug=True)
