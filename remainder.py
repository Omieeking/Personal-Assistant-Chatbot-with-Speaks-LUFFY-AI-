
import subprocess
import datetime
import time
from plyer import notification
from speak_module import speak

def set_reminder_with_alarm(reminder_text, reminder_time_str):
    try:
        reminder_time = datetime.datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.datetime.now()
        time_difference = (reminder_time - current_time).total_seconds()
        if time_difference <= 0:
            # Time has already passed
            return None
        else:
            # Sleep until the reminder time
            time.sleep(time_difference)
            # Speak the reminder message three times
            for _ in range(3):
                speak(reminder_text)
            # Display a notification for the reminder
            notification.notify(title="Reminder", message=reminder_text, timeout=10)
            return {"text": reminder_text, "time": reminder_time_str}
    except ValueError:
        return None
# Example usage
# reminder_text = "Go to the market"
# reminder_time_str = "2024-05-01 16:37:00"
# reminder = set_reminder(reminder_text, reminder_time_str)
# if reminder:
#     print(f"Reminder set: {reminder['text']} at {reminder['time']}")
# else:
#     print("Invalid reminder format. Please use format: 'YYYY-MM-DD HH:MM:SS'")


#     remind me to submit the report at 2024-04-05 09:00:00

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])