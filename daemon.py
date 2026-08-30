import os
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from brain import synthesize_code
from sandbox import run_in_sandbox

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def serve_ui():
    """Directly reads and serves index.html as a text response."""
    html_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    return "Error: index.html not found in directory!", 404

@app.route('/omni/execute', methods=['POST'])
def execute_intent():
    data = request.json
    intent = data.get('intent')
    
    if not intent:
        return jsonify({"error": "No intent provided"}), 400
        
    print(f"\n[1] Received intent: {intent}")
    
    print("[2] Synthesizing code using AI...")
    generated_code = synthesize_code(intent)
    
    print("[3] Executing code in Native Python Sandbox...")
    result = run_in_sandbox(generated_code)
    
    print("[4] Returning results to client.")
    return jsonify({
        "status": "success",
        "intent": intent,
        "code_executed": generated_code,
        "sandbox_output": result
    })

if __name__ == "__main__":
    print("========================================")
    print("    OMNI-DAEMON STUDIO SERVER RUNNING    ")
    print("========================================")
    
    # Render assigns a dynamic port via the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    
    # Bind to 0.0.0.0 to accept external cloud traffic
    app.run(host="0.0.0.0", port=port)