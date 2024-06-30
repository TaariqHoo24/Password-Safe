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

        self.password_manager_heading = tk.Label(self.password_manager_frame, text = 'Password Manager', font = ('Arial', 20, 'bold'))
        self.password_manager_heading.grid(row = 0)

        instructions = 'To add password, fill all boxes and click "Add Password"\nTo see your passwords, click "View Password(s)"'

        self.pword_mgr_instructions = tk.Label(self.password_manager_frame, text = instructions, width = 60, justify = 'center', font = ('Arial', 13))  # Instructions text for better usability
        self.pword_mgr_instructions.grid(row = 1)

        self.button_frame = tk.Frame(self.password_manager_frame)   # Seperate frame for buttons, for more organisation
        self.button_frame.grid(row = 2)

        self.add_password_button = tk.Button(self.button_frame, text = 'Add Password', font = ("Arial", 17, "bold"), fg = self.white, bg = self.blue, command = self.add_password)
        self.add_password_button.grid(row = 0, column = 0, padx = '20', pady = '20')

        self.view_passwords = tk.Button(self.button_frame, text = 'View Password(s)', font = ('Arial', 17, 'bold'), fg = self.white, bg = self.orange, state = 'disabled')
        self.view_passwords.grid(row = 0, column = 1, padx = '20', pady = '20')
    # Function to redirect user to password entry window when they click "Add Password"
    def add_password(self):
        root1.destroy()

        root2 = tk.Tk()
        root2.title('Add Password')

        self.password_manager_frame1 = tk.Frame(pady = 10, padx = 10)
        self.password_manager_frame1.grid()

        self.password_manager_heading1 = tk.Label(self.password_manager_frame1, text = 'Add Password', font = ('Arial', 20, 'bold'))
        self.password_manager_heading1.grid(row = 0)

        self.instructions = 'Service: The service you want to store your password for.\nUsername: The name of your account.\nPassword: Series of character or numbers needed to access account.\n'
        
        self.instructions_label = tk.Label(self.password_manager_frame1, text = self.instructions, font = ('Arial', 13))
        self.instructions_label.grid(row = 1)
        
        self.service_label = tk.Label(self.password_manager_frame1, text = 'Service:', font = ('Arial', 17), justify = 'left')
        self.service_label.grid(row = 2, column = 0, pady = 20, padx = 20)

        self.account_label = tk.Label(self.password_manager_frame1, text = 'Account:', font = ('Arial', 17))
        self.account_label.grid(row = 3, column = 0, pady = 20, padx = 20)

        self.password_label = tk.Label(self.password_manager_frame1, text = 'Password:', font = ('Arial', 17))
        self.password_label.grid(row = 4, column = 0, pady = 20,padx = 20)

        root2.mainloop()

root1 = tk.Tk()
password_manager(root1)
root1.mainloop()