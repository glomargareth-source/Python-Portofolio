import tkinter as tk
from datetime import datetime

class StarTrekClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Star Trek Digital Clock")
        self.root.geometry("500x300")
        self.is_24hour = True
        self.current_theme = 0
        
        # Star Trek color themes (LCARS inspired)
        self.themes = [
            {"bg": "#000000", "time": "#FF9966", "date": "#9999FF", "btn": "#CC6699"},
            {"bg": "#1a1a2e", "time": "#00D9FF", "date": "#FFB800", "btn": "#FF6B9D"},
            {"bg": "#0f0f23", "time": "#66FF66", "date": "#FFCC00", "btn": "#FF3366"}
        ]
        
        # Bahasa Indonesia months
        self.bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                      "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        self.hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        
        self.setup_ui()
        self.update_time()
        
    def setup_ui(self):
        self.root.configure(bg=self.themes[0]["bg"])
        
        # Time label
        self.time_label = tk.Label(self.root, font=("Consolas", 60, "bold"))
        self.time_label.pack(pady=30)
        
        # Date label
        self.date_label = tk.Label(self.root, font=("Consolas", 16))
        self.date_label.pack(pady=10)
        
        # Button frame
        btn_frame = tk.Frame(self.root, bg=self.themes[0]["bg"])
        btn_frame.pack(pady=20)
        
        # Toggle format button
        self.format_btn = tk.Button(btn_frame, text="12-Hour", font=("Consolas", 12),
                                    command=self.toggle_format, width=12)
        self.format_btn.pack(side=tk.LEFT, padx=5)
        
        # Theme button
        self.theme_btn = tk.Button(btn_frame, text="Change Theme", font=("Consolas", 12),
                                   command=self.change_theme, width=12)
        self.theme_btn.pack(side=tk.LEFT, padx=5)
        
        self.apply_theme()
    
    def update_time(self):
        now = datetime.now()
        if self.is_24hour:
            time_str = now.strftime("%H:%M:%S")
        else:
            time_str = now.strftime("%I:%M:%S %p")
        
        day_idx = now.weekday()
        date_str = f"{self.hari[day_idx]}, {now.day} {self.bulan[now.month-1]} {now.year}"
        
        self.time_label.config(text=time_str)
        self.date_label.config(text=date_str)
        self.root.after(1000, self.update_time)
    
    def toggle_format(self):
        self.is_24hour = not self.is_24hour
        self.format_btn.config(text="12-Hour" if self.is_24hour else "24-Hour")
    
    def change_theme(self):
        self.current_theme = (self.current_theme + 1) % len(self.themes)
        self.apply_theme()
    
    def apply_theme(self):
        theme = self.themes[self.current_theme]
        self.root.configure(bg=theme["bg"])
        self.time_label.config(bg=theme["bg"], fg=theme["time"])
        self.date_label.config(bg=theme["bg"], fg=theme["date"])
        self.format_btn.config(bg=theme["btn"], fg="#FFFFFF", activebackground=theme["time"])
        self.theme_btn.config(bg=theme["btn"], fg="#FFFFFF", activebackground=theme["time"])

root = tk.Tk()
app = StarTrekClock(root)
root.mainloop()