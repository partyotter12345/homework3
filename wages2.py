#wages2.py
#HMWK_3

def calcWeeklyWages(totalHours, hourlyWage):  #NEW
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    elif totalHours <=60:
        overtime = totalHours - 40
        regularHours = 40
    elif totalHours >60:
        doubleovertime = totalHours - 60
        regularHours =40
        overtime = 20
        
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime + (2*hourlyWage)*doubleovertime

def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.'
          .format(**locals()))

main()
