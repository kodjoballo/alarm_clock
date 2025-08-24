import playsound
from playsound import playsound
import time


CLEAR = "\033[2J"
#CLEAR_AND_RETURN= "\033[H"
CLEAR_AND_RETURN = "\033[H\033[J"



"""
if the module is not getting installed, run 
python -m install playsound 
if not, python.exe -m install playsound
if not pip install --upgrade wheel 
pip install --upgrade setuptools wheel
pip install playsound
"""

def alarm_clock(seconds):
    elapsed_time = 0
    print(CLEAR)  # to clear the screen, however it's going on another line, we'll use the other clear_and_return to have the next
    # output on the same line
    while elapsed_time < seconds:
        time.sleep(1)
        elapsed_time += 1
        time_left = seconds - elapsed_time
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Time left before Alarm clock {minutes_left:02d}:{seconds_left:02d}")

        # this CLEAR_AND_RETURN is only working in the terminal not with RUN, it's due to the ANSI code not
        # working properly. Alternatively will be to import new module but we don't wanna make this more complex
        # we can use print("\n *100) in order to push the previous display up

    playsound("alarm.mp3")

print("******************************************")
print("**************Alarm Clock ****************")
print("******************************************")
print()

minutes = int(input("Please provide the minutes: "))
seconds = int(input("Please provide the seconds: "))

# Let's assume that the user will enter an integer

total_time = (minutes * 60) + seconds

alarm_clock(total_time)


