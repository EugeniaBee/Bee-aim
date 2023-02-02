#imports
import keyboard as kb
import time
import random

#variables

#functions

def react(key):
    while True:
        print('Press shift to start.')
        kb.wait("shift")
        time.sleep(random.uniform(0.5, 5))
        print('uwu')
        startcounter = time.monotonic()
        kb.wait("shift")
        endcounter = time.monotonic()
        print('Reaction time is {:>9.4f}'.format(endcounter - startcounter))
        time.sleep(0.5)
        if(kb.is_pressed(key)):
            print('Closing game. Thanks for playing.')
            main()

#main
def main():
    print('Choose the game:')
    print('React')

    s = input()
    if (s == 'react' or s == 'React'):
        react('ctrl')

main()
