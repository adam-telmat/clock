import datetime
import time
from datetime import timedelta

def actual_time():
    try:
        while True:
            present_time = datetime.datetime.now()
            print(present_time.strftime("%H:%M:%S"))
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRetour au menu")

actual_time()