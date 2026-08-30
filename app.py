import tkinter as tk
from tkinter import scrolledtext
from brain import synthesize_code
from sandbox import run_in_sandbox

def run_task():
    intent = text_input.get("1.0", tk.END).strip()
    if not intent:
        return
    
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, "Synthesizing code and executing in sandbox...\n")
    root.update()
    
    try:
        # Phase A & B: Brain + Sandbox
        generated_code = synthesize_code(intent)
        result = run_in_sandbox(generated_code)
        
        output_display.delete("1.0", tk.END)
        if result["status"] == "success":
            output_display.insert(tk.END, result["output"])
        else:
            output_display.insert(tk.END, f"Error:\n{result['output']}")
    except Exception as e:
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, f"Execution Error: {str(e)}")

# Build Native Desktop Window
root = tk.Tk()
root.title("Omni-Daemon Native Studio")
root.geometry("800x600")
root.configure(bg="#090d16")

# Title Label
title_label = tk.Label(root, text="OMNI-DAEMON STUDIO", fg="#10b981", bg="#090d16", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Input Box Frame
input_frame = tk.Frame(root, bg="#111827", bd=1, relief="solid")
input_frame.pack(fill="x", padx=20, pady=10)

tk.Label(input_frame, text="Enter Task Intent:", fg="#9ca3af", bg="#111827", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
text_input = tk.Text(input_frame, height=4, bg="#090d16", fg="#f3f4f6", insertbackground="white", font=("Courier", 11))
text_input.pack(fill="x", padx=10, pady=5)

btn = tk.Button(input_frame, text="Synthesize & Execute", bg="#10b981", fg="black", font=("Arial", 11, "bold"), command=run_task)
btn.pack(anchor="e", padx=10, pady=10)

# Output Box Frame
output_frame = tk.Frame(root, bg="#111827", bd=1, relief="solid")
output_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(output_frame, text="Sandbox Console Output", fg="#9ca3af", bg="#111827", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
output_display = scrolledtext.ScrolledText(output_frame, bg="#05070c", fg="#10b981", insertbackground="white", font=("Courier", 11))
output_display.pack(fill="both", expand=True, padx=10, pady=5)
output_display.insert(tk.END, "System idle. Waiting for task intent...")

root.mainloop()