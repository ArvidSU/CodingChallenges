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
    a = 0
    b = 0
    for num in OrderedList:
        if (num > a and num < number):
            a = num

    for num in OrderedList:
        b = num
        if (a + b == number):
            break
    return [number, a, b]

print(RasmusTrorHanECool(6))