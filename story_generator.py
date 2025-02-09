import tkinter as tk
from tkinter import filedialog, scrolledtext
import markovify
import pyttsx3



def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, encoding='utf-8') as f:
            text = f.read()
        return text
    return None


def generate_story():
    text = open_file()
    if text:
        text_model = markovify.Text(text)

        generated_story = ""
        while len(generated_story.split()) < 1000:
            new_sentence = text_model.make_sentence()
            if new_sentence:
                generated_story += " " + new_sentence

        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, generated_story)

        original_text.delete(1.0, tk.END)  # Clear previous text
        original_text.insert(tk.END, text)

def save_story():
    generated_story = result_text.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generated_story)

def regenerate_story():
    text_model = markovify.Text(original_text.get(1.0, tk.END))
    
    generated_story = ""
    while len(generated_story.split()) < 1000:
        new_sentence = text_model.make_sentence()
        if new_sentence:
            generated_story += " " + new_sentence

    result_text.delete(1.0, tk.END)  # Clear previous text
    result_text.insert(tk.END, generated_story)

def speak_generated_story():
    generated_story = result_text.get(1.0, tk.END)
    engine = pyttsx3.init()
    engine.say(generated_story)
    engine.runAndWait()


# Create window
window = tk.Tk()
window.title("Markov Story Generator")
window.geometry("800x600")  # Set the window size to 800x600

# Styling
window.configure(bg="#f0f0f0")
open_button = tk.Button(window, text="Open File", command=generate_story, bg="#4CAF50", fg="white", font=("Arial", 12))
open_button.pack(pady=10, padx=10)

original_label = tk.Label(window, text="Original Text", font=("Arial", 14), bg="#f0f0f0")
original_label.pack(pady=10)

original_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
original_text.pack(padx=10, pady=10)

generate_label = tk.Label(window, text="Generated Story", font=("Arial", 14), bg="#f0f0f0")
generate_label.pack(pady=10)

result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
result_text.pack(padx=10, pady=10)

save_button = tk.Button(window, text="Save", command=save_story, bg="#008CBA", fg="white", font=("Arial", 12))
save_button.pack(side=tk.RIGHT, pady=10)

regenerate_button = tk.Button(window, text="Re-generate", command=regenerate_story, bg="#FFD700", font=("Arial", 12))
regenerate_button.pack(side=tk.RIGHT, padx=5, pady=10)

speak_button = tk.Button(window, text="Speak", command=speak_generated_story, bg="#FFA500", font=("Arial", 12))
speak_button.pack(side=tk.RIGHT, padx=5, pady=10)



# Run the GUI
window.mainloop()
