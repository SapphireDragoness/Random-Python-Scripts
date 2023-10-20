import time

def timer(study=1275,pause=300,times=10): 
    i = 0
    while i < times:
        time.sleep(study)
        print('Get to work!\a')
        time.sleep(pause)
        print('Time for a small pause!\a')

print("If no input is given, I will use this preset: study for 25 minutes, pause for 5, repeat 10 times.\n"
      "Keep the script running in the background and turn on the speakers, or I won't be able to notify you!\n")

study = input("How long will your study session be (in minutes)? ")
pause = input("How long will your pause be (in minutes)? ")
times = input("How many loops? ") 

timer(int(study)*60,int(pause)*60,int(times)*60)

