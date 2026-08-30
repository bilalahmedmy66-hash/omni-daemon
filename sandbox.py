import subprocess
import tempfile
import os

def run_in_sandbox(code_string, timeout_seconds=5):
    """
    Takes a string of Python code, writes it to a temporary file, 
    executes it safely, and returns the result.
    """
    # 1. Create a temporary file that automatically deletes itself later
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code_string)
        temp_filepath = temp_file.name

    try:
        # 2. Execute the temporary file as a separate subprocess
        result = subprocess.run(
            ['python', temp_filepath], 
            capture_output=True, 
            text=True, 
            timeout=timeout_seconds # Kills the code if it takes too long
        )
        
        # 3. Check if the code crashed or succeeded
        if result.returncode == 0:
            return {"status": "success", "output": result.stdout.strip()}
        else:
            return {"status": "error", "output": result.stderr.strip()}
            
    except subprocess.TimeoutExpired:
        return {"status": "error", "output": f"Code execution exceeded {timeout_seconds} seconds and was killed."}
        
    finally:
        # 4. Always clean up and delete the temporary file from the computer
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)

# --- TEST THE SANDBOX ---
if __name__ == "__main__":
    print("Testing Omni-Daemon Sandbox...")
    
    # Imagine the AI just generated this math script
    ai_generated_code = """
x = 50
y = 100
print(f"The calculated result is: {x * y}")
"""
    
    # Run the AI code through our sandbox
    response = run_in_sandbox(ai_generated_code)
    print(response)