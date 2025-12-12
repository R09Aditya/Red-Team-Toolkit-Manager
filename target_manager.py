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

def open_target_manager(dashboard):

    win = tk.Toplevel()
    win.title("Target Manager")
    win.state("zoomed")
    win.configure(bg="#0f0f0f")

    win.columnconfigure(0, weight=1)
    for r in range(10):
        win.rowconfigure(r, weight=0)

    def go_back():
        win.destroy()
        dashboard.deiconify()

    tk.Button(
        win, text="← Back", command=go_back,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 12, "bold")
    ).grid(row=0, column=0, sticky="ne", padx=30, pady=20)

    tk.Label(
        win, text="Target Manager",
        font=("Segoe UI", 28, "bold"),
        fg="#00ff88", bg="#0f0f0f"
    ).grid(row=1, column=0, pady=10)

    form = tk.Frame(win, bg="#0f0f0f")
    form.grid(row=2, column=0, pady=10)

    for i in range(2):
        form.columnconfigure(i, weight=1)

    def create_label(text, row):
        tk.Label(
            form, text=text,
            bg="#0f0f0f", fg="white",
            font=("Segoe UI", 12)
        ).grid(row=row, column=0, sticky="e", padx=20, pady=8)

    def create_entry(row):
        e = tk.Entry(
            form, width=45,
            bg="#1c1c1c", fg="#00ff88",
            insertbackground="#00ff88",
            font=("Segoe UI", 12)
        )
        e.grid(row=row, column=1, sticky="w", padx=20, pady=8)
        return e

    create_label("Target Name:", 0)
    name_entry = create_entry(0)

    create_label("IP Address:", 1)
    ip_entry = create_entry(1)

    create_label("OS:", 2)
    os_entry = ttk.Combobox(
        form, values=["Windows", "Linux", "Android", "iOS", "macOS", "Other"],
        state="readonly", width=43
    )
    os_entry.grid(row=2, column=1, pady=8, sticky="w", padx=20)
    os_entry.current(0)

    create_label("Description:", 3)
    desc_entry = create_entry(3)

    create_label("Notes:", 4)
    notes_entry = create_entry(4)

    def save_target():
        name = name_entry.get()
        ip = ip_entry.get()
        os_val = os_entry.get()
        desc = desc_entry.get()
        notes = notes_entry.get()

        if name == "" or ip == "":
            messagebox.showerror("Error", "Name & IP are required")
            return

        db = connect_db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO target_manager (target_name, ip_address, os, description, notes)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, ip, os_val, desc, notes))

        db.commit()
        cursor.close()
        db.close()

        load_targets()
        messagebox.showinfo("Success", "Target Added!")

    tk.Button(
        win, text="Add Target", command=save_target,
        font=("Segoe UI", 14, "bold"),
        bg="#00ff88", fg="black",
        width=20
    ).grid(row=3, column=0, pady=15)

    list_frame = tk.Frame(win, bg="#0f0f0f")
    list_frame.grid(row=4, column=0, pady=10)

    columns = ("ID", "Name", "IP", "OS", "Description", "Notes")
    tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=12)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=170)

    tree.pack()

    def load_targets():
        for row in tree.get_children():
            tree.delete(row)

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM target_manager")
        rows = cursor.fetchall()

        for r in rows:
            tree.insert("", "end", values=r)

        cursor.close()
        db.close()

    load_targets()

    def delete_selected():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a target to delete")
            return

        target_id = tree.item(selected, "values")[0]

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM target_manager WHERE id=%s", (target_id,))
        db.commit()
        db.close()

        load_targets()
        messagebox.showinfo("Deleted", "Target removed")

    tk.Button(
        win, text="Delete Selected", command=delete_selected,
        font=("Segoe UI", 12), width=20,
        bg="#ff4444", fg="white"
    ).grid(row=5, column=0, pady=8)

    def update_selected():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a target to update")
            return

        values = tree.item(selected, "values")
        target_id = values[0]

        upd = tk.Toplevel(win)
        upd.title("Update Target")
        upd.geometry("450x350")
        upd.configure(bg="#0f0f0f")

        tk.Label(
            upd, text="Update Target Details",
            font=("Segoe UI", 16, "bold"),
            bg="#0f0f0f", fg="#00ff88"
        ).pack(pady=10)

        form_u = tk.Frame(upd, bg="#0f0f0f")
        form_u.pack(pady=10)

        labels = ["Target Name:", "IP Address:", "OS:", "Description:", "Notes:"]
        for i, lbl in enumerate(labels):
            tk.Label(form_u, text=lbl, bg="#0f0f0f", fg="white").grid(row=i, column=0, sticky="w", pady=5)

        name_u = tk.Entry(form_u, width=35); name_u.insert(0, values[1])
        ip_u = tk.Entry(form_u, width=35); ip_u.insert(0, values[2])

        os_u = ttk.Combobox(
            form_u,
            values=["Windows", "Linux", "Android", "iOS", "macOS", "Other"],
            state="readonly", width=33
        )
        os_u.set(values[3])

        desc_u = tk.Entry(form_u, width=35); desc_u.insert(0, values[4])
        notes_u = tk.Entry(form_u, width=35); notes_u.insert(0, values[5])

        entries = [name_u, ip_u, os_u, desc_u, notes_u]
        for i, ent in enumerate(entries):
            ent.grid(row=i, column=1, pady=5)

        def save_updates():
            db = connect_db()
            cursor = db.cursor()

            cursor.execute("""
                UPDATE target_manager
                SET target_name=%s, ip_address=%s, os=%s, description=%s, notes=%s
                WHERE id=%s
            """, (name_u.get(), ip_u.get(), os_u.get(),
                  desc_u.get(), notes_u.get(), target_id))

            db.commit()
            db.close()

            upd.destroy()
            load_targets()
            messagebox.showinfo("Updated", "Target details updated successfully!")

        tk.Button(
            upd, text="Save Updates",
            command=save_updates,
            bg="#00ff88", fg="black", width=20
        ).pack(pady=15)
