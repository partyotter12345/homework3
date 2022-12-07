#savings.py
#HMWK_3

#initbalance = float(input("What is your initial balance?")
#annpercent = float(input("What is your annual percentage for interest as a decimal, like .04 for 4%")
#finalbalancewant = float(input("What is the final balance you desire?"))


import pygame
import sys
pygame.init()

# set window size
size = width, height = 640, 480

# set window caption
pygame.display.set_caption("Cat Moves with Mouse")

# set window background color
screen = pygame.display.set_mode(size)
bg = (20, 20, 20)

# set cat image
catImg = pygame.image.load('cat.png')
catx = 320
caty = 240
direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # get mouse position
    mx, my = pygame.mouse.get_pos()

    # move the cat
    if mx > catx:
        catx += 1
    if mx < catx:
        catx -= 1
    if my > caty:
        caty += 1
    if my < caty:
        caty -= 1

    # draw background
    screen.fill(bg)
