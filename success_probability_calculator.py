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
    os_list = [col.replace("os_", "").capitalize() for col in columns if col.startswith("os_")]
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

def open_success_probability_calculator(dashboard):
   

    win = tk.Toplevel()
    win.title("Success Probability Calculator")
    win.state("zoomed")                      # FULL SCREEN
    win.configure(bg="#0f0f0f")

    # Responsive grid
    win.columnconfigure(0, weight=1)
    win.rowconfigure(6, weight=1)

    # BACK BUTTON (top right)
    def back():
        win.destroy()
        dashboard.deiconify()

    tk.Button(
        win, text="← Back", command=back,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 12, "bold")
    ).grid(row=0, column=0, sticky="ne", padx=20, pady=20)

    # TITLE (center)
    tk.Label(
        win, text="Success Probability Calculator",
        font=("Segoe UI", 28, "bold"),
        fg="#00ff88", bg="#0f0f0f"
    ).grid(row=1, column=0, pady=20)

    # CENTERED FRAME
    frame = tk.Frame(win, bg="#0f0f0f")
    frame.grid(row=2, column=0, pady=20)

    for i in range(2):
        frame.columnconfigure(i, weight=1)

    # ------------------------------
    # DROPDOWNS + INPUTS
    # ------------------------------
    def create_label(text, r):
        tk.Label(
            frame, text=text,
            font=("Segoe UI", 14),
            fg="#00ff88", bg="#0f0f0f"
        ).grid(row=r, column=0, sticky="e", padx=20, pady=10)

    def create_entry(r):
        e = tk.Entry(
            frame, width=32, bg="#1c1c1c",
            fg="#00ff88", insertbackground="#00ff88",
            font=("Segoe UI", 12)
        )
        e.grid(row=r, column=1, sticky="w", padx=20, pady=10)
        return e

    create_label("Select Target OS:", 0)
    os_var = tk.StringVar()
    os_dropdown = ttk.Combobox(
        frame, textvariable=os_var,
        values=fetch_os_list(), state="readonly", width=30
    )
    os_dropdown.grid(row=0, column=1, pady=10)
    if os_dropdown["values"]:
        os_dropdown.current(0)

    create_label("Select Attack Type:", 1)
    attack_var = tk.StringVar()
    attack_dropdown = ttk.Combobox(
        frame, textvariable=attack_var,
        values=fetch_attack_types(), state="readonly", width=30
    )
    attack_dropdown.grid(row=1, column=1, pady=10)
    if attack_dropdown["values"]:
        attack_dropdown.current(0)

    create_label("Open Ports (comma separated):", 2)
    open_ports_entry = create_entry(2)

    create_label("Tool (optional):", 3)
    tool_entry = create_entry(3)

    # ------------------------------
    # RESULT BOX (centered)
    # ------------------------------
    result_box = tk.Text(
        win, height=10, width=80,
        bg="#1a1a1a", fg="#00ff88",
        font=("Consolas", 13)
    )
    result_box.grid(row=3, column=0, pady=20)

    # ------------------------------
    # CALCULATION LOGIC
    # ------------------------------
    def calculate_probability():
        os_val = os_var.get().lower()
        attack_val = attack_var.get()
        open_ports = open_ports_entry.get()
        tool_val = tool_entry.get()

        result_box.delete(1.0, tk.END)

        db = connect_db()
        cursor = db.cursor()

        # base probability
        cursor.execute(
            f"SELECT COUNT(*) FROM attack_recommendation "
            f"WHERE attack_type=%s AND os_{os_val}=1",
            (attack_val,)
        )
        rows = cursor.fetchone()[0]
        probability = min(rows * 25, 100)

        # port bonus
        if open_ports.strip():
            ports = [p.strip() for p in open_ports.split(",") if p.strip().isdigit()]
            probability += len(ports) * 5

        # tool bonus
        if tool_val.strip():
            cursor.execute(
                "SELECT COUNT(*) FROM toolkit_inventory WHERE tool_name LIKE %s",
                (f"%{tool_val}%",)
            )
            probability += cursor.fetchone()[0] * 10

        cursor.close()
        db.close()

        probability = min(probability, 100)

        # OUTPUT
        result_box.insert(tk.END, f"Estimated Success Probability: {probability}%\n\n")
        result_box.insert(tk.END, f"Attack Type: {attack_val}\n")
        result_box.insert(tk.END, f"Target OS: {os_val.capitalize()}\n\n")

        if open_ports.strip():
            result_box.insert(tk.END, f"Open Ports: {open_ports}\n")
        if tool_val.strip():
            result_box.insert(tk.END, f"Tool Used: {tool_val}\n")

    tk.Button(
        win, text="Calculate", command=calculate_probability,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 14, "bold"),
        width=22, height=2
    ).grid(row=4, column=0, pady=20)
