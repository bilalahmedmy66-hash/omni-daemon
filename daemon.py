from flask import Flask, request, jsonify
from brain import synthesize_code
from sandbox import run_in_sandbox

app = Flask(__name__)

@app.route('/omni/execute', methods=['POST'])
def execute_intent():
    data = request.json
    intent = data.get('intent')
    
    if not intent:
        return jsonify({"error": "No intent provided"}), 400
        
    print(f"\n[1] Received intent: {intent}")
    
    # Phase A: The Brain writes the code
    print("[2] Synthesizing code using AI...")
    generated_code = synthesize_code(intent)
    
    # Phase B: The Sandbox runs the code safely
    print("[3] Executing code in Native Python Sandbox...")
    result = run_in_sandbox(generated_code)
    
    # Phase C: Return the final output
    print("[4] Returning results to client.")
    return jsonify({
        "status": "success",
        "intent": intent,
        "code_executed": generated_code,
        "sandbox_output": result
    })

if __name__ == "__main__":
    print("========================================")
    print("   OMNI-DAEMON NATIVE SERVER RUNNING    ")
    print("========================================")
    # The server listens locally on port 5000
    app.run(host="127.0.0.1", port=5000)