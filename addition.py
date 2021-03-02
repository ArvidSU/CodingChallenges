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
def findNumbers(OrderedList, number):
    print(OrderedList)
    print("Number: ", number)

    aInd = 0
    bInd = len(OrderedList) - 1
    for i in range(1, len(OrderedList)):
        a = OrderedList[aInd]
        b = OrderedList[bInd]

        if b >= number:
            bInd -= 1
        
        if a + b < number:
            aInd += 1
        
        if a + b == number:
            return a, b

print(findNumbers(generateOL(random.randint(4,15)), random.randint(2,15)))
