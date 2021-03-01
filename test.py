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
def RasmusTrorHanECool(OrderedList, number):
    #OrderedList = generateOL(number)
    print(OrderedList)
    print("Number: ", number)

    a = 0
    for i in range(1, len(OrderedList)):
        if (OrderedList[-i] < number):
            a = OrderedList[-i]
    print(a)
    for i in range(0, len(OrderedList)):
        if (OrderedList[i] + a == number and a != number and OrderedList[i] != number):
            return OrderedList[i], a

print(RasmusTrorHanECool([2,3,4,7], 2))
print(RasmusTrorHanECool([2,3,4,7], 7))
print(RasmusTrorHanECool([4,5,7,9,13], 9))
print(RasmusTrorHanECool([4,5,7,9,13], 12))
