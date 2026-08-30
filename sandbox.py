import subprocess
import os
import re

def run_in_sandbox(code_string):
    """Executes Python code inside workspace/ and automatically installs missing imports."""
    workspace_dir = os.path.join(os.path.dirname(__file__), "workspace")
    os.makedirs(workspace_dir, exist_ok=True)
    
    script_path = os.path.join(workspace_dir, "temp_task.py")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code_string)
        
    for attempt in range(2): # Try running; if a module is missing, install it and retry once
        try:
            result = subprocess.run(
                ["python", "temp_task.py"],
                capture_output=True,
                text=True,
                timeout=15,
                cwd=workspace_dir
            )
            
            # Check if execution failed due to a missing module (ImportError / ModuleNotFoundError)
            if result.returncode != 0 and attempt == 0:
                stderr = result.stderr
                match = re.search(r"No module named '(.+?)'", stderr)
                if match:
                    missing_module = match.group(1)
                    print(f"[Sandbox] Missing module detected: '{missing_module}'. Installing...")
                    # Automatically install the missing package
                    install_res = subprocess.run(
                        ["python", "-m", "pip", "install", missing_module],
                        capture_output=True,
                        text=True
                    )
                    if install_res.returncode == 0:
                        continue # Retry running the script with the new package installed
            
            if result.returncode != 0:
                return {
                    "status": "error",
                    "output": result.stderr.strip()
                }
                
            return {
                "status": "success",
                "output": result.stdout.strip() if result.stdout.strip() else "Execution completed successfully (no console output)."
            }
            
        except subprocess.TimeoutExpired:
            return {
                "status": "error",
                "output": "Execution timed out (exceeded 15 seconds)."
            }
        except Exception as e:
            return {
                "status": "error",
                "output": str(e)
            }
    
    return {"status": "error", "output": "Failed to resolve dependencies and execute code."}