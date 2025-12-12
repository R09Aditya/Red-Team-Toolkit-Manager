import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as sqltor

BG = "#0f0f0f"
FG = "#00ff88"


def open_toolkit_inventory(dashboard):


    win = tk.Toplevel()
    win.title("Toolkit Inventory")
    win.state("zoomed")
    win.configure(bg=BG)

    def back():
        win.destroy()
        dashboard.deiconify()

    tk.Button(
        win, text="← Back", command=back,
        bg=FG, fg="black", font=("Segoe UI", 12, "bold")
    ).pack(anchor="ne", padx=25, pady=15)

    tk.Label(
        win, text="Toolkit Inventory",
        font=("Segoe UI", 26, "bold"),
        fg=FG, bg=BG
    ).pack(pady=10)

    def connect_db():
        return sqltor.connect(
            host="localhost",
            user="root",
            password="tiger",
            database="rttm"
        )

    tree_frame = tk.Frame(win, bg=BG)
    tree_frame.pack(pady=10, fill="both")

    columns = ("ID", "Tool Name", "Type", "Version", "Description")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=12)

    style = ttk.Style()
    style.configure("Treeview", background="#111", foreground=FG, fieldbackground="#111", rowheight=28)
    style.configure("Treeview.Heading", background="#222", foreground=FG, font=("Segoe UI", 11, "bold"))

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200, anchor="center")

    tree.pack(padx=20, fill="x")

    def load_data():
        for i in tree.get_children():
            tree.delete(i)
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT tid, tool_name, tool_type, version, description FROM toolkit_inventory")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        cursor.close()
        db.close()

    load_data()

    form_frame = tk.Frame(win, bg=BG)
    form_frame.pack(pady=15)

    def add_field(label, row):
        tk.Label(
            form_frame,
            text=label,
            fg=FG, bg=BG,
            font=("Segoe UI", 11, "bold")
        ).grid(row=row, column=0, sticky="e", padx=10, pady=6)

    def add_entry(row, width=40):
        e = tk.Entry(
            form_frame, width=width,
            bg="#1c1c1c", fg=FG,
            insertbackground=FG, font=("Segoe UI", 11)
        )
        e.grid(row=row, column=1, sticky="w", padx=10, pady=6)
        return e

    add_field("Tool Name:", 0)
    name_entry = add_entry(0)

    add_field("Type:", 1)
    type_entry = add_entry(1)

    add_field("Version:", 2)
    version_entry = add_entry(2)

    add_field("Description:", 3)
    desc_entry = add_entry(3, width=50)

    def add_tool():
        name = name_entry.get()
        ttype = type_entry.get()
        version = version_entry.get()
        desc = desc_entry.get()

        if name == "":
            messagebox.showerror("Error", "Tool Name is required.")
            return

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO toolkit_inventory (tool_name, tool_type, version, description)
            VALUES (%s, %s, %s, %s)
        """, (name, ttype, version, desc))
        db.commit()
        cursor.close()
        db.close()

        load_data()
        messagebox.showinfo("Success", "Tool added successfully.")

    def update_tool():
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a tool to update.")
            return
        tid = tree.item(selected[0])["values"][0]

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE toolkit_inventory SET tool_name=%s, tool_type=%s, version=%s, description=%s WHERE tid=%s
        """, (name_entry.get(), type_entry.get(), version_entry.get(), desc_entry.get(), tid))
        db.commit()
        cursor.close()
        db.close()

        load_data()
        messagebox.showinfo("Success", "Tool updated successfully.")

    def delete_tool():
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a tool to delete.")
            return
        tid = tree.item(selected[0])["values"][0]

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM toolkit_inventory WHERE tid=%s", (tid,))
        db.commit()
        cursor.close()
        db.close()

        load_data()
        messagebox.showinfo("Success", "Tool deleted successfully.")

    btn_frame = tk.Frame(win, bg=BG)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add Tool", command=add_tool,
              bg=FG, fg="black", width=18, font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=12)

    tk.Button(btn_frame, text="Update Tool", command=update_tool,
              bg=FG, fg="black", width=18, font=("Segoe UI", 11, "bold")).grid(row=0, column=1, padx=12)

    tk.Button(btn_frame, text="Delete Tool", command=delete_tool,
              bg="#ff4444", fg="white", width=18, font=("Segoe UI", 11, "bold")).grid(row=0, column=2, padx=12)

    def fill_form(event):
        selected = tree.selection()
        if selected:
            values = tree.item(selected[0])["values"]

            name_entry.delete(0, tk.END)
            type_entry.delete(0, tk.END)
            version_entry.delete(0, tk.END)
            desc_entry.delete(0, tk.END)

            name_entry.insert(0, values[1])
            type_entry.insert(0, values[2])
            version_entry.insert(0, values[3])
            desc_entry.insert(0, values[4])

    tree.bind("<<TreeviewSelect>>", fill_form)
