import re

def intro():
    print('\nThis \"Split Calulator\" will take a variable number of splits')
    print('given by you and display the full time back. For example, if you')
    print('input 4 splits of 52 seconds each, 3:28.00 will be shown. You can')
    print('choose between splits all being the same time, or different times.\n')

def recieveInput():
    while True:
        splitLength = input('Please enter \'same\' for even splits, or \'diff\' for variable length splits: ')
        if splitLength == 'same':
            sameSplits()
            break
        elif splitLength == 'diff':
            diffSplits()
            break
        else:
            print('\n--Input does not match--\n')


def sameSplits():
    splitTalk()

    splitCount, splitLength = getSplitInfo(False)

    splitList = parseLength(splitLength)
    hours, minutes, seconds = calculateTime(splitCount, splitList, False)
    printTime(hours, minutes, seconds)

def diffSplits():
    splitTalk()
    print('A prompt will pop up for each split you\'d like to compute\n')
    #splitLength is a list of lists in this case, since each split is different
    splitCount, splitLength = getSplitInfo(True)
    lol = []

    for i in range(int(splitCount)):
        splitList = parseLength(splitLength[i])
        lol.append(splitList)

    h, m, s = calculateTime(splitCount, lol, True)

    printTime(h, m, s)

def splitTalk():
    print('\nEnter the number of splits and your split time below. You can enter your split')
    print('time with lower case m, and/or s, such as 6m 12s. You can also enter the split')
    print('in stopwatch notation, such as 6:12')
    print('This Calculator does not take splits longer than 1 hour\n')

def getSplitInfo(diff):
    while True:
        try:
            splitCount = int(input('How many splits are we working with? '))
            break
        except ValueError:
            print('Input entered is not a number. Please try again')

    if diff:
        lol = []
        for i in range(int(splitCount)):
            while True:
                splitLength = input('Enter your split time here: ')
                if 'm' not in splitLength and 's' not in splitLength and ':' not in splitLength:
                    print('Incorrect format used. Please try again')
                else:
                    lol.append(splitLength)
                    break
        return splitCount, lol
    else:
        while True:
            splitLength = input('Enter your split time here: ')
            if 'm' not in splitLength and 's' not in splitLength and ':' not in splitLength:
                print('Incorrect format used. Please try again')
            else: break

        return splitCount, splitLength

def parseLength(splitLength):
    # Split on either an m, s, or colon for the time
    splitList = re.split('m |s|:', splitLength)

    while '' in splitList:
        splitList.remove('')

    return splitList

def calculateTime(splitCount, splitList, diff):
    initialMinutes = initialSeconds = -1
    countedMinutes = countedSeconds = hours = 0

    if len(splitList) == 2:
        initialMinutes = int(splitList[0])
        initialSeconds = int(splitList[1])
    elif len(splitList) == 1:
        initialSeconds = int(splitList[0])

    if diff:
        for l in splitList:
            if len(l) > 1:
                countedMinutes = countedMinutes + int(l[0])
                countedSeconds = countedSeconds + int(l[1])
            if len(l) == 1:
                countedSeconds = countedSeconds + int(l[0])
    else:
        for split in range(splitCount):
            if initialMinutes != -1:
                countedMinutes = countedMinutes + initialMinutes
            if initialSeconds != -1:
                countedSeconds = countedSeconds + initialSeconds

    if countedSeconds > 60:
        countedMinutes = countedMinutes + (countedSeconds // 60)
        countedSeconds = countedSeconds % 60

    if countedMinutes > 60:
        hours = countedMinutes // 60
        countedMinutes = countedMinutes % 60

    return hours, countedMinutes, countedSeconds

def printTime(hours, minutes, seconds):
    if minutes == 0:
        print('\nTotal time is:\t{} SECONDS\n'.format(seconds))
    elif hours == 0:
        print('\nTotal time is:\t{} MINUTES {} SECONDS\n'.format(minutes, seconds))
    else:
        print('\nTotal time is:\t{} HOURS {} MINUTES {} SECONDS\n'.format(hours, minutes, seconds))

if __name__ == '__main__':
    intro()
    recieveInput()
