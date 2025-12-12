import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import itertools
import os

BG = "#0f0f0f"
FG = "#00ff88"

TEMPLATE_FILE = "wordlist_template.csv"


def save_template(data):
    try:
        with open(TEMPLATE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "dob", "pet_name", "fav_things", "nickname", "patterns"])
            writer.writerow(data)
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False


def load_template():
    if not os.path.exists(TEMPLATE_FILE):
        return []
    try:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 1:
                return rows[1]
            return []
    except:
        return []


def generate_wordlist(values):
    final_list = set()

    for v in values:
        if v.strip():
            final_list.update([v, v.lower(), v.upper(), v.capitalize()])

    for r in range(2, 4):
        for combo in itertools.permutations(values, r):
            joined = "".join(combo)
            final_list.update([joined, joined.lower(), joined.upper(), joined.capitalize()])

    return [x for x in final_list if x.strip()]


def open_wordlist_generator(dashboard):

    win = tk.Toplevel()
    win.title("Wordlist Generator")
    win.geometry("900x650")
    win.configure(bg=BG)

    def back():
        win.destroy()
        dashboard.deiconify()

    tk.Button(
        win, text="← Back", command=back,
        bg=FG, fg="black",
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="ne", padx=20, pady=12)

    tk.Label(
        win, text="Wordlist Generator",
        font=("Segoe UI", 26, "bold"),
        fg=FG, bg=BG
    ).pack(pady=10)

    frame = tk.Frame(win, bg=BG)
    frame.pack(pady=10)

    fields = ["Name", "DOB", "Pet Name", "Favourite Things", "Nickname", "Patterns"]
    entries = {}

    saved = load_template()
    saved = saved if saved else [""] * 6

    for i, field in enumerate(fields):
        tk.Label(
            frame, text=f"{field}:",
            bg=BG, fg="white",
            font=("Segoe UI", 12, "bold")
        ).grid(row=i, column=0, sticky="e", padx=10, pady=6)

        e = tk.Entry(
            frame, width=45,
            bg="#1a1a1a", fg="white",
            insertbackground="white",
            font=("Segoe UI", 11)
        )
        e.grid(row=i, column=1, padx=10, pady=6)
        e.insert(0, saved[i])
        entries[field] = e

    def save_csv_template():
        values = [entries[f].get().strip() for f in fields]
        if save_template(values):
            messagebox.showinfo("Saved", "Template saved successfully!")

    tk.Button(
        win, text="Save Template", command=save_csv_template,
        bg=FG, fg="black", width=20,
        font=("Segoe UI", 12, "bold")
    ).pack(pady=12)

    tk.Label(
        win, text="Select fields to include in wordlist:",
        bg=BG, fg="white",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=8)

    check_frame = tk.Frame(win, bg=BG)
    check_frame.pack()

    checks = {}
    for field in fields:
        var = tk.BooleanVar(value=True)
        chk = tk.Checkbutton(
            check_frame, text=field, variable=var,
            bg=BG, fg=FG,
            selectcolor=BG,
            activebackground=BG, activeforeground=FG,
            font=("Segoe UI", 12)
        )
        chk.pack(anchor="center")
        checks[field] = var

    def generate_file():
        selected_values = [entries[f].get().strip() for f in fields if checks[f].get()]

        if not selected_values:
            messagebox.showerror("Error", "Select at least one field.")
            return

        words = generate_wordlist(selected_values)
        if not words:
            messagebox.showerror("Error", "No valid data to generate wordlist.")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Wordlist"
        )

        if not filepath:
            return

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(words))

            messagebox.showinfo("Success", f"Wordlist generated!\nTotal words: {len(words)}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        win, text="Generate Wordlist",
        command=generate_file,
        bg=FG, fg="black",
        width=28, height=1,
        font=("Segoe UI", 15, "bold")
    ).pack(pady=25)
