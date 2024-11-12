#COUNTDOWN Timer

import time

my_time = int(input("For how long(in seconds): "))

for i in range(my_time,0,-1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) #may add %24 when including days in f string -- next line
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")