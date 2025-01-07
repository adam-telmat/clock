import time
import datetime
##Creating an alarm

def input_time_check(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        return True
    except ValueError:
        return False

def set_alarm():
    #Asking grandma when she wants our alarm to ring
    alarm_time=""
    while not input_time_check(alarm_time):
        alarm_time=input("Choose at what time the alarm should ring (HH:MM:SS): ")
        if not input_time_check(alarm_time):
                print("Grandma, you're getting old. You seem to have lost the ability to read an hour !")
    # return alarm_time

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