'''
name = 'Jennifer'
print(name[1:-1])
'''

# Price this a house is 1 million dollars

'''
good_credit = True
price = 1000000

if good_credit:
    price = price - (price * 0.10)
else:
    price = price - (price * 0.20)

print(f"\nThe new price you will pay is ${price:.2f}, because you have good credit.\n")
'''

'''
high_income = True
good_credit = True

if high_income and good_credit: # The 'and' operator requires both conditions to be true.
    print("\nEligible for loan because you have a high income and good credit\n")
else:
    ("\nYou're not eligible for loan\n")
'''

'''
high_income = True
good_credit = False

if high_income or good_credit: # The 'or' operator requires only one condition to be true.
    print("\nEligible for loan\n")
else:
    ("\nYou're not eligible for loan\n")
'''

'''
name = str(input("\nWhat's your name? ")).strip()

print(f"\nYour name have {len(name) - name.count(" ")} characters. ")

if len(name) - name.count(" ") < 3:
    print("\nName must be at least 3 characters\n")
elif len(name) - name.count(" ") > 50:
    print("\nName can be a maximium of 50 characters\n")
else:
    print("\nIt's a good name!\n")
'''
'''
i = 1
while (i <= 5):
    print(i)
    i += 1
print("\nDone")
'''

'''
command = ''
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("\nCar already started\n")
        else:
            started = True
            print("\nCar started\n")
    elif command == 'stop':
        if not started:
            print("\nCar already stopped\n")
        else:
            started = False
            print("\nCar stopped\n")
    elif command == 'help':
        print("\nstart - to start the car\nstop - to stop the car\nquit - to quit\n")
    elif command == 'quit':
        break
    else:
        print("\nSorry, i don't understand that")
'''
'''
list_of_names = ['Joao', 'Bya', 'Nilza', 'Fabiana']

for names in list_of_names:
    print(names)
'''

'''
prices = [10, 20 ,30]
total_price = 0
for price in prices:
    total_price += price
print(f"\nYou will pay {total_price:.2f}")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
'''

numbers = [5, 2, 7, 9, 8, 10, 6]
max = numbers[0]
for n in numbers:
    if n > max:
        max = n
print(max)