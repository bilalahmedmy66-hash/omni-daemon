import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env file
load_dotenv()

# Initialize client safely from environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def synthesize_code(intent):
    """Takes a human intent and forces the AI to output ONLY raw Python code."""
    prompt = f"""
    You are the Omni-Daemon core routing brain. 
    Task: "{intent}"
    Write ONLY valid, executable Python code to accomplish this task. 
    Do not include markdown formatting (like ```python). 
    Do not include explanations. Just the raw code.
    Make sure the code prints its final result to the console.
    """

    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
    )

    clean_code = response.text.strip().replace("```python", "").replace("```", "")
    return clean_code