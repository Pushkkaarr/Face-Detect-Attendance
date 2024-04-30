import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
import mysql.connector
import subprocess
from tkinter import PhotoImage

class LoginApp:
    def __init__(self, root):
        self.root=root
        # Setting title
        root.title("Login Form")
        root.attributes('-fullscreen', True)  # Open in fullscreen
        root.configure(bg="lightblue")  # Set window background color to light blue

        # Add close and minimize buttons    
        close_button = tk.Button(root, text="Close", command=root.destroy)
        close_button.place(relx=0.9, rely=0, anchor="ne")

        minimize_button = tk.Button(root, text="Minimize", command=root.iconify)
        minimize_button.place(relx=0.85, rely=0, anchor="ne")

        # Set font to Verdana
        font = tkFont.Font(family='Book Antiqua', size=20)
        title_font = tkFont.Font(family='Algerian', size=28) 
        self.icon_image = tk.PhotoImage(file="login.png") 
        label_title = tk.Label(root, text="Faculty Login", font=title_font, bg="blue", fg="white", compound=tk.LEFT, image=self.icon_image)
        label_title.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")
        # Labels with Verdana font
        labels = [
            ("Enter Teacher ID :-", 0.4),
            ("Enter Your Password:-", 0.6)
        ]

        for text, rely_value in labels:
            label = tk.Label(root, text=text, font=font, bg="#ffd700", fg="#cc0000", justify="center")
            label.place(relx=0.1, rely=rely_value, relwidth=0.3, relheight=0.1)

        # Entries and Submit button
        self.entry_teacher_id = tk.Entry(root, font=font)
        self.entry_teacher_id.place(relx=0.45, rely=0.4, relwidth=0.4, relheight=0.1)

        self.entry_password = tk.Entry(root, show="*", font=font)
        self.entry_password.place(relx=0.45, rely=0.6, relwidth=0.4, relheight=0.1)

        submit_button = tk.Button(root, text="Submit", font=font, command=self.check_login)
        submit_button.place(relx=0.9, rely=1.0, anchor="se")

        reg_button = tk.Button(root, text="Want to Register", font=font, command=self.goto_register)
        reg_button.place(relx=0.2, rely=1.0, anchor="se")
        
    def goto_register(self):
        subprocess.call(['python', 'register.py'])
         # Close the current window
        self.root.destroy()

    def check_login(self):
        # Connect to MySQL database
        conn = mysql.connector.connect(
        host="localhost",
            user="root",
            password="MePushkar@sql#193?PW",
            database="faculty"
        )
        cursor = conn.cursor()

        teacher_id = self.entry_teacher_id.get()
        password = self.entry_password.get()

        # Retrieve data from the MySQL table
        query = "SELECT * FROM faculty WHERE teacher_id = %s"
        cursor.execute(query, (teacher_id,))
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror("Error", "Invalid Teacher ID")
        elif result[3] == password:
            messagebox.showinfo("Success", "Login Successful")

            # Close the current window
            root.destroy()

            # Open attendance.py
            subprocess.call(['python', 'attendance.py'])
        else:
            messagebox.showerror("Error", "Incorrect Password")

        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
