import time

def countdown(int):
    i = int
    while i >= 1:
        print(f'{i} SECOND(S)!')
        if(i == 1):
            print("HAPPY NEW YEAR!")
        i -= 1
    
def countdown_with_sleep(int):
    i = int
    while i >= 1:
        print(f'{i} SECOND(S)!')
        if(i == 1):
            print("HAPPY NEW YEAR!")
        time.sleep(1)
        i -= 1
        






