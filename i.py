import time
import threading

def show():
    for i in range(20):
        print(i)
        time.sleep(0.5)
        i+=1
        print("\033c", end="")
    print(i)
if __name__ == "__main__":
    show()