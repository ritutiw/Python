"""
Below is a python scipt used to generate the overall time
consumed for mobile production optimized using Greedy Algorithm

The input file is of the format - 1/2/3
"""

# Triggering the open function to open the file in the read mode.
# Splitting the records based on newline character
# Assigning the records to a variable

textLines = open('C:/Users/rkuma767/Desktop/ASSIGNMENT1_BLR_GROUP073/inputPS1.txt', 'rt').read().split('\n')
# An empty list is being assigned to a variable
mobiles = []
# Looping through the file variable N times
# Looping and splitting records based on the delimeter and creating a tuple
for line in textLines:
    mobiles.append(tuple([int(i) for i in line.split('/')]))
# print('INPUT: ', mobiles)  # input list
# Triggering the open function to open the file in the write mode.
f = open('C:/Users/rkuma767/Desktop/ASSIGNMENT1_BLR_GROUP073/outputPS1.txt', 'w')
f.write('Mobiles should be produced in the order: ')
f.close()
# List that would be ordered is taken empty initial
ordered = []
# Assembly unit time for the first iteration before manufacturing is taken as 0
Alast = 0
"""
#Looping through the input dataset to order the mobiles based on
manufacturing time and we can minimize time for production by
having mobiles manufactured and send to assembly unit time in a queue
"""
for x in range(len(mobiles)):
    minDiff = 10**10  # Assumption for initial time as a very high value
    for index, mobile in enumerate(mobiles):
        (i, PMi, Ai) = mobile
        diff = PMi-Alast
        if(diff < minDiff):
            minDiff, nextMobile, nextMobilePos = diff, mobile, index

    ordered.append(nextMobile)
    mobiles.pop(nextMobilePos)
    Alast = Ai
    """
    once we are done with the ordering - we do not considered that record
    anymore and hence the same is popped of from the stack
    """

f = open('C:/Users/rkuma767/Desktop/ASSIGNMENT1_BLR_GROUP073/outputPS1.txt', 'a')
# order of mobile production is printed out to output file
f.write(','.join([str(i[0]) for i in ordered]))
# print('Mobiles should be produced in the order: ', ','.join([str(i[0]) for i in ordered]))
f.close()
# totalIdleTime and ProductionTime is assumed to be Zero initially
totalIdleTime, ProdTime, Alast = 0, 0, 0
# print('\n', '-'*30, 'FOR UNDERSTANDING', '-'*30)
# Print('ORDERED LIST: ', ordered, '\n\n')  # ordered list
"""
Ordered is a List - Hence we take corresponding indexes to
compute the corresponding time
"""
for mobile in ordered:
    totalIdleTime += mobile[1]-Alast
    ProdTime += mobile[1]+mobile[2]-Alast
    Alast = mobile[2]
f = open('C:/Users/rkuma767/Desktop/ASSIGNMENT1_BLR_GROUP073/outputPS1.txt', 'a')
f.write('\nIdle Time of Assembly Unit: {} \n'.format(totalIdleTime))
f.write('Total production time of all mobiles is: {} \n'.format(ProdTime))
# results are outputted to outputPS1.txt file
# print('Idle Time of Assembly Unit: ', totalIdleTime)
# print('Total production time of all mobiles is: ', ProdTime)
f.close()
