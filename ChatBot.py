import tkinter as tk
from tkinter import scrolledtext
from DataBase import initialize_db, save_to_db, get_all_conversations

# Initialize database
initialize_db()


def get_response(user_input):
    # For simplicity, use a placeholder response. Replace with GPT API call if needed.
    return "This is a sample bot response."


def send_message():
    user_input = entry_box.get()
    if user_input.strip():
        chat_area.insert(tk.END, f"You: {user_input}\n")
        entry_box.delete(0, tk.END)

        bot_response = get_response(user_input)
        chat_area.insert(tk.END, f"Bot: {bot_response}\n")

        save_to_db(user_input, bot_response)


def show_conversations():
    conversations = get_all_conversations()
    chat_area.delete(1.0, tk.END)
    for conv in conversations:
        timestamp, user, bot = conv
        chat_area.insert(tk.END, f"{timestamp}\nYou: {user}\nBot: {bot}\n\n")


# Set up Tkinter window
root = tk.Tk()
root.title("AI-Powered Chatbot")
root.geometry("500x600")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Entry box for user input
entry_box = tk.Entry(root)
entry_box.pack(padx=10, pady=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Button to show conversation history
history_button = tk.Button(root, text="Show History", command=show_conversations)
history_button.pack()

root.mainloop()
