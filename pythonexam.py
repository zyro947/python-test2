import time
import winsound  # For Windows
import os  # For macOS/Linux
from datetime import datetime

# Alarm function
def play_alarm():
    if os.name == 'nt':  # Windows
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # macOS/Linux
        os.system("afplay alarm_sound.mp3")  # For macOS
        # os.system("mpg321 alarm_sound.mp3")  # For Linux if mpg321 is installed

# Pre-set GRWM task times
tasks = [
    {"task": "Brush Teeth", "time": "07:00"},
    {"task": "Pick Outfit", "time": "07:15"},
    {"task": "Make Breakfast", "time": "07:30"},
    {"task": "Pack Bag", "time": "07:45"},
    {"task": "Leave for Work", "time": "08:00"}
]

# Loop forever and check tasks
while True:
    current_time = datetime.now().strftime("%H:%M")
    
    # Check if it's time for any task
    for task in tasks:
        if current_time == task["time"]:
            print(f"Time to do: {task['task']}!")
            play_alarm()  # Play alarm sound
            tasks.remove(task)  # Remove the task from the list
    
    if not tasks:  # If no tasks left, we're done
        print("You're ready for the day!")
        break
    
    time.sleep(60)  # Wait for 60 seconds before checking again
