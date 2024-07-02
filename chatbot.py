import tkinter as tk
from tkinter import scrolledtext

# Define the chatbot response function
def respond(input_text):
    input_text = input_text.lower()

    if 'weather' in input_text:
        return "The weather is sunny and warm today."

    elif 'time' in input_text:
        return "The current time is 3:00 PM."

    elif 'greeting' in input_text or 'hello' in input_text or 'hi' in input_text:
        return "Hello! How can I assist you today?"

    elif 'thanks' in input_text or 'thank you' in input_text:
        return "You're welcome!"

    elif 'who are you' in input_text or 'your name' in input_text:
        return "I'm a friendly chatbot here to help you with information."

    elif 'joke' in input_text:
        return "Why don't scientists trust atoms? Because they make up everything!"

    else:
        return "I'm sorry, I don't have information on that topic. How can I help you otherwise?"

# Define the function to handle user input and display responses
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() != "":
        chat_history.configure(state=tk.NORMAL)
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        chat_history.configure(state=tk.DISABLED)

        response = respond(user_input)
        chat_history.configure(state=tk.NORMAL)
        chat_history.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_history.configure(state=tk.DISABLED)

        user_entry.delete(0, tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a scrolled text widget to display chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
chat_history.configure(state=tk.DISABLED)
chat_history.pack(padx=10, pady=10)

# Create an entry widget for user input
user_entry = tk.Entry(root, width=50)
user_entry.bind("<Return>", send_message)
user_entry.pack(padx=10, pady=10)

# Create a button to send user input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Start the main loop of the GUI
root.mainloop()