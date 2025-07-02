import customtkinter as ctk
from monitor.monitor import start_monitoring

def start_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.geometry("400x300")
    app.title("FPS Booster")

    label = ctk.CTkLabel(app, text="🎮 FPS Booster Aktif", font=("Arial", 20))
    label.pack(pady=20)

    start_button = ctk.CTkButton(app, text="Boost Başlat", command=start_monitoring)
    start_button.pack(pady=10)

    app.mainloop()
