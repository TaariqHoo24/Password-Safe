import tkinter as tk

class password_manager:
    # Add colours to accommodate people who happen to be colour blind
    white = '#FFFFFF'
    red = "#FF0000"
    blue = "#0000FF"
    yellow = "#FFFF00"
    orange = "#FFA500"
    # Create main window
    def __init__(self, master):
        self.master = master
        master.title('Password Manager')

        self.password_manager_frame = tk.Frame(pady = 10, padx = 10)    # Main text gets put in this frame
        self.password_manager_frame.grid()

        self.password_manager_heading = tk.Label(self.password_manager_frame, text = 'Password Manager', font = ('Arial', 25, 'bold'))
        self.password_manager_heading.grid(row = 0)

        instructions = 'To add password, fill all boxes and click "Add Password"\nTo see your passwords, click "View Password(s)"'

        self.pword_mgr_instructions = tk.Label(self.password_manager_frame, text = instructions, width = 60, justify = 'center', font = ('Arial', 13))  # Instructions text for better usability
        self.pword_mgr_instructions.grid(row = 1)

        self.button_frame = tk.Frame(self.password_manager_frame)   # Seperate frame for buttons, for more organisation
        self.button_frame.grid(row = 2)

        self.add_password_button = tk.Button(self.button_frame, text = 'Add Password', font = ("Arial", 17, "bold"), fg = self.white, bg = self.blue, command = self.add_password)
        self.add_password_button.grid(row = 0, column = 0, padx = '20', pady = '20')

        self.view_passwords_button = tk.Button(self.button_frame, text = 'View Password(s)', font = ('Arial', 17, 'bold'), fg = self.white, bg = self.orange, command = self.view_passwords, state = 'disabled')
        self.view_passwords_button.grid(row = 0, column = 1, padx = '20', pady = '20')
    # Function to redirect user to password entry window when they click "Add Password"
    def add_password(self):
        root1.destroy()

        root2 = tk.Tk()
        root2.title('Add Password')

        self.password_manager_frame1 = tk.Frame(padx = 10, pady = 10)
        self.password_manager_frame1.grid()

        self.password_manager_heading1 = tk.Label(self.password_manager_frame1, text = 'Add Password', font = ('Arial', 25, 'bold'))
        self.password_manager_heading1.grid(row = 0)

        self.instructions = 'Service: The service you want to store your password for (e.g. Netflix, Google, Bing).\nUsername: The name of your account.\nPassword: Series of characters and numbers needed to access account.\n'

        self.password_manager_frame2 = tk.Frame(padx = 10, pady = 10)
        self.password_manager_frame2.grid(row = 1, column = 0)

        self.instructions_label = tk.Label(self.password_manager_frame1, text = self.instructions, font = ('Arial', 13))
        self.instructions_label.grid(row = 1)

        self.service_label = tk.Label(self.password_manager_frame2, text = 'Service:', font = ('Arial', 17))
        self.service_label.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'w')
        self.service_entry = tk.Entry(self.password_manager_frame2, font = ('Arial', 17), width = 30)
        self.service_entry.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'w')

        self.account_username_label = tk.Label(self.password_manager_frame2, text = 'Username:', font = ('Arial', 17))
        self.account_username_label.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = 'w')
        self.account_username_entry = tk.Entry(self.password_manager_frame2, font = ('Arial', 17), width = 30)
        self.account_username_entry.grid(row = 1, column = 1)

        self.password_label = tk.Label(self.password_manager_frame2, text = 'Password:', font = ('Arial', 17))
        self.password_label.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = 'w')
        self.password_entry = tk.Entry(self.password_manager_frame2, font = ('Arial', 17), width = 30)
        self.password_entry.grid(row = 2, column = 1)

        self.password_manager_frame3 = tk.Frame()
        self.password_manager_frame3.grid()

        self.confirm_button = tk.Button(self.password_manager_frame3, font = ('Arial', 17), text = 'Confirm', justify = 'center', bg = self.red, fg = self.white, width = 42)
        self.confirm_button.grid()

        root2.mainloop()

    def view_passwords(self):
        root1.destroy()

        root3 = tk.Tk()
        root3.title('View Passwords')

        self.view_passwords_frame = tk.Frame(padx = 10, pady = 10)
        self.view_passwords_frame.grid()

        self.view_passwords_heading = tk.Label(self.view_passwords_frame, text = 'View Passwords', font = ('Arial', 25, 'bold'))
        self.view_passwords_heading.grid(padx = 10, pady = 10)

        root3.mainloop()

root1 = tk.Tk()
password_manager(root1)
root1.mainloop()