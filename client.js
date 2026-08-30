class Omni {
    static async run(intent) {
        const url = "http://127.0.0.1:5000/omni/execute";
        
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ intent: intent })
            });
            
            const data = await response.json();
            
            if (data.status === "success") {
                return data.sandbox_output.output;
            } else {
                return `Error: ${JSON.stringify(data)}`;
            }
        } catch (error) {
            return "Error: Could not connect to Omni-Daemon. Is the server running?";
        }
    }
}

// --- HOW A DEVELOPER ACTUALLY USES YOUR TOOL ---
(async () => {
    console.log("Sending task to Omni-Daemon...\n");
    
    // The developer just writes what they want
    const task = "Generate a list of 5 random hex color codes, format them as a JSON array, and print it.";
    
    // One line of code to execute anything asynchronously
    const result = await Omni.run(task);
    
    console.log(`Final Result from Engine:\n${result}`);
})();