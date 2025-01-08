# print ('Hello, \nWorld!')

# What is in a Name?
# Take a person's name and return the first letter.

# name = input('What is your name?')
# print(name[:1])

# # Iterate through a string
# a = "Hello, World!"
# for c in a:
#     print(c)

# Excerpt From
# Python QuickStart Guide
# ClydeBank Media
# This material may be protected by copyright.

# For loops with a range
# for i in range(#):
    #//code to be executed

# Enumeration 

# for index, value in planets:
    #print('Planet ' + str(index) + ': ' = value)
# returns - Planet 0: Mercury // 'str(index + 1) returns - Planet 1: Mercury

#While

#i=0
# while i<10:
#         print (i)
#         i+=1

#99 Bottles Song

bottles = 99
while bottles > 0:
    print(str(bottles) + ' bottles of beer on the wall.')
    print(str(bottles) + ' bottles of beer.')
    bottles -= 1
    print('Take one down, pass it around.')
    print(str(bottles) + ' bottles of beer on the wall.')

bottle = 99
for bottle in range(99):
    print(str(bottle) + ' bottles of beer on the wall.')
    print(str(bottle) + ' bottles of beer.')
    print('Take one down, pass it around.')
    print(str(bottle) + ' bottles of beer on the wall.')