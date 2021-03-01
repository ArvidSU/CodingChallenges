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

    # Largest number not equaling 'number'
    a = 0

    count = 0
    while count < len(OrderedList):
        print(count + 1)
        a = OrderedList[-1 - count]
        if (number - a) in OrderedList:
            b = OrderedList[OrderedList.index(number - a)]
            return '%s + %s = %s' % (a, b, number)
        count += 1



print(RasmusTrorHanECool(9))