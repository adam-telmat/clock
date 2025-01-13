import time
from datetime import datetime, timedelta
import threading

class Clock:
    def __init__(self):
        """
        Initializes the clock with the current time, no alarm, 24-hour mode, and not paused.
        """
        self.current_time = datetime.now()  # Initializing the current time
        self.alarm = None  # Setting the alarm to None initially
        self.mode_12h = False  # Default is 24-hour mode
        self.paused = False  # Clock is not paused initially
        self.is_running = False  # Clock is not running initially

    def display_time(self):
        """
        Continuously displays the current time, updating every second.
        If an alarm is set, it will notify the user when the alarm time is reached.
        """
        self.is_running = True  # The program is now running
        self.pause_message_shown = False  # Pause message hasn't been displayed yet
        while self.is_running:
            if not self.paused:  # If the clock is not paused
                # Format time based on 12-hour or 24-hour mode
                displayed_time = self.current_time.strftime("%I:%M:%S %p" if self.mode_12h else "%H:%M:%S")
                print(displayed_time, end="\r")  # Display time on the same line

                # Check if the current time matches the alarm time
                if self.alarm and self.current_time.strftime("%H:%M:%S") == self.alarm.strftime("%H:%M:%S"):
                    print("\nALARM! It's time!")  # Notify user when the alarm rings
                    self.alarm = None  # Disable the alarm after it rings

                # Increment the time by one second
                self.current_time += timedelta(seconds=1)
                self.pause_message_shown = False  # Reset the pause message
            else:
                # If the clock is paused, show a message
                if not self.pause_message_shown:
                    print(f"Clock paused - {self.current_time.strftime('%H:%M:%S')}", end="\r")
                    self.pause_message_shown = True  # Prevent displaying the pause message repeatedly

            time.sleep(1)  # Wait for 1 second before refreshing the time

    def set_time_from_tuple(self, time_tuple):
        """
        Sets the time using a tuple (hours, minutes, seconds).
        This will convert the tuple into a datetime object.
        """
        h, m, s = time_tuple  # Decompose the tuple into hours, minutes, and seconds
        self.current_time = self.current_time.replace(hour=h, minute=m, second=s)  # Set the time
        print(f"Time successfully set to {h:02d}:{m:02d}:{s:02d}")  # Display the updated time

    def set_alarm(self, time_tuple):
        """
        Sets an alarm for a specific time using a tuple (hours, minutes, seconds).
        """
        h, m, s = time_tuple  # Decompose the tuple to set the alarm time
        self.alarm = self.current_time.replace(hour=h, minute=m, second=s)  # Set the alarm
        print(f"Alarm set for {h:02d}:{m:02d}:{s:02d}")  # Display the alarm time

    def toggle_mode(self):
        """
        Toggles the clock display mode between 12-hour and 24-hour formats.
        """
        self.mode_12h = not self.mode_12h  # Switch between 12-hour and 24-hour mode
        mode = "12-hour" if self.mode_12h else "24-hour"  # Determine the current mode
        print(f"Mode changed to {mode}")  # Display the selected mode

    def toggle_pause(self):
        """
        Toggles the clock between paused and running states.
        """
        self.paused = not self.paused  # Switch between paused and running state
        state = "paused" if self.paused else "running"  # Display the current state
        print(f"Clock is now {state}")  # Display the clock state

    def stop_clock(self):
        """
        Stops the clock.
        """
        self.is_running = False  # Stop the clock

def run_clock(clock):
    """
    Starts the clock in a continuous loop. The user can press Ctrl+C to stop and return to the menu.
    """
    print("Press Ctrl+C to return to the menu")  # Inform the user how to exit
    try:
        if not clock.is_running:
            # Start a thread to run the clock in the background
            display_thread = threading.Thread(target=clock.display_time)
            display_thread.daemon = True  # Daemonize the thread so it stops when the program exits
            display_thread.start()

        while True:  # Main loop to keep the program running
            time.sleep(1)
    except KeyboardInterrupt:  # If the user presses Ctrl+C
        clock.stop_clock()  # Stop the clock
        print("\nReturning to menu")  # Inform the user that the menu is being shown again

def menu():
    """
    Displays the main menu for the clock program, allowing the user to choose various options.
    """
    clock = Clock()  # Create an instance of the clock

    while True:  # Display the menu in a loop
        print("\n=== MENU ===")
        print("1. Display the current time in real-time")
        print("2. Set the time")
        print("3. Set an alarm")
        print("4. Change display mode (12-hour/24-hour)")
        print("5. Pause/Resume the clock")
        print("6. Exit")

        choice = input("\nYour choice: ")  # Ask the user to choose an option

        if choice == "1":
            run_clock(clock)  # Run the clock in real-time

        elif choice == "2":
            try:
                # Ask the user to set a new time
                h = int(input("Hours (0-23): "))
                m = int(input("Minutes (0-59): "))
                s = int(input("Seconds (0-59): "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:  # Validate input
                    clock.set_time_from_tuple((h, m, s))  # Set the time with the tuple
                    run_clock(clock)  # Run the clock after setting the time
                else:
                    print("Invalid values.")  # Show an error message if values are invalid
            except ValueError:
                print("Invalid input.")  # Handle invalid input errors

        elif choice == "3":
            try:
                # Ask the user to set the alarm time
                h = int(input("Hours (0-23): "))
                m = int(input("Minutes (0-59): "))
                s = int(input("Seconds (0-59): "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:  # Validate input
                    clock.set_alarm((h, m, s))  # Set the alarm with the tuple
                    run_clock(clock)  # Run the clock after setting the alarm
                else:
                    print("Invalid values.")  # Show an error message if values are invalid
            except ValueError:
                print("Invalid input.")  # Handle invalid input errors

        elif choice == "4":
            clock.toggle_mode()  # Change the display mode (12-hour or 24-hour)

        elif choice == "5":
            clock.toggle_pause()  # Pause or resume the clock

        elif choice == "6":
            print("Goodbye!")  # Display a goodbye message
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice.")  # Show an error message for invalid choices


if __name__ == "__main__":
    menu()  # Start the main menu when the program is run