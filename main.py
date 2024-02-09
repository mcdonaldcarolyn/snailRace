import random, time, sys

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20 
FINISH_LINE = 40

print(''' snail race by invent with python''')

while True:
    print('How many snails will Race? Max:', MAX_NUM_SNAILS)
    response = input('>')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number 2 and', MAX_NUM_SNAILS)

snailNames = []
for i in range (1, numSnailsRacing + 1):
    while True:
        print('Enter snail #' + str(i) + "'s name: ")
        name = input('>')
        if len(name) == 0:
            print ('please enter a mame.')
        elif print in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break 
    snailNames.append(name)

print('\n' * 40)
