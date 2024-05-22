import assistant_details
from speak_module import speak
from database import speak_is_on

def output(o):
    # command line output
    if speak_is_on():
        speak(o)
    print(assistant_details.name + ":" + o)
    print()

    if o is not None:
        return str(o)
    else:
        return ""