import tkinter as tk
from tkinter import messagebox
import random
import string
import tkinter.font as tkFont

# Dictionary to store the mappings
url_mapping = {}

def generate_short_url(long_url):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    
    if short_url in url_mapping:
        return generate_short_url(long_url)
    
    url_mapping[short_url] = long_url
    return short_url

def shorten_url():
    long_url = url_entry.get()
    
    if long_url:
        short_url = generate_short_url(long_url)
        short_url_label.config(text="Short URL: " + short_url)
    else:
        messagebox.showerror("Error", "Please enter a valid URL.")

def redirect_url():
    short_url = redirect_entry.get()
    
    if short_url in url_mapping:
        original_url = url_mapping[short_url]
        messagebox.showinfo("Redirect", f"Original URL: {original_url}")
    else:
        messagebox.showerror("Error", "Short URL not found!")

# Create main application window
app = tk.Tk()
app.title("URL Shortener")

# Configure window size (width x height) and position (optional)
app.geometry("429x335")

app.configure(bg="#f9ce90")  # Set background color of the main window

# Define a custom font
label_font = tkFont.Font(family="Eras Bold ITC", size=12)
button_font = tkFont.Font(family="Eras Bold ITC", size=12)
underlined_font = tkFont.Font(family="Eras Bold ITC", size=13, underline=True)

# Input for Long URL
tk.Label(app, text="Enter Long URL:", font=label_font, bg="#f9ce90").pack(pady=10)
url_entry = tk.Entry(app, width=40, font=label_font, bg="#ffffff")
url_entry.pack(pady=5)

# Button to Shorten URL
shorten_button = tk.Button(app, text="Shorten URL", font=button_font, command=shorten_url, bg="#f9f1da")
shorten_button.pack(pady=10)

# Display Short URL
short_url_label = tk.Label(app, text="", font=underlined_font, bg="#f9ce90")
short_url_label.pack(pady=10)

# Input for Redirect
tk.Label(app, text="Enter Short URL for Redirect:", font=label_font, bg="#f9ce90").pack(pady=10)
redirect_entry = tk.Entry(app, width=40, font=label_font, bg="#ffffff")
redirect_entry.pack(pady=5)

# Button to Redirect
redirect_button = tk.Button(app, text="Redirect to Original URL", font=button_font, command=redirect_url, bg="#f9f1da")
redirect_button.pack(pady=10)

# Run the application
app.mainloop()
