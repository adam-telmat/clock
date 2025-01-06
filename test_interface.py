# Import necessary modules
import time
import customtkinter

def clock():
    """
    Update the label with the current time every second.
    """
    current_time = time.strftime("%H:%M:%S")
    label.configure(text=current_time)
    app.after(1000, clock)  # Schedule the clock function to run every 1000 ms (1 second)

def button_set_alarm():
    """
    Function executed when the 'Set Alarm' button is clicked.
    Prints a message to the console.
    """
    print("Set Alarm!!!")

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
button1 = customtkinter.CTkButton(app, text="Set Alarm", command=button_set_alarm)
button1.grid(row=1, column=0, padx=20, pady=20)

button2 = customtkinter.CTkButton(app, text="Set Time", command=button_set_time)
button2.grid(row=1, column=1, padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Stop", command=button_stop)
button3.grid(row=1, column=2, padx=20, pady=20)

# Start the clock function to update the time
clock()

# Start the main application loop
app.mainloop()
