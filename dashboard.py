import tkinter as tk
from tkinter import messagebox
from profile import open_profile
from attack_recommendation import open_attack_recommendation
from target_manager import open_target_manager
from credentials_manager import open_credentials_manager
from wordlist_generator import open_wordlist_generator
from exploit_database import open_exploit_database
from payload_generator import open_payload_generator
from toolkit_inventory import open_toolkit_inventory
from success_probability_calculator import open_success_probability_calculator


def open_dashboard(uname, username):
    dashboard = tk.Toplevel()
    dashboard.title("Red Team Toolkit Management - Dashboard")
    dashboard.config(bg="#0F0F0F")
    dashboard.after(100, lambda: dashboard.state("zoomed"))

    header = tk.Frame(dashboard, bg="#131313", height=60)
    header.pack(fill="x")

    title_label = tk.Label(
        header,
        text="Red Team Toolkit Management",
        font=("Segoe UI", 24, "bold"),
        bg="#131313",
        fg="#00E1FF"
    )
    title_label.pack(pady=10)

    profile_btn = tk.Button(
        header,
        text=f"{username} 👤",
        font=("Segoe UI", 12, "bold"),
        bg="#1E1E1E",
        fg="#00E1FF",
        activebackground="#252525",
        activeforeground="white",
        command=lambda: open_profile(uname),
        relief="ridge",
        bd=2,
        padx=15,
        pady=5
    )
    profile_btn.place(relx=0.97, rely=0.5, anchor="e")

    container = tk.Frame(dashboard, bg="#0F0F0F")
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg="#0F0F0F", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    center_frame = tk.Frame(canvas, bg="#0F0F0F")

    window_id = canvas.create_window(
        0, 0,
        window=center_frame,
        anchor="n"
    )

    def resize_frame(event):
        canvas_width = event.width
        canvas.itemconfig(window_id, width=canvas_width)

    canvas.bind("<Configure>", resize_frame)

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    center_frame.bind("<Configure>", update_scroll)

    def centered_button(text, command):
        btn = tk.Button(
            center_frame,
            text=text,
            width=40,
            height=2,
            bg="#1F1F1F",
            fg="#00E1FF",
            activebackground="#272727",
            activeforeground="white",
            font=("Segoe UI", 13, "bold"),
            relief="ridge",
            bd=2,
            command=command
        )
        btn.pack(pady=12)
        return btn

    centered_button("1. Attack Recommendation",
                    lambda: open_attack_recommendation(dashboard))

    centered_button("2. Target Manager",
                    lambda: open_target_manager(dashboard))

    centered_button("3. Credentials Manager",
                    lambda: open_credentials_manager(dashboard))

    centered_button("4. Wordlist Generator",
                    lambda: open_wordlist_generator(dashboard))

    centered_button("5. Exploit Database",
                    lambda: open_exploit_database(dashboard))

    centered_button("6. Payload Generator",
                    lambda: open_payload_generator(dashboard))

    centered_button("7. Toolkit Inventory",
                    lambda: open_toolkit_inventory(dashboard))

    centered_button("8. Success Probability Calculator",
                    lambda: open_success_probability_calculator(dashboard))

    tk.Button(
        center_frame,
        text="Exit",
        bg="#FF3B3B",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=20,
        command=dashboard.destroy
    ).pack(pady=30)
