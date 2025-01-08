# Import necessary modules
import time
import datetime
import customtkinter

def clock():
    """
    Update the label with the current time every second.
    """
    current_time = time.strftime("%H:%M:%S")
    label.configure(text=current_time)
    app.after(1000, clock)  # Schedule the clock function to run every 1000 ms (1 second)

##Creating an alarm
def set_alarm():
    #Asking grandma when she wants our alarm to ring
    alarm_time=input("Choose at what time the alarm should ring (HH:MM:SS): ")

    #Getting the hour, minutes, seconds from grandma's choice
    alarm_hour=alarm_time[:2]
    alarm_minute=alarm_time[3:5]
    alarm_seconds=alarm_time[6:8]

    print(f"Alarm has been set at {alarm_hour}:{alarm_minute}")

    #Infinite loop to watch over the hour
    while True:
        now=datetime.datetime.now()
        current_hour=now.strftime("%H")
        current_minute=now.strftime("%M")
        current_seconds=now.strftime("%S")

        #if every component of the settings grandma wants == the differents components of current time, then it should ring
        if alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds:
            print("Ding Ding Ding (de la prof d'anglais)")
            break

def button_set_time():
    """
    Function executed when the 'Set Time' button is clicked.
    Prints a message to the console.
    """
    print("Set time!!!")

def button_stop():
    """
    Function executed when the 'Stop' button is clicked.
    Prints a message to the console.
    """
    print("Stop the time ;)")

# Create the main application window
app = customtkinter.CTk()
app.title("L'horlage de mamie")
app.geometry("500x300")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Create and place the label to display the clock
label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 24))
label.grid(row=0, column=0, columnspan=3, pady=20)

# Create and place the buttons
button1 = customtkinter.CTkButton(app, text="Set Alarm", command=set_alarm)
button1.grid(row=1, column=0, padx=20, pady=20)

button2 = customtkinter.CTkButton(app, text="Set Time", command=button_set_time)
button2.grid(row=1, column=1, padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Stop", command=button_stop)
button3.grid(row=1, column=2, padx=20, pady=20)

# Start the clock function to update the time
clock()

# Start the main application loop
app.mainloop()
