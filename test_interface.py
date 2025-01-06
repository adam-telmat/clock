# Load time module
import time
# Load interface module
import customtkinter

def clock():
    # The boucle While recharge the current_time value, 
    # print and wait one second to re-start the cycle
    while True:
        # Save the valeur in a variable
        current_time = time.strftime("%H:%M:%S")
        # Print the current time
        print(current_time)
        # Wait one second
        time.sleep(1) 

def button_set_alarm():
    print("Set Alarm!!!")

def button_set_time():
    print("Set time!!!")

def button_stop():
    print("Stop the time ;)")

app = customtkinter.CTk()
app.title("L'horlage de mamie")
app.geometry("500x300")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

button = customtkinter.CTkButton(app, text="Set Alarm", command=button_set_alarm)
button.grid(row=0, column=0, padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Set Time", command=button_set_time)
button.grid(row=0, column=1, padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Set Time", command=button_stop)
button.grid(row=0, column=2, padx=20, pady=20)

app.mainloop()