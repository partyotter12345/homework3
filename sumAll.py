#sumAll.py
#HMWK_3

sum = 0
num = int(input("Enter a number (enter 0 to end): "))
while num != 0:
    sum = sum + num
    num = int(input("Enter a number (enter 0 to end): "))

print("The sum is", sum)
