import datetime
import time
from datetime import timedelta

def current_time():
    try:
        while True:
            current_time = datetime.datetime.now()
            print(current_time.strftime("%H:%M:%S"))
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRetour au menu")


#current_time()

def capture_new_time():
    h = int(input("Heures (0-23) : "))
    m = int(input("Minutes (0-59) : "))
    s = int(input("Secondes (0-59) : "))
    if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
        new_time_tuple = (h, m, s)
    else:
        print("Valeurs invalides.")
    return new_time_tuple

'''print(new_hour_tuple[0])
print(new_hour_tuple[1])
print(new_hour_tuple[2])'''


def afficher_heure(new_hour_tuple):
    h = new_hour_tuple[0]
    m = new_hour_tuple[1]
    s = new_hour_tuple[2]
    present_time = datetime.datetime.now()
    current_time = present_time.replace(hour=h, minute=m, second=s)
    print("Heure réglée avec succès.")
    print(current_time.strftime("%H:%M:%S"))



new_hour_tuple = capture_new_time()
afficher_heure(new_hour_tuple)