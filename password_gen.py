# importing the random and tkinter modules
import random
import tkinter as tk


# create main function
def generate_passwords():
    num_passwords = int(num_passwords_entry.get())

    if num_passwords > 0:
        passwords = []
        for _ in range(num_passwords):
            password = random_password()
            passwords.append(password)

        password_text.delete(1.0, tk.END)  # Clear previous passwords
        password_text.insert(tk.END, "\n".join(passwords))
    else:
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, "Please enter a number greater than 0")


# create a function for random password
def random_password():
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    )
    password_length = 14
    password = ""
    for _ in range(password_length):
        password += random.choice(characters)
    return password


# Create the main Tkinter window
window = tk.Tk()  # create the tkinter window
window.title("Password Generator")

# Create and place the labels and entry fields
num_passwords_label = tk.Label(window, text="Number of passwords:")
num_passwords_label.pack()  # pack() method:It organizes the widgets in blocks before placing in the parent widget.

num_passwords_entry = tk.Entry(window)
num_passwords_entry.pack()

# Create the button to generate passwords
generate_button = tk.Button(
    window, text="Generate Passwords", command=generate_passwords
)
generate_button.pack()

# Create the text widget to display the passwords
password_text = tk.Text(window, height=10, width=40)
password_text.pack()

# Start the Tkinter event loop
window.mainloop()  # used when application is ready to run


# ref
# https://www.geeksforgeeks.org/python-gui-tkinter/
# https://docs.python.org/3/library/tkinter.html
# https://support.microsoft.com/en-us/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb#:~:text=A%20strong%20password%20is%3A,character%2C%20product%2C%20or%20organization.
