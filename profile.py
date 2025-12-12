import tkinter as tk
from tkinter import messagebox
import mysql.connector as sqltor
try:
    mycon = sqltor.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="RTTM"
    )
    mycur = mycon.cursor()
except Exception as e:
    print("Database connection failed:", e)
    exit()

def open_profile(username):

    profile = tk.Toplevel()
    profile.title("User Profile")
    profile.state("zoomed")          # FULL SCREEN
    profile.config(bg="#0F0F0F")

    # Make responsive grid
    profile.columnconfigure(0, weight=1)
    profile.rowconfigure(5, weight=1)

    # Fetch current details
    query = "SELECT name, email, uname, password FROM users WHERE uname=%s"
    mycur.execute(query, (username,))
    row = mycur.fetchone()

    if not row:
        messagebox.showerror("Error", "User not found!")
        profile.destroy()
        return

    name_var = tk.StringVar(value=row[0])
    email_var = tk.StringVar(value=row[1])
    uname_var = tk.StringVar(value=row[2])
    pwd_var = tk.StringVar(value=row[3])

    # -------------------------------
    # PAGE TITLE (CENTERED)
    # -------------------------------
    tk.Label(
        profile,
        text="Edit Profile",
        font=("Segoe UI", 30, "bold"),
        bg="#0F0F0F",
        fg="#00E1FF"
    ).grid(row=0, column=0, pady=30)

    # -------------------------------
    # FORM FRAME (CENTERED)
    # -------------------------------
    form = tk.Frame(profile, bg="#0F0F0F")
    form.grid(row=1, column=0, pady=20)

    for i in range(2):
        form.columnconfigure(i, weight=1)

    # Reusable field generator
    def field(label, var, row):
        tk.Label(
            form, text=label,
            font=("Segoe UI", 14),
            fg="white", bg="#0F0F0F"
        ).grid(row=row, column=0, padx=20, pady=12, sticky="e")

        entry = tk.Entry(
            form,
            textvariable=var,
            font=("Segoe UI", 13),
            width=32,
            bg="#1E1E1E",
            fg="white",
            insertbackground="white"
        )
        entry.grid(row=row, column=1, padx=20, pady=12, sticky="w")

    # Fields
    field("Name:", name_var, 0)
    field("Email:", email_var, 1)
    field("Username:", uname_var, 2)
    field("Password:", pwd_var, 3)

    # -------------------------------
    # SAVE BUTTON (CENTERED)
    # -------------------------------
    def save_changes():
        new_name = name_var.get()
        new_email = email_var.get()
        new_uname = uname_var.get()
        new_pwd = pwd_var.get()

        update_query = """
        UPDATE users SET name=%s, email=%s, uname=%s, password=%s WHERE uname=%s
        """

        try:
            mycur.execute(update_query, (new_name, new_email, new_uname, new_pwd, username))
            mycon.commit()
            messagebox.showinfo("Success", "Profile updated successfully!")
            profile.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {e}")

    tk.Button(
        profile,
        text="Save Changes",
        font=("Segoe UI", 16, "bold"),
        bg="#00E1FF",
        fg="black",
        width=20,
        height=2,
        command=save_changes
    ).grid(row=4, column=0, pady=40)
