import tkinter as tk
from tkinter import messagebox
import json
import os

class PasswordManager:
    # Add colors to make the UI more accessible
    white = '#FFFFFF'
    red = "#FF0000"
    blue = "#0000FF"
    yellow = "#FFFF00"
    orange = "#FFA500"
    black = "#000000"

    def __init__(self, master):
        # Initialize the Password Manager application
        self.master = master
        master.title('Password Manager')

        self.password_file = "passwords.json"  # File where passwords will be stored
        self.passwords = self.load_passwords()  # Load passwords from file

        self.create_main_window()  # Create main window 
    
    def clear_window(self):
        # Clear all widgets from current window
        for widget in self.master.winfo_children():
            widget.destroy()  # Destroy widgets in window    

    def load_passwords(self):
        # Load passwords from a json file; if there are no files, it will return an empty dictionary
        if os.path.exists(self.password_file):
            with open(self.password_file, 'r') as file:
                return json.load(file)  # Load passwords from json file
        return {}  # Return an empty dictionary if no files are there

    def save_passwords(self):
        # Save the current passwords to a json file
        with open(self.password_file, 'w') as file:
            json.dump(self.passwords, file)  # Save passwords to json file

    def create_main_window(self):
        # Create main window
        self.clear_window()  # Clear existing widgets

        # Create the main frame for the password manager
        self.password_manager_frame = tk.Frame(self.master, pady=10, padx=10)
        self.password_manager_frame.grid()

        # Heading label
        self.password_manager_heading = tk.Label(self.password_manager_frame, text='Password Manager', font=('Arial', 25, 'bold'))
        self.password_manager_heading.grid(row=0)

        # Instructions label
        instructions = 'To add a password, fill all boxes and click "Add Password"\nTo see your passwords, click "View Password(s)"'
        self.pword_mgr_instructions = tk.Label(self.password_manager_frame, text=instructions, width=60, justify='center', font=('Arial', 13))
        self.pword_mgr_instructions.grid(row=1)

        # Frame for buttons
        self.button_frame = tk.Frame(self.password_manager_frame)
        self.button_frame.grid(row=2)

        # "Add Password" button
        self.add_password_button = tk.Button(self.button_frame, text='Add Password', font=("Arial", 17, "bold"), fg=self.white, bg=self.blue, command=self.add_password_window)
        self.add_password_button.grid(row=0, column=0, padx=20, pady=20)

        # "View Password(s)" button
        self.view_passwords_button = tk.Button(self.button_frame, text='View Password(s)', font=('Arial', 17, 'bold'), fg=self.white, bg=self.orange, command=self.view_passwords_window)
        self.view_passwords_button.grid(row=0, column=1, padx=20, pady=20)

    def add_password_window(self):
        # Create new password window
        self.clear_window()  # Clear existing widgets

        # Frame for "Add Password" window
        self.password_manager_frame1 = tk.Frame(self.master, padx=10, pady=10)
        self.password_manager_frame1.grid()

        # Heading label
        self.password_manager_heading1 = tk.Label(self.password_manager_frame1, text='Add Password', font=('Arial', 25, 'bold'))
        self.password_manager_heading1.grid(row=0)

        # Instructions for input fields
        instructions = 'Service: The service you want to store your password for (e.g. Netflix, Google, Bing).\nUsername: The name of your account.\nPassword: Series of characters and numbers needed to access the account.\n\nHow to:\nUpdate passwords: Enter same service name and enter new username/password.\nMultiple accounts for one service: Go with other naming conventions.'
        self.instructions_label = tk.Label(self.password_manager_frame1, text=instructions, font=('Arial', 13))
        self.instructions_label.grid(row=1)

        # Frame for input fields
        self.password_manager_frame2 = tk.Frame(self.password_manager_frame1, padx=10, pady=10)
        self.password_manager_frame2.grid(row=2, column=0)

        # Service input field
        self.service_label = tk.Label(self.password_manager_frame2, text='Service:', font=('Arial', 17))
        self.service_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')
        self.service_entry = tk.Entry(self.password_manager_frame2, font=('Arial', 17), width=30)
        self.service_entry.grid(row=0, column=1, padx=20, pady=20, sticky='w')

        # Username input field
        self.account_username_label = tk.Label(self.password_manager_frame2, text='Username:', font=('Arial', 17))
        self.account_username_label.grid(row=1, column=0, padx=20, pady=20, sticky='w')
        self.account_username_entry = tk.Entry(self.password_manager_frame2, font=('Arial', 17), width=30)
        self.account_username_entry.grid(row=1, column=1)

        # Password input field
        self.password_label = tk.Label(self.password_manager_frame2, text='Password:', font=('Arial', 17))
        self.password_label.grid(row=2, column=0, padx=20, pady=20, sticky='w')
        self.password_entry = tk.Entry(self.password_manager_frame2, font=('Arial', 17), width=30, show='*')  # Password hidden by default
        self.password_entry.grid(row=2, column=1)

        # Show/Hide Password Button
        self.show_password = False
        self.toggle_password_button = tk.Button(self.password_manager_frame2, text='Show Password', font=('Arial', 13), command=self.toggle_password_visibility)
        self.toggle_password_button.grid(row=2, column=2, padx=10, pady=20)

        # Frame for confirm and back buttons
        self.password_manager_frame3 = tk.Frame(self.password_manager_frame1)
        self.password_manager_frame3.grid(row=3, column=0)

        # "Confirm" button to save the password
        self.confirm_button = tk.Button(self.password_manager_frame3, font=('Arial', 17), text='Confirm', justify='center', bg=self.red, fg=self.white, width=42, command=self.save_password)
        self.confirm_button.grid()

        # "Back" button to return to the main window
        self.back_button = tk.Button(self.password_manager_frame3, font=('Arial', 17), text='Back', justify='center', bg=self.yellow, fg=self.black, width=42, command=self.create_main_window)
        self.back_button.grid(pady=10)

    def toggle_password_visibility(self):
        # Toggle the visibility of the password field
        if self.show_password:
            self.password_entry.config(show='*')  # Hide password
            self.toggle_password_button.config(text='Show Password')
        else:
            self.password_entry.config(show='')  # Show password
            self.toggle_password_button.config(text='Hide Password')
        self.show_password = not self.show_password  # Toggle state

    def save_password(self):
        # Save the entered password to the dictionary and json file
        service = self.service_entry.get()
        username = self.account_username_entry.get()
        password = self.password_entry.get()

        if service and username and password:
            self.passwords[service] = (username, password)  # Add password to dictionary
            self.save_passwords()  # Save passwords to json file
            messagebox.showinfo("Success", "Password saved successfully!")
            self.create_main_window()  # Return to main window
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields.")  # Warning if any fields are empty

    def view_passwords_window(self):
        # Create the window layout to view and delete passwords
        self.clear_window()  # Clear existing widgets

        # Frame for the "View Password(s)" window
        self.password_manager_frame1 = tk.Frame(self.master, padx=10, pady=10)
        self.password_manager_frame1.grid()

        if not self.passwords:
            # Show a message if no passwords are saved
            self.no_passwords_label = tk.Label(self.password_manager_frame1, text='No passwords saved.', font=('Arial', 17))
            self.no_passwords_label.grid(row=1, column=1, pady=20)
            row_count = 2  # Ensure the Back button is placed correctly when no passwords are present
        else:
            row_count = 1
            # Display each saved password with a "Delete" button
            for service, credentials in self.passwords.items():
                tk.Label(self.password_manager_frame1, text=f"Service: {service}", font=('Arial', 17)).grid(row=row_count, column=0, padx=20, pady=5, sticky='w')
                tk.Label(self.password_manager_frame1, text=f"Username: {credentials[0]}", font=('Arial', 17)).grid(row=row_count, column=1, padx=20, pady=5, sticky='w')
                tk.Label(self.password_manager_frame1, text=f"Password: {credentials[1]}", font=('Arial', 17)).grid(row=row_count, column=2, padx=20, pady=5, sticky='w')

                # "Delete" button for each password
                delete_button = tk.Button(self.password_manager_frame1, text="Delete", font=('Arial', 13), fg=self.white, bg=self.red, command=lambda s=service: self.delete_password(s))
                delete_button.grid(row=row_count, column=3, padx=10, pady=5)
                
                row_count += 1

        # "Back" button to return to the main window
        self.back_button = tk.Button(self.password_manager_frame1, font=('Arial', 17), text='Back', justify='center', bg=self.yellow, fg=self.black, width=20, command=self.create_main_window)
        self.back_button.grid(row=row_count, column=0, columnspan=4, pady=20)

    def delete_password(self, service):
        # Delete a specific password after confirming with the user
        confirm = messagebox.askyesno("Delete Password", f"Are you sure you want to delete the password for {service}?")
        if confirm:
            del self.passwords[service]  # Remove the password from the dictionary
            self.save_passwords()  # Update the json file
            messagebox.showinfo("Deleted", f"The password for {service} has been deleted.")
            self.view_passwords_window()  # Refresh the view passwords window

# Initialize and run the application
root = tk.Tk()
password_manager = PasswordManager(root)
root.mainloop()