# Load time module
import time

# The boucle While recharge the current_time value, 
# print and wait one second to re-start the cycle
while True:
    # Save the valeur in a variable
    current_time = time.strftime("%H:%M:%S")
    # Print the current time
    print(f"Hora actual: {current_time}")
    # Wait one second
    time.sleep(1)