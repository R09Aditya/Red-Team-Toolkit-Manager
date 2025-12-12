import tkinter as tk
from tkinter import messagebox
import mysql.connector as sqltor
from dashboard import open_dashboard

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

def login_user():
    uname = entry_username.get()
    pwd = entry_password.get()

    query = "SELECT * FROM users WHERE uname=%s AND password=%s"
    mycur.execute(query, (uname, pwd))
    row = mycur.fetchone()

    if row:
        uid = row[0]
        username = row[1]
        name = row[2]
        messagebox.showinfo("Success", f"Login successful! Welcome {name}")
        root.withdraw()
        open_dashboard(row[1], row[2])
    else:
        messagebox.showerror("Error", "Invalid username or password")

def signup_user():
    uname = sentry_username.get()
    pwd = sentry_password.get()
    name = entry_name.get()
    email = entry_email.get()

    if not uname or not pwd or not name or not email:
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    query = "INSERT INTO users (uname, name, email, password) VALUES (%s, %s, %s, %s)"
    
    try:
        mycur.execute(query, (uname, name, email, pwd))
        mycon.commit()
        messagebox.showinfo("Success", "Signup successful!")
        switch_to_login()
    except Exception as e:
        messagebox.showerror("Error", f"Signup failed: {e}")

def switch_to_signup():
    login_frame.pack_forget()
    signup_frame.pack(expand=True)

def switch_to_login():
    signup_frame.pack_forget()
    login_frame.pack(expand=True)

root = tk.Tk()
root.title("RTTM - Login System")
root.state("zoomed") 
root.configure(bg="#0f0f0f") 

BG = "#0f0f0f"
FG = "#00ff88"
ENTRY_BG = "#1c1c1c"
BUTTON_BG = "#00ff88"
BUTTON_FG = "black"

login_frame = tk.Frame(root, bg=BG)
login_frame.pack(expand=True)

tk.Label(login_frame, text="LOGIN",
         font=("Segoe UI", 26, "bold"),
         bg=BG, fg=FG).pack(pady=20)

tk.Label(login_frame, text="Username:", bg=BG, fg=FG,
         font=("Segoe UI", 12)).pack()
entry_username = tk.Entry(login_frame, width=35,
                          bg=ENTRY_BG, fg=FG,
                          insertbackground=FG,
                          font=("Segoe UI", 11))
entry_username.pack(pady=8)

tk.Label(login_frame, text="Password:", bg=BG, fg=FG,
         font=("Segoe UI", 12)).pack()
entry_password = tk.Entry(login_frame, width=35, show="*",
                          bg=ENTRY_BG, fg=FG,
                          insertbackground=FG,
                          font=("Segoe UI", 11))
entry_password.pack(pady=8)

tk.Button(login_frame, text="Login",
          width=20, height=1,
          bg=BUTTON_BG, fg=BUTTON_FG,
          font=("Segoe UI", 12, "bold"),
          command=login_user).pack(pady=15)

tk.Button(login_frame, text="No account? Signup",
          bg=BG, fg=FG,
          font=("Segoe UI", 10, "underline"),
          bd=0,
          command=switch_to_signup).pack(pady=5)

signup_frame = tk.Frame(root, bg=BG)

tk.Label(signup_frame, text="SIGN UP",
         font=("Segoe UI", 26, "bold"),
         bg=BG, fg=FG).pack(pady=20)

tk.Label(signup_frame, text="Full Name:", bg=BG, fg=FG).pack()
entry_name = tk.Entry(signup_frame, width=35, bg=ENTRY_BG, fg=FG,
                      insertbackground=FG)
entry_name.pack(pady=8)

tk.Label(signup_frame, text="Email:", bg=BG, fg=FG).pack()
entry_email = tk.Entry(signup_frame, width=35, bg=ENTRY_BG, fg=FG,
                       insertbackground=FG)
entry_email.pack(pady=8)

tk.Label(signup_frame, text="Username:", bg=BG, fg=FG).pack()
sentry_username = tk.Entry(signup_frame, width=35, bg=ENTRY_BG, fg=FG,
                           insertbackground=FG)
sentry_username.pack(pady=8)

tk.Label(signup_frame, text="Password:", bg=BG, fg=FG).pack()
sentry_password = tk.Entry(signup_frame, width=35, show="*",
                           bg=ENTRY_BG, fg=FG,
                           insertbackground=FG)
sentry_password.pack(pady=8)

tk.Button(signup_frame, text="Signup",
          width=20, height=1,
          bg=BUTTON_BG, fg=BUTTON_FG,
          font=("Segoe UI", 12, "bold"),
          command=signup_user).pack(pady=15)

tk.Button(signup_frame, text="Already have an account? Login",
          bg=BG, fg=FG,
          font=("Segoe UI", 10, "underline"),
          bd=0,
          command=switch_to_login).pack(pady=5)

root.mainloop()
