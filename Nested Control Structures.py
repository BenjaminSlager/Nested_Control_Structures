"""
Programer: Ben Slager
Date: 10.15.19
Program: Double for Loop

This program will nest a for loop inside of another for loop
"""


for i in range(3):
    print("Outer For Loop: " + str(i))
    for l in range(2):
        print('   Inner For Loop: '+ str(l))


print("\n***********\n")



"""
Programmer: Ben Slager
Date:10.23.19
Program: For Loop + While Loop

This program will incoporate a for loop embeeding a while loop in it

"""
for i in range(4):
    print("Outer For Loop: " + str(i))
    x = 6
    while x >= 0:
        print("    While Loop: " + str(x))
        x = x - 1







