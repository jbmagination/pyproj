from utilities import inputfix;
from utilities import importrl;
import locale;
import math;
import sys;

inputfix()
importrl()

def sumNumbers(num1: int, num2: int):
    num1Original = num1
    num2Original = num2
    if num1 > num2:
        num1 = num2Original
        num2 = num1Original
    del num1Original
    del num2Original
    
    print('Starting from ' + str(num1))
    attemptingToSum = True
    number = num1
    currentTotal = num1
    while attemptingToSum:
        previousTotal = currentTotal
        currentTotal = previousTotal + number
        print(str(previousTotal) + ' + ' + str(number) + ' = ' + str(currentTotal))
        if number == num2:
            print('Your result is ' + str(currentTotal))
            attemptingToSum = False
        number = number + 1

def processNumber(num: int):
    emptyString = (bool(str(num)) == False) or (str(num).join(str(num).split()) == "")
    if emptyString:
        print("\033[91mYou must provide a number!\033[0m")
        return False
    else:     
        num = str(num).replace(locale.localeconv()["thousands_sep"], '')
        try:
            num = math.trunc(int(num))
            if num < 0:
                print("\033[91mYour number must be greater than 0!\033[0m")
                return False
            return num
        except ValueError:
            print("\033[91m" + str(num) + " is not a number!\033[0m")
            return False

while True:
    try:
        num1 = raw_input('Please enter the first number: ')
        processNumber(num1)
        if not (processNumber(num1) == False):
            num1 = processNumber(num1)
        
        num2 = raw_input('Please enter the second number: ')
        processNumber(num2)
        if not (processNumber(num2) == False):
            num2 = processNumber(num2)
        
        if num2 - num1 == 0:
            print("\033[91mYour numbers must be different!\033[0m")
        else:
            sumNumbers(num1, num2)
    except ValueError as error:
        print("\033[91m" + str() + " is not a number!\033[0m")
    except KeyboardInterrupt:
        print('')
        sys.exit(0)