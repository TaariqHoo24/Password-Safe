import tkinter as tk

class password_manager:

    white = '#FFFFFF'
    red = "#FF0000"
    blue = "#0000FF"
    yellow = "#FFFF00"
    orange = "#FFA500"

    def __init__(self, master):
        self.master = master
        master.title('Password Manager')

        self.password_manager_frame = tk.Frame(pady = 10, padx = 10)
        self.password_manager_frame.grid()

        self.password_manager_heading = tk.Label(self.password_manager_frame, text = 'Password Manager', font = ('Arial', 20, 'bold'))
        self.password_manager_heading.grid(row = 0)

        instructions = 'To add password, fill all entry boxes and press "Add Password"\nTo see passwords, enter Account Name and press "See Passwords"'

        self.pword_mgr_instructions = tk.Label(self.password_manager_frame, text = instructions, width = 60, justify = 'center', font = ('Arial', 13))
        self.pword_mgr_instructions.grid(row = 1)

        self.button_frame = tk.Frame(self.password_manager_frame)
        self.button_frame.grid(row = 2)

        self.add_password_button = tk.Button(self.button_frame, text = 'Add Password', font = ("Arial", 17, "bold"), fg = self.white, bg = self.blue)
        self.add_password_button.grid(row = 0, column = 0, padx = '20', pady = '20')

        self.view_passwords = tk.Button(self.button_frame, text = 'View Password', font = ('Arial', 17, 'bold'), fg = self.white, bg = self.orange)
        self.view_passwords.grid(row = 0, column = 1, padx = '20', pady = '20')

root = tk.Tk()
password_manager(root)
root.mainloop()