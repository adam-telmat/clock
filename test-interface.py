import customtkinter

def button_set_alarm():
    print("Set Alarm")

app = customtkinter.CTk()
app.title("L'horlage de mamie")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Set Alarm", command=button_set_alarm)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()