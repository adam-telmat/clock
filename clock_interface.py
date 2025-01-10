import customtkinter as ctk
import time
from datetime import datetime, timedelta
import threading

class Clock:
    def __init__(self, master):
        self.master = master
        self.current_time = datetime.now()
        self.alarm = None
        self.is_12h_mode = False
        self.is_paused = False
        self.is_running = False

        # Main window configuration
        self.master.title("Clock")
        self.master.geometry("400x300")
        
        # GUI widgets
        self.time_label = ctk.CTkLabel(master, text=self.current_time.strftime("%H:%M:%S"), font=("Helvetica", 36))
        self.time_label.pack(pady=20)

        self.pause_button = ctk.CTkButton(master, text="Pause/Resume", command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        self.mode_button = ctk.CTkButton(master, text="Switch 12h/24h Mode", command=self.switch_mode)
        self.mode_button.pack(pady=10)

        self.alarm_button = ctk.CTkButton(master, text="Set Alarm", command=self.open_alarm_window)
        self.alarm_button.pack(pady=10)

        self.set_time_button = ctk.CTkButton(master, text="Set Time", command=self.open_time_window)
        self.set_time_button.pack(pady=10)

        # Start the clock
        self.start_clock()

    def update_time(self):
        if not self.is_paused:
            displayed_time = self.current_time.strftime("%I:%M:%S %p" if self.is_12h_mode else "%H:%M:%S")
            self.time_label.configure(text=displayed_time)
            
            if self.alarm and self.current_time.strftime("%H:%M:%S") == self.alarm.strftime("%H:%M:%S"):
                print("\nRING RING! It's alarm time!")
                self.alarm = None  # Disable the alarm after it rings
            
            self.current_time += timedelta(seconds=1)
        
        self.master.after(1000, self.update_time)

    def set_alarm(self, h, m, s):
        self.alarm = self.current_time.replace(hour=h, minute=m, second=s)
        print(f"Alarm set for {h:02d}:{m:02d}:{s:02d}")

    def open_alarm_window(self):
        window = ctk.CTkToplevel(self.master)
        window.title("Set Alarm")
        window.geometry("300x300")
        
        ctk.CTkLabel(window, text="Hours (0-23)").pack(pady=5)
        hours_entry = ctk.CTkEntry(window)
        hours_entry.pack()

        ctk.CTkLabel(window, text="Minutes (0-59)").pack(pady=5)
        minutes_entry = ctk.CTkEntry(window)
        minutes_entry.pack()

        ctk.CTkLabel(window, text="Seconds (0-59)").pack(pady=5)
        seconds_entry = ctk.CTkEntry(window)
        seconds_entry.pack()

        def confirm():
            try:
                h = int(hours_entry.get())
                m = int(minutes_entry.get())
                s = int(seconds_entry.get())
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    self.set_alarm(h, m, s)
                    window.destroy()
                else:
                    print("Invalid values.")
            except ValueError:
                print("Invalid input.")

        ctk.CTkButton(window, text="Confirm", command=confirm).pack(pady=10)

    def open_time_window(self):
        window = ctk.CTkToplevel(self.master)
        window.title("Set Time")
        window.geometry("300x300")
        
        ctk.CTkLabel(window, text="Hours (0-23)").pack(pady=5)
        hours_entry = ctk.CTkEntry(window)
        hours_entry.pack()

        ctk.CTkLabel(window, text="Minutes (0-59)").pack(pady=5)
        minutes_entry = ctk.CTkEntry(window)
        minutes_entry.pack()

        ctk.CTkLabel(window, text="Seconds (0-59)").pack(pady=5)
        seconds_entry = ctk.CTkEntry(window)
        seconds_entry.pack()

        def confirm():
            try:
                h = int(hours_entry.get())
                m = int(minutes_entry.get())
                s = int(seconds_entry.get())
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    self.current_time = self.current_time.replace(hour=h, minute=m, second=s)
                    print("Time successfully set.")
                    window.destroy()
                else:
                    print("Invalid values.")
            except ValueError:
                print("Invalid input.")

        ctk.CTkButton(window, text="Confirm", command=confirm).pack(pady=10)

    def switch_mode(self):
        self.is_12h_mode = not self.is_12h_mode
        mode = "12h" if self.is_12h_mode else "24h"
        print(f"Mode switched to {mode}")

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        state = "paused" if self.is_paused else "running"
        print(f"Clock {state}")

    def start_clock(self):
        if not self.is_running:
            self.is_running = True
            self.update_time()

if __name__ == "__main__":
    root = ctk.CTk()
    app = Clock(root)
    root.mainloop()
