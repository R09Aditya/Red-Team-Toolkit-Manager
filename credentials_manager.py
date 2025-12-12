import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="RTTM"
    )

def open_credentials_manager(dashboard):
    win = tk.Toplevel()
    win.title("Credentials Manager")
    win.state("zoomed")  # FULLSCREEN
    win.configure(bg="#0f0f0f")

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(3, weight=1)

    def go_back():
        win.destroy()
        dashboard.deiconify()

    tk.Button(
        win, text="← Back", command=go_back,
        font=("Segoe UI", 12, "bold"),
        bg="#ff4444", fg="white"
    ).grid(row=0, column=1, sticky="e", padx=20, pady=20)

    tk.Label(
        win, text="Credentials Manager",
        font=("Segoe UI", 26, "bold"),
        bg="#0f0f0f", fg="#00ff88"
    ).grid(row=0, column=0, pady=10)

    form_frame = tk.Frame(win, bg="#0f0f0f")
    form_frame.grid(row=1, column=0, columnspan=2, pady=20)

    for i in range(2):
        form_frame.columnconfigure(i, weight=1)

    tk.Label(form_frame, text="Service / Website:", bg="#0f0f0f", fg="white").grid(row=0, column=0, sticky="e", pady=5)
    tk.Label(form_frame, text="Username:", bg="#0f0f0f", fg="white").grid(row=1, column=0, sticky="e", pady=5)
    tk.Label(form_frame, text="Password:", bg="#0f0f0f", fg="white").grid(row=2, column=0, sticky="e", pady=5)
    tk.Label(form_frame, text="Notes:", bg="#0f0f0f", fg="white").grid(row=3, column=0, sticky="e", pady=5)

    service_entry = tk.Entry(form_frame, width=50)
    username_entry = tk.Entry(form_frame, width=50)
    password_entry = tk.Entry(form_frame, width=50, show="*")
    notes_entry = tk.Entry(form_frame, width=50)

    service_entry.grid(row=0, column=1, pady=5)
    username_entry.grid(row=1, column=1, pady=5)
    password_entry.grid(row=2, column=1, pady=5)
    notes_entry.grid(row=3, column=1, pady=5)

    def toggle_password():
        if password_entry.cget("show") == "*":
            password_entry.config(show="")
            toggle_btn.config(text="Hide")
        else:
            password_entry.config(show="*")
            toggle_btn.config(text="Show")

    toggle_btn = tk.Button(form_frame, text="Show", command=toggle_password,
                           bg="#00ff88", fg="black")
    toggle_btn.grid(row=2, column=2, padx=10)

    def add_credential():
        service = service_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        notes = notes_entry.get()

        if service == "" or username == "" or password == "":
            messagebox.showerror("Error", "Service, Username, and Password are required.")
            return

        db = connect_db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO credentials_manager(service, username, password, notes)
            VALUES (%s, %s, %s, %s)
        """, (service, username, password, notes))

        db.commit()
        cursor.close()
        db.close()

        load_credentials()
        service_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        notes_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Credential added successfully!")

    tk.Button(
        win, text="Add Credential", command=add_credential,
        font=("Segoe UI", 12, "bold"),
        bg="#00ff88", fg="black", width=20
    ).grid(row=2, column=0, columnspan=2, pady=10)

    table_frame = tk.Frame(win, bg="#0f0f0f")
    table_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=30, pady=10)

    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    tree = ttk.Treeview(
        table_frame,
        columns=("ID", "Service", "Username", "Password", "Notes"),
        show="headings"
    )

    style = ttk.Style()
    style.configure("Treeview", background="#1a1a1a", foreground="white", rowheight=28, fieldbackground="#1a1a1a")
    style.map("Treeview", background=[("selected", "#00ff88")], foreground=[("selected", "black")])

    tree.heading("ID", text="ID")
    tree.heading("Service", text="Service")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")
    tree.heading("Notes", text="Notes")

    tree.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    def load_credentials():
        for item in tree.get_children():
            tree.delete(item)

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM credentials_manager")
        data = cursor.fetchall()

        for row in data:
            tree.insert("", tk.END, values=row)

        cursor.close()
        db.close()

    load_credentials()

    def delete_credential():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        record = tree.item(selected, "values")[0]

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM credentials_manager WHERE id=%s", (record,))
        db.commit()
        cursor.close()
        db.close()

        load_credentials()
        messagebox.showinfo("Deleted", "Credential deleted successfully!")

    tk.Button(
        win, text="Delete Selected", command=delete_credential,
        font=("Segoe UI", 12, "bold"),
        bg="#ff4444", fg="white", width=20
    ).grid(row=4, column=0, pady=10)

    def update_credential():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a record to update")
            return

        values = tree.item(selected, "values")
        cred_id, old_service, old_user, old_pass, old_notes = values

        upd = tk.Toplevel(win)
        upd.title("Update Credential")
        upd.geometry("450x350")
        upd.configure(bg="#0f0f0f")
        upd.grab_set()

        tk.Label(upd, text="Update Credential",
                 font=("Segoe UI", 16, "bold"),
                 bg="#0f0f0f", fg="#00ff88").pack(pady=10)

        form_u = tk.Frame(upd, bg="#0f0f0f")
        form_u.pack(pady=10)

        tk.Label(form_u, text="Service:", bg="#0f0f0f", fg="white").grid(row=0, column=0, pady=5)
        tk.Label(form_u, text="Username:", bg="#0f0f0f", fg="white").grid(row=1, column=0, pady=5)
        tk.Label(form_u, text="Password:", bg="#0f0f0f", fg="white").grid(row=2, column=0, pady=5)
        tk.Label(form_u, text="Notes:", bg="#0f0f0f", fg="white").grid(row=3, column=0, pady=5)

        su = tk.Entry(form_u, width=35)
        uu = tk.Entry(form_u, width=35)
        pu = tk.Entry(form_u, width=35, show="*")
        nu = tk.Entry(form_u, width=35)

        su.insert(0, old_service)
        uu.insert(0, old_user)
        pu.insert(0, old_pass)
        nu.insert(0, old_notes)

        su.grid(row=0, column=1, pady=5)
        uu.grid(row=1, column=1, pady=5)
        pu.grid(row=2, column=1, pady=5)
        nu.grid(row=3, column=1, pady=5)

        def save_u():
            db = connect_db()
            cursor = db.cursor()

            cursor.execute("""
                UPDATE credentials_manager
                SET service=%s, username=%s, password=%s, notes=%s
                WHERE id=%s
            """, (su.get(), uu.get(), pu.get(), nu.get(), cred_id))

            db.commit()
            cursor.close()
            db.close()

            upd.destroy()
            load_credentials()
            messagebox.showinfo("Updated", "Credential updated successfully!")

        tk.Button(
            upd, text="Save Changes", command=save_u,
            bg="#00ff88", fg="black", width=20
        ).pack(pady=15)

    tk.Button(
        win, text="Update Selected", command=update_credential,
        font=("Segoe UI", 12, "bold"),
        bg="#ffaa00", fg="black", width=20
    ).grid(row=4, column=1, pady=10)
