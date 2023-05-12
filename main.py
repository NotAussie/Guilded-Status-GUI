# Import tkinter for GUI
import tkinter as tk

# Import requests for sending messages
import requests; from requests.structures import CaseInsensitiveDict

# Import traceback
import traceback

# Define a function to validate the message length
def validate_message():
    # Get the message from the entry widget
    message = message_entry.get()

    # Check if the message is longer than 100 characters
    if len(message) > 100:
        # Display an error message on the GUI
        status_label.config(text="Message is too long!", fg="red")
        return False
    else:
        # Return True if the message is valid
        return True

# Define a function to send a message using bot id and token
def send_message():
    # Get the values from the entry widgets
    bot_id = bot_id_entry.get()
    bot_token = bot_token_entry.get()
    message = message_entry.get()
    id = id_entry.get()

    # Validate the message length
    if validate_message():
       try: 
        # Construct the URL for sending messages
        url = f"https://www.guilded.gg/api/v1/users/{bot_id}/status"

        # Construct the data for sending messages
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {bot_token}"
        headers["Accept"] = "application/json"
        headers["Content-type"] = "application/json"

        # Construct the data for sending messages
        data = {"content": message, "emoteId": id}

        # Send a POST request to the URL with the data
        resp = requests.put(url, headers=headers, json=data)

        status_label.config(text="Status sent successfully!", fg="green")

       except Exception as e:
        status_label.config(text="Status failed to send!", fg="red")
            

# Create a root window for the GUI
root = tk.Tk()

# Create a title for the GUI
root.title("Simple Bot Status")

# Create four labels for the inputs
bot_id_label = tk.Label(root, text="Bot User ID:")
bot_token_label = tk.Label(root, text="Bot Token:")
message_label = tk.Label(root, text="Message:")
id_label = tk.Label(root, text="ID:")

# Create four entry widgets for the inputs
bot_id_entry = tk.Entry(root)
bot_token_entry = tk.Entry(root, show="*")
message_entry = tk.Entry(root)
id_entry = tk.Entry(root)

# Create a button widget for sending messages
send_button = tk.Button(root, text="Send", command=send_message)

# Create a label widget for displaying the status of sending messages
status_label = tk.Label(root, text="")

# Arrange the widgets on a grid layout
bot_id_label.grid(row=0, column=0, sticky=tk.E)
bot_token_label.grid(row=1, column=0, sticky=tk.E)
message_label.grid(row=2, column=0, sticky=tk.E)
id_label.grid(row=3, column=0, sticky=tk.E)
bot_id_entry.grid(row=0, column=1)
bot_token_entry.grid(row=1, column=1)
message_entry.grid(row=2, column=1)
id_entry.grid(row=3, column=1)
send_button.grid(row=4, column=0, columnspan=2)
status_label.grid(row=5, column=0, columnspan=2)

# Start the main loop of the GUI
root.mainloop()

# Made with love by Guilded.gg/u/NotAussie <3
