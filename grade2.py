#grade2.py
#HMWK_3

def letterGrade(score):
    if score < 59.5:
        letter = 'F'
    elif score < 69.5:
        letter = 'D'
    elif score < 79.5:
        letter = 'C'
    elif score < 89.5:
        letter = 'B'
    else:
        letter = 'A'
    return letter

def main():
    x = float(input('Enter a numerical grade: '))
    letter = letterGrade(x)
    print('Your grade is ' + letter + '.') 

main()
