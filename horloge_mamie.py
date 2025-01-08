import time
from datetime import datetime, timedelta
import threading

class Clock:
    def __init__(self):
        """
        Initializes the clock with the current time, no alarm, 24-hour mode, and not paused.
        """
        self.current_time = datetime.now()
        self.alarm = None
        self.mode_12h = False
        self.paused = False
        self.is_running = False

    def display_time(self):
        """
        Continuously displays the current time, updating every second.
        If an alarm is set, it will notify the user when the alarm time is reached.
        """
        self.is_running = True
        self.pause_message_shown = False
        while self.is_running:
            if not self.paused:
                displayed_time = self.current_time.strftime("%I:%M:%S %p" if self.mode_12h else "%H:%M:%S")
                print(displayed_time, end="\r")

                if self.alarm and self.current_time.strftime("%H:%M:%S") == self.alarm.strftime("%H:%M:%S"):
                    print("\nALARM! It's time!")
                    self.alarm = None  # Disable the alarm after it rings

                self.current_time += timedelta(seconds=1)
                self.pause_message_shown = False
            else:
                if not self.pause_message_shown:
                    print(f"Clock paused - {self.current_time.strftime('%H:%M:%S')}", end="\r")
                    self.pause_message_shown = True

            time.sleep(1)

    def set_alarm(self, h, m, s):
        """
        Sets an alarm for a specific time.

        Args:
            h (int): Hour (0-23)
            m (int): Minute (0-59)
            s (int): Second (0-59)
        """
        self.alarm = self.current_time.replace(hour=h, minute=m, second=s)
        print(f"Alarm set for {h:02d}:{m:02d}:{s:02d}")

    def toggle_mode(self):
        """
        Toggles the clock display mode between 12-hour and 24-hour formats.
        """
        self.mode_12h = not self.mode_12h
        mode = "12-hour" if self.mode_12h else "24-hour"
        # print(f"Mode changed to {mode}")

    def toggle_pause(self):
        """
        Toggles the clock between paused and running states.
        """
        self.paused = not self.paused
        state = "paused" if self.paused else "running"
        print(f"Clock is now {state}")

    def stop_clock(self):
        """
        Stops the clock.
        """
        self.is_running = False


def run_clock(clock):
    """
    Starts the clock in a continuous loop. The user can press Ctrl+C to stop and return to the menu.

    Args:
        clock (Clock): The clock object to run.
    """
    print("Press Ctrl+C to return to the menu")
    try:
        if not clock.is_running:
            display_thread = threading.Thread(target=clock.display_time)
            display_thread.daemon = True
            display_thread.start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clock.stop_clock()
        print("\nReturning to menu")


def menu():
    """
    Displays the main menu for the clock program, allowing the user to choose various options.
    """
    clock = Clock()

    while True:
        print("\n=== MENU ===")
        print("1. Display the current time in real-time")
        print("2. Set the time")
        print("3. Set an alarm")
        print("4. Change display mode (12-hour/24-hour)")
        print("5. Pause/Resume the clock")
        print("6. Exit")

        choice = input("\nYour choice: ")

        if choice == "1":
            run_clock(clock)

        elif choice == "2":
            try:
                h = int(input("Hours (0-23): "))
                m = int(input("Minutes (0-59): "))
                s = int(input("Seconds (0-59): "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    clock.current_time = clock.current_time.replace(hour=h, minute=m, second=s)
                    print("Time successfully set.")
                    run_clock(clock)
                else:
                    print("Invalid values.")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            try:
                h = int(input("Hours (0-23): "))
                m = int(input("Minutes (0-59): "))
                s = int(input("Seconds (0-59): "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    clock.set_alarm(h, m, s)
                    run_clock(clock)
                else:
                    print("Invalid values.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            clock.toggle_mode()

        elif choice == "5":
            clock.toggle_pause()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()