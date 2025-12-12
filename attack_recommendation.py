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

def fetch_os_list():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SHOW COLUMNS FROM attack_recommendation")
    columns = [col[0] for col in cursor.fetchall()]

    os_list = []
    for col in columns:
        if col.startswith("os_"):
            os_list.append(col.replace("os_", "").capitalize())

    cursor.close()
    db.close()
    return os_list


def fetch_attack_types():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT attack_type FROM attack_recommendation")
    data = [row[0] for row in cursor.fetchall()]
    cursor.close()
    db.close()
    return data


def open_attack_recommendation(dashboard_win):

    win = tk.Toplevel()
    win.title("Attack Recommendation")
    win.configure(bg="#0f0f0f")

    win.after(100, lambda: win.state("zoomed"))

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=0)
    win.rowconfigure(1, weight=1)

    def go_back():
        win.destroy()
        dashboard_win.deiconify()

    top_frame = tk.Frame(win, bg="#0f0f0f")
    top_frame.grid(row=0, column=0, sticky="e", pady=10, padx=20)

    back_btn = tk.Button(
        top_frame, text="⬅ Back",
        font=("Segoe UI", 11, "bold"),
        bg="#00ff88", fg="black",
        command=go_back
    )
    back_btn.pack(anchor="e")

    title = tk.Label(
        win,
        text="Attack Recommendation Engine",
        font=("Segoe UI", 24, "bold"),
        bg="#0f0f0f",
        fg="#00ff88"
    )
    title.grid(row=0, column=0, pady=(50, 20), sticky="n")

    content_frame = tk.Frame(win, bg="#0f0f0f")
    content_frame.grid(row=1, column=0, sticky="n", pady=10)

    for i in range(2):
        content_frame.columnconfigure(i, weight=1)

    try:
        os_list = fetch_os_list()
        attack_list = fetch_attack_types()
    except:
        messagebox.showerror("Database Error", "Failed to load dropdown data.")
        return

    tk.Label(content_frame, text="Select Target OS:",
             font=("Segoe UI", 14), bg="#0f0f0f", fg="white").grid(row=0, column=0, pady=10, sticky="e")

    os_var = tk.StringVar()
    os_dropdown = ttk.Combobox(content_frame, textvariable=os_var,
                               values=os_list, state="readonly", width=40)
    os_dropdown.grid(row=0, column=1, pady=10, sticky="w")
    if os_list:
        os_dropdown.current(0)

    tk.Label(content_frame, text="Select Attack Type:",
             font=("Segoe UI", 14), bg="#0f0f0f", fg="white").grid(row=1, column=0, pady=10, sticky="e")

    attack_var = tk.StringVar()
    attack_dropdown = ttk.Combobox(content_frame, textvariable=attack_var,
                                   values=attack_list, state="readonly", width=40)
    attack_dropdown.grid(row=1, column=1, pady=10, sticky="w")
    if attack_list:
        attack_dropdown.current(0)

    tk.Label(content_frame, text="Open Ports (comma separated):",
             font=("Segoe UI", 14), bg="#0f0f0f", fg="white").grid(row=2, column=0, pady=10, sticky="e")

    open_ports_entry = tk.Entry(content_frame, width=43,
                                bg="#1c1c1c", fg="#00ff88",
                                insertbackground="#00ff88")
    open_ports_entry.grid(row=2, column=1, pady=10, sticky="w")

    result_box = tk.Text(
        win,
        height=15,
        width=90,
        bg="#1a1a1a",
        fg="#00ff88",
        font=("Consolas", 12),
        wrap="word"
    )
    result_box.grid(row=2, column=0, pady=20)

    def recommend():
        os_val = os_var.get().lower()
        attack_val = attack_var.get()
        open_ports = open_ports_entry.get()

        result_box.delete(1.0, tk.END)

        db = connect_db()
        cursor = db.cursor()

        sql = f"""
        SELECT tool_name, description 
        FROM attack_recommendation
        WHERE attack_type = %s AND os_{os_val} = 1
        """

        cursor.execute(sql, (attack_val,))
        results = cursor.fetchall()

        cursor.close()
        db.close()

        if not results:
            result_box.insert(tk.END, "No tools found for this combination.")
            return

        result_box.insert(tk.END, f"Open Ports: {open_ports}\n\n")

        for tool, desc in results:
            result_box.insert(tk.END, f"[ {tool} ]\n{desc}\n\n")

    tk.Button(
        win,
        text="Get Recommendations",
        command=recommend,
        font=("Segoe UI", 14, "bold"),
        bg="#00ff88",
        fg="black",
        width=25,
        height=1
    ).grid(row=3, column=0, pady=10)
