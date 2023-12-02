import sys;
from getpass import getpass;
import locale;
locale.setlocale(locale.LC_ALL, '')
import math;
from datetime import datetime;
from utilities import importrl;
from utilities import inputfix;
from utilities import clear;

importrl()
inputfix()

def pause():
    print('')
    getpass("\033[94m[ Press ENTER or RETURN to try again! ]")
    print('')

def processYear(year):
    try:
        int(year)
        if year < 0:
            print('\033[91m' + str(year) + ' is below 0 and being processed - you should never see this!')
    except Exception as error:
        print('Caught this error: ' + repr(error))
        
    isOrIsNot = "is"
    leapYearOrLeapCentury = "a leap year"
    color = "92"
    totaldays = "29"

    # The majority of the population between 45 B.C. and 1582 A.D. used the 
    # Julian calendar. Today, we use the Gregorian calendar. The names shown
    # are written as they were made in their original language.
    if year > 1581:
        februaryOrFebruarius = "February"
    else:
        februaryOrFebruarius = "Februarius"

    # Leap centuries are divisible by 400. They did not exist until the Gregorian
    # calendar, which started in 1582.
    isCenturyLeapYear = year > 1581 and year % 400 == 0

    # This is kind of a big condition - comments to explain:
    #
    # The Julian calendar has a leap year every four years, but the Gregorian
    # calendar does not. The exception to the rule is when a year is divisible
    # by 100, but not by 400. This change lessens our discrepancy between 
    # astronomical time, but makes my life much harder.
    #
    # This condition will check if ONE of the following is true:
    # - If the year is 1581, AND the year is divisible by 100.
    # - If the year is not divisible by 4.
    # - If the year IS 4.
    # - If the year is 0.
    # 
    # Why if the year is 4?
    # As with everything, there was meddling - pontifices initially added a 
    # leap day every three years in the Julian calendar instead of four years.
    # This was eventually resolved, but scholars still disagree on whether or 
    # not 4 A.D. was counted as a leap year in the Julian calendar. Some even 
    # say that 7 A.D. is a leap year. I've manually set 4 A.D. as not a leap 
    # year to be safe, because everyone agrees that 8 A.D. *is* a leap year,
    # which would be the next leap year anyway.
    isNotRegularLeapYear = (year > 1581 and year % 100 == 0) or (not year % 4 == 0) or year == 4 or year == 0

    if isCenturyLeapYear:
        leapYearOrLeapCentury = "a leap century"
    elif isNotRegularLeapYear:
        isOrIsNot = "is not"
        color = "93"
        if year < 1582:
            leapYearOrLeapCentury = "a leap year"
        else:
            leapYearOrLeapCentury = "a leap year or a leap century"
        totaldays = "28"
    print("\033[" + color + "m" + str(year) + " " + isOrIsNot + " " + leapYearOrLeapCentury + "!\033[0m")
    print("\033[0m" + str(year) + "'s " + februaryOrFebruarius + " has " + totaldays + " days.")

while True:
    try:
        clear()
        print('\033[94mPress ENTER or RETURN to see whether it is currently a leap year.')
        print('\033[94mInput a year (starting from 0 A.D.) to get its year.')
        print('\033[94mInput "quit" to quit.')
        print('')
        year = raw_input('\033[0mEnter your input: ')
        print('')

        if year == 'quit':
            clear()
            sys.exit(0)
        
        emptyString = (bool(str(year)) == False) or (str(year).join(str(year).split()) == "")
        if emptyString:
            year = str(datetime.now().year)
        year = str(year).replace(locale.localeconv()["thousands_sep"], '')
        year = math.trunc(int(year))

        if year >= 0:
            processYear(year)
        else:
            print("\033[91m" + str(year) + " is not a valid year!\033[0m")
        pause()
    except ValueError:
        print("\033[91m" + str(year) + " is not a number!\033[0m")
        pause()
    except KeyboardInterrupt:
        print('')
        sys.exit(0)
        