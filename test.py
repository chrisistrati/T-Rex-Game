import keyboard
import time
import pyautogui
# time.sleep(1)
# keyboard.press("down arrow")
# keyboard.release("down arrow")

# pyautogui.keyDown("down")

import win32api
import win32con

def press_key(key):
    """
    Press a key on the keyboard.
    
    Args:
    key: The key to press. Should be a virtual key code.
    """
    # Press the key
    win32api.keybd_event(key, 0, 0, 0)
    # Release the key
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

keyboard.press("down arrow")
