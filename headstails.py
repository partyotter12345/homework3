#Headstails.py
#HMWK_3


import random

def flip():
    x = random.randrange(2)

    if x==0:
        print("Heads")
    else:
        print("Tails")

def main():
    for i in range(10):
        flip()

main()
