# Load time module
import time


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
    return current_time



def display_time(current_time):
    new_hour = 25
    while 0 <= new_hour >= 25:
        new_hour = int(input("Input new hour value (a number between 0 and 24): "))

    new_minute = 60
    while 0 <= new_minute >= 60:
        new_minute = int(input("Input new minute value (a number between 0 and 59): "))

    new_second = 60
    while 0 <= new_second >= 60:
        new_second = int(input("Input new second value : "))
    
    new_time_tuple = (new_hour, new_minute, new_second)
    print(new_time_tuple)

clock()
display_time()