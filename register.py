import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
import tkinter.messagebox as messagebox
import subprocess
import mysql.connector

class App:
    def __init__(self, root):
        # Setting title
        self.root=root
        root.title("Register Form")
        root.attributes('-fullscreen', True)  # Open in fullscreen
        

        root.configure(bg="#ff871f")  # Set window background color to green
        

        # Add close and minimize buttons
        close_button = tk.Button(root, text="Close", command=root.destroy)
        close_button.place(relx=0.9, rely=0, anchor="ne")

        minimize_button = tk.Button(root, text="Minimize", command=root.iconify)
        minimize_button.place(relx=0.85, rely=0, anchor="ne")

        # Set font to Verdana
        font = tkFont.Font(family='Book Antiqua', size=20)

        # Add label in the center at the top with an image icon
        title_font = tkFont.Font(family='Algerian', size=28) 
        self.icon_image = tk.PhotoImage(file="register.png")  
        label_title = tk.Label(root, text="Faculty Registration Form", font=title_font, bg="#4d4dff", fg="white", compound=tk.LEFT,image=self.icon_image)
        label_title.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")

        # Labels with Verdana font
        labels = [
            ("Enter Teacher Name :-", 0.2),
            ("Enter Your Mob no :-", 0.4),
            ("Enter Teacher ID :-", 0.6),        
            ("Enter Your Password:-", 0.8)
        ]

        for text, rely_value in labels:
            label = tk.Label(root, text=text, font=font, bg="#ff80bf", fg="#000099", justify="center")
            label.place(relx=0.1, rely=rely_value, relwidth=0.3, relheight=0.1)

        # Entries and Submit button
        self.entry_name = tk.Entry(root, font=font)
        self.entry_name.place(relx=0.45, rely=0.2, relwidth=0.4, relheight=0.1)

        self.entry_teacher_id = tk.Entry(root, font=font)
        self.entry_teacher_id.place(relx=0.45, rely=0.4, relwidth=0.4, relheight=0.1)

        self.entry_mob_no = tk.Entry(root, font=font)
        self.entry_mob_no.place(relx=0.45, rely=0.6, relwidth=0.4, relheight=0.1)

        self.entry_password = tk.Entry(root, show="*", font=font)
        self.entry_password.place(relx=0.45, rely=0.8, relwidth=0.4, relheight=0.1)

        submit_button = tk.Button(root, text="Submit", font=font, command=self.submit_data)
        submit_button.place(relx=0.9, rely=1.0, anchor="se")

        reg_button = tk.Button(root, text="Back to Login", font=font, command=self.goto_submit)
        reg_button.place(relx=0.2, rely=1.0, anchor="se")

    def goto_submit(self):
        subprocess.call(['python', 'login.py'])
         # Close the current window
        self.root.destroy()

    def submit_data(self):
        # Data validation
        if not all([self.entry_name.get(), self.entry_teacher_id.get(), self.entry_mob_no.get(), self.entry_password.get()]):
              messagebox.showerror("Error", "Please fill in all the fields")
              return

        if any(char.isdigit() for char in self.entry_name.get()):
            messagebox.showerror("Error", "Name cannot contain numbers")
            return

        if len(self.entry_mob_no.get()) != 10:
            messagebox.showerror("Error", "Mobile number should be 10 characters")
            return

        if not self.entry_teacher_id.get().isdigit() or len(self.entry_teacher_id.get()) != 5:
            messagebox.showerror("Error", "Teacher ID should be 5 characters and contain only numbers")
            return

        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MePushkar@sql#193?PW",
            database="faculty"
        )
        cursor = conn.cursor()

        # Insert data into the MySQL database
        data = (self.entry_name.get(), self.entry_teacher_id.get(), self.entry_mob_no.get(), self.entry_password.get())
        cursor.execute('INSERT INTO faculty (name, teacher_id, mob_no, password) VALUES (%s, %s, %s, %s)', data)

        conn.commit()
        conn.close()

        # Show popup message
        messagebox.showinfo("Success", f"Faculty saved with Teacher ID: {self.entry_teacher_id.get()}")

        # Close the current window
        root.destroy()

        # Open login.py
        subprocess.call(['python', 'login.py'])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
