import random

# quick & dirty ( ͡° ͜ʖ ͡°)
def generateOL(length):
    OrderedList = []
    while len(OrderedList) < length:
        rnd = random.randint(1, length)
        OrderedList.append(rnd)
    OrderedList.sort()
    return OrderedList

# Finds two integers in an ordered list that added together equals given number
def RasmusTrorHanECool(number):
    OrderedList = generateOL(number)
    print(OrderedList)
    
    # Find the largest number in list that is less than the given number.
    index = 0

    # Checks list from 'index' if any value ahead added to number at index equals 'number'
    # Worst case, non are found
    while index < len(OrderedList):
        num = OrderedList[index]
        for i in range(index, len(OrderedList)):
            print(num, OrderedList[i], num + OrderedList[i])
            if num + OrderedList[i] == number:
                return '%s + %s = %s' % (num, OrderedList[i], number)

        index += 1


print(RasmusTrorHanECool(9))