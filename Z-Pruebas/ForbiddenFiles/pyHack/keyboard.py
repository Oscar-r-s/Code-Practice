
import pynput
import time

# Disable mouse and keyboard events
mouse_listener = pynput.mouse.Listener(suppress=True)
mouse_listener.start()
keyboard_listener = pynput.keyboard.Listener(suppress=True)
keyboard_listener.start()

time.sleep(10)
# Enable mouse and keyboard events
mouse_listener.stop()
keyboard_listener.stop()