import os
from time import sleep
from datetime import datetime

def fecha():
    now = datetime.now()
    return "%d:%d:%d" %(now.hour,now.minute,now.second)

def padre():
    for x in range(10):
        
        sleep(10)

        pid = os.fork()

        if(pid == 0):
            hijo()
        else:
            pidHijo = pid
            print("Iniciando el proceso:",pidHijo,"a las",fecha())

def hijo():
    print("Iniciando el proceso con PID:",os.getpid())
    sleep(3)
    print("Terminando el proceso con PID:",os.getpid())
    os._exit(1)

if __name__ == "__main__":
    padre()