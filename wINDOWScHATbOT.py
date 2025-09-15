import tkinter as tk

# Define basic responses
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 😊"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm happy to chat!"
    elif "your name" in user_input:
        return "I'm ChatBot Junior 🤖"
    elif "bye" in user_input:
        return "Goodbye! 👋 Come back soon!"
    else:
        return "I'm still learning. Can you ask something else?"

# Function to send message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_box.insert(tk.END, "You: " + user_input)
    response = get_response(user_input)
    chat_box.insert(tk.END, "Bot: " + response)
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Simple Chatbot")
window.geometry("400x400")
window.config(bg="#e0f7fa")

# Chat display area
chat_box = tk.Listbox(window, height=20, width=50, font=("Arial", 12))
chat_box.pack(pady=10)

# User entry field
entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=10, pady=5)

# Send button
send_button = tk.Button(window, text="Send", width=10, command=send_message, bg="#a0e7e5")
send_button.pack(side=tk.LEFT)

# Start the application
window.mainloop()