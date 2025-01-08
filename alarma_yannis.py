import time
import datetime
##Creating an alarm

def set_alarm():
    #Asking grandma when she wants our alarm to ring
    alarm_time=input("Choose at what time the alarm should ring (HH:MM:SS): ")

    #Getting the hour, minutes, seconds from grandma's choice
    alarm_hour=alarm_time[0:2]
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

#To launch it
set_alarm()