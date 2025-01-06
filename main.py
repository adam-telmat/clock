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



def display_time():
    print("Change the hour")
    new_hour = int(input("New hour: "))
    new_minute = int(input("New minute: "))
    new_second = int(input("New second : "))
    
    new_time_tuple = (new_hour, new_minute, new_second)
    print(new_time_tuple)

clock()
display_time()