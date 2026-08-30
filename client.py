import requests

class Omni:
    @staticmethod
    def run(intent):
        """Sends the intent to the local Omni-Daemon and returns the result."""
        url = "http://127.0.0.1:5000/omni/execute"
        payload = {"intent": intent}
        
        try:
            response = requests.post(url, json=payload)
            data = response.json()
            
            if data.get("status") == "success":
                # We only return the final sandbox output to the user
                return data["sandbox_output"]["output"]
            else:
                return f"Error: {data}"
                
        except requests.exceptions.ConnectionError:
            return "Error: Could not connect to Omni-Daemon. Is the server running?"

# --- HOW A DEVELOPER ACTUALLY USES YOUR TOOL ---
if __name__ == "__main__":
    print("Sending task to Omni-Daemon...\n")
    
    # The developer just writes what they want
    task = "Generate a random secure password with 16 characters, including numbers and symbols, and print it."
    
    # One line of code to execute anything
    result = Omni.run(task)
    
    print(f"Final Result from Engine:\n{result}")