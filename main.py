import sys
import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
from plyer import notification
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import threading
import time

root = tk.Tk()
root.title("YouTube Subscribers Hack")
root.geometry("500x425")
root.resizable(False, False)

frame = ttk.Frame(root, padding=15, relief="ridge", borderwidth=2)
frame.pack(fill="both", expand=True)

header_frame = ttk.Frame(frame)
header_frame.pack(fill="x", pady=(0, 10))

icon_label = ttk.Label(header_frame, text="📈", font=("Segoe UI Emoji", 22))
icon_label.pack(side="left", padx=(0, 8))

title_label = ttk.Label(header_frame, text="YouTube Subscribers Hack v1.0", font=("Segoe UI", 16, "bold"))
title_label.pack(side="left")

progress = ttk.Progressbar(frame, orient="horizontal", length=460, mode="determinate", maximum=100)
progress['value'] = 0
progress.pack(pady=(0, 10))

status_label = ttk.Label(frame, text="Waiting to start...", font=("Segoe UI", 11))
status_label.pack(pady=(0, 5))

console_text = tk.Text(frame, height=10, width=58, state="disabled", bg="#0d0d0d", fg="#39ff14", font=("Consolas", 10))
console_text.pack(pady=(5, 10), fill="both", expand=True)

footer_label = ttk.Label(frame, text="Progress: 0%", font=("Segoe UI", 9, "italic"))
footer_label.pack()

controls_frame = ttk.Frame(frame)
controls_frame.pack(pady=(10, 0))

btn_start = ttk.Button(controls_frame, text="Start")
btn_start.grid(row=0, column=0, padx=5)

btn_pause = ttk.Button(controls_frame, text="Pause")
btn_pause.grid(row=0, column=1, padx=5)

btn_stop = ttk.Button(controls_frame, text="Stop")
btn_stop.grid(row=0, column=2, padx=5)

# Dummy commands (do nothing)
btn_pause.config(command=lambda: None)
btn_stop.config(command=lambda: None)

class BrowserWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("interface")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl(url))
        self.showFullScreen()

def open_fake_browser():
    root.destroy()
    app = QApplication(sys.argv)
    if os.path.exists("backend/interface.html"):
        local_file_path = os.path.abspath("backend/interface.html")
    else:
        local_file_path = os.path.abspath("_internal/backend/interface.html")
    url = f"file:///{local_file_path.replace(os.sep, '/')}"
    window = BrowserWindow(url)
    sys.exit(app.exec_())

def send_notification(title, message, timeout):
    notification.notify(title=title, message=message, timeout=timeout)

def disable_minimize():
    for w in popup_windows:
        w.attributes("-toolwindow", 1)

def spawn_ghosts():
    def ghost():
        for _ in range(5):
            ghost_win = tk.Toplevel()
            ghost_win.geometry(f"200x80+{random.randint(100, 800)}+{random.randint(100, 600)}")
            tk.Label(ghost_win, text="👻 System Glitch Detected!").pack()
            ghost_win.after(2000, ghost_win.destroy)
    threading.Thread(target=ghost).start()

def wiggle_cursor():
    def animate_cursor():
        fake_cursor = tk.Toplevel()
        fake_cursor.overrideredirect(1)
        fake_cursor.geometry("20x20")
        fake_cursor.attributes("-topmost", True)
        dot = tk.Label(fake_cursor, text="🖱️", font=("Arial", 12))
        dot.pack()
        for _ in range(30):
            x = root.winfo_x() + random.randint(0, 400)
            y = root.winfo_y() + random.randint(0, 300)
            fake_cursor.geometry(f"+{x}+{y}")
            time.sleep(0.05)
        fake_cursor.destroy()
    threading.Thread(target=animate_cursor).start()

def show_fake_error():
    msgbox.showerror("Fatal Error", "System Error: 0x00000F")

def fake_lock_keyboard():
    status_label.config(text="(Attempting to lock keyboard... just kidding!)")

steps = [
    ("Setting up script...", (1000, 2000), None, 2),
    ("Finding 1,000 YouTube subscribers...", (2000, 3500), None, 14),
    ("Sending request to YouTube servers...", (1500, 2500), None, 22),
    ("Request failed, trying again (1/3)", (500, 1000), None, 27),
    ("Sending request to YouTube servers...", (1000, 2000), None, 35),
    ("Request failed, trying again (2/3)", (300, 800), None, 41),
    ("Sending request to YouTube servers...", (1000, 1800), None, 50),
    ("Request failed, trying again (3/3)", (300, 600), None, 58),
    ("Sending request to YouTube servers...", (800, 1500), None, 65),
    ("Request failed, trying another method.", (1200, 2000), None, 68),
    ("Ordering x15 Dell Inspiron 15 Laptops...", (2000, 3000), None, 72),
    ("Authenticating card details...", (2500, 4000), None, 75),
    ("Success!", (1000, 1500), {
        "title": "Payment Alert",
        "message": "Charged £5575 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 78),
    ("Ordering x1 Generic Anime Body Pillow...", (2000, 3000), None, 80),
    ("Authenticating card details...", (2500, 4000), None, 81),
    ("Success!", (1000, 1500), {
        "title": "Payment Alert",
        "message": "Charged £29.99 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 83),
    ("Ordering x3 RGB Gaming Mousepads...", (1500, 2500), None, 84),
    ("Authenticating card details...", (1200, 2000), None, 86),
    ("Success!", (800, 1200), {
        "title": "Payment Alert",
        "message": "Charged £59.97 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 87),
    ("Ordering x2 4090 Graphics Cards...", (2000, 3000), None, 89),
    ("Authenticating card details...", (1500, 2500), None, 90),
    ("Success!", (1000, 1500), {
        "title": "Payment Alert",
        "message": "Charged £3198 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 91),
    ("Ordering x5 Mystery Snack Boxes...", (1200, 1800), None, 92),
    ("Authenticating card details...", (1000, 1500), None, 93),
    ("Success!", (800, 1200), {
        "title": "Payment Alert",
        "message": "Charged £74.95 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 94),
    ("Ordering x1 Inflatable Dinosaur Costume...", (1500, 2200), None, 95),
    ("Authenticating card details...", (1200, 1800), None, 96),
    ("Success!", (800, 1200), {
        "title": "Payment Alert",
        "message": "Charged £39.99 from Amazon on Mastercard ending with ****",
        "timeout": 3
    }, 97),
    ("Disabling minimize buttons...", (1000, 1500), "disable_minimize", 97),
    ("Spawning ghost windows...", (1500, 2500), "spawn_ghosts", 97),
    ("Making your cursor dance...", (2000, 3000), "wiggle_cursor", 98),
    ("Showing random error messages...", (2000, 3000), "show_fake_error", 98),
    ("Locking keyboard... (just kidding)", (1000, 2000), "fake_lock_keyboard", 98),
    ("Deleting C:/Windows/System32...", (2000, 3500), None, 99),
    ("Deleting C:/Windows...", (1500, 2500), None, 99),
    ("Installing Red Star OS...", (2500, 4000), None, 100),
    ("Error", (1000, 1000), None, 100),
]

popup_windows = []
total_ok_clicks = 0
popups_finished = False
in_popup_phase = False
current_index = 0
paused = False
stopped = False
shown_messages = set()

def create_popups(num):
    to_create = num - len(popup_windows)
    if to_create <= 0:
        return
    for _ in range(to_create):
        popup = tk.Toplevel()
        popup.title("Warning!")
        popup.geometry("300x100+{}+{}".format(
            root.winfo_x() + random.randint(-100, 100),
            root.winfo_y() + random.randint(-100, 100)
        ))
        label_popup = tk.Label(popup, text="System warning detected! Click OK to continue.")
        label_popup.pack(pady=10)
        btn = tk.Button(popup, text="OK", command=lambda p=popup: on_ok_click(p))
        btn.pack()
        btn.focus_set()
        popup.bind('<Return>', lambda event, p=popup: on_ok_click(p))
        popup.protocol("WM_DELETE_WINDOW", lambda p=popup: on_ok_click(p))
        popup_windows.append(popup)

def on_ok_click(popup):
    global total_ok_clicks, popups_finished, in_popup_phase, current_index
    if popup in popup_windows:
        popup.destroy()
        popup_windows.remove(popup)
    total_ok_clicks += 1
    if total_ok_clicks >= 25:
        if not popups_finished:
            popups_finished = True
            in_popup_phase = False
            for win in popup_windows:
                win.destroy()
            popup_windows.clear()
            root.after(500, lambda: update(current_index + 1))
    else:
        if not popups_finished:
            new_target = len(popup_windows) * 2 or 2
            create_popups(new_target)

def update(index=0):
    global current_index, in_popup_phase, paused, stopped
    if stopped:
        status_label.config(text="Process stopped.")
        return
    if paused:
        status_label.config(text="Paused...")
        root.after(500, update, index)
        return
    current_index = index
    if in_popup_phase:
        return
    if index < len(steps):
        message, delay_range, notify, progress_percent = steps[index]
        status_label.config(text=f"Status: {message}")
        progress['value'] = progress_percent
        footer_label.config(text=f"Progress: {progress_percent}%")

        if message not in shown_messages:
            shown_messages.add(message)
            console_text.config(state="normal")
            console_text.insert("end", f"[{time.strftime('%H:%M:%S')}] {message}\n")
            console_text.see("end")
            console_text.config(state="disabled")

        base_delay = random.randint(*delay_range)
        jitter = random.randint(-200, 200)
        final_delay = max(300, base_delay + jitter)

        if isinstance(notify, dict):
            root.after(500, lambda: send_notification(notify['title'], notify['message'], notify['timeout']))
        elif isinstance(notify, str):
            prank_actions = {
                "disable_minimize": disable_minimize,
                "spawn_ghosts": spawn_ghosts,
                "wiggle_cursor": wiggle_cursor,
                "show_fake_error": show_fake_error,
                "fake_lock_keyboard": fake_lock_keyboard,
            }
            action = prank_actions.get(notify)
            if action:
                action()

        if message == "Deleting C:/Windows/System32...":
            in_popup_phase = True
            create_popups(1)
            return

        if message == "Error":
            root.after(final_delay, open_fake_browser)
            return

        root.after(final_delay, update, index + 1)
    else:
        status_label.config(text="Process completed!")
        btn_start.config(state="normal")
        btn_pause.config(state="disabled")
        btn_stop.config(state="disabled")

def start():
    global paused, stopped, total_ok_clicks, popups_finished, in_popup_phase, current_index, shown_messages
    if btn_start['state'] == 'disabled':
        return
    paused = False
    stopped = False
    total_ok_clicks = 0
    popups_finished = False
    in_popup_phase = False
    current_index = 0
    shown_messages = set()
    progress['value'] = 0
    footer_label.config(text="Progress: 0%")
    console_text.config(state="normal")
    console_text.delete(1.0, "end")
    console_text.config(state="disabled")
    status_label.config(text="Starting process...")
    btn_start.config(state="disabled")
    btn_pause.config(state="normal", text="Pause")
    btn_stop.config(state="normal")
    root.after(1000, update)

btn_start.config(command=start)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.mainloop()
