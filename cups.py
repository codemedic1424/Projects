price = input('What is the price of a cup of coffee?')
cups = input('How many cups do you want?')
#total = price * cups #need to convert to int
total = float(price) * int(cups)
print('Your total is $' + str(total) + ' for ' + cups + ' cups.')