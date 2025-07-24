'''
# Exercise EIGHT: Measurement converter
distance = float(input("Enter a distance in meters: "))
distance_km = distance / 1000
print(f"The distance in kilometers is: {distance_km:.2f}")

# Exercise Nine: Salary Adjustment
salary = float(input("\nWhat is the employee's salary? "))
salary_r = salary + (salary * 0.15)
print(f"The employee's salary with a 15% increase is: {salary_r:.2f}")

# Execise FOURTEEN: Temperature converter
temp_c = float(input("\nWhat is temperature in celsius degree? "))
temp_f = (temp_c * 9/5) + 32
print(f"The temperature in Fahrenheit is: {temp_f:.2f}")
'''
# Exercicse Twenty-One: Play a MP3 Music # Use Pygame

# Test with strings

'''In Python,strings are immutable, which means that once declared, it is not possible to make changes to their content. 
To modify a string, you need to create a new variable to store the new value of the string.'''

# test = str(input("Type a name: ")).strip()

'''Shows three sentence formats: capitalizing the beginning of a sentence, all lowercase, all uppercase,
and capitalizing the first letter of the sentence while keeping the rest lowercase'''
'''
print(f"{test.title()}\n{test.lower()}\n{test.upper()}\n{test.capitalize()}")

# Characters 0 to 4, also can be "[:5]"(5 is deleted)
print(f"{test[0:5]}") 

# Total length
print(f"{len(test)}") 

# Total length but without espaces
print(f"{len(test) - test.count(" ")}") 
'''

'''Counts how many times the lowercase letter 'o' appears.
You can also count within a specific interval, for example: test.count('o', 0, 5).'''
'''
print(f"{test.count('o')}")  

# Finds a specific group of letters and shows the starting position.
print(f"{test.find('joa')}")

# Indicates if it exists or not
print('lucas' in test)

# Replace the first name in parentheses(lucas) with the second(gabuxa)
print(f"{test.replace('lucas', 'gabuxa')}")

# Separate the string for a list in every space 
print(f"{test.split()}")

# In every space at the string, inside the hifen
print(f"{'-'.join(test)}")


print(f"{test}") # Shows origininal string


car_vel = float(input("\nWhat's the car's velocity? "))  
if car_vel > 80:  
    multa = (car_vel - 80) * 7  
    print(f"""\nYou received a traffic fine because your speed is {car_vel} km/h.  
You will pay ${multa:.2f}. """)  
print("\nBe careful when driving. Have a good day!")
'''
'''
num = int(input("\nType an integer number: "))  
if num % 2 == 0:  
    print("\nYour number is even.")  
else:  
    print("\nYour number is odd.")  
'''

dist = float(input("\nWhich is a distance this travel? "))

if dist <= 200:
    price = dist * 0.5
    print(f"\nThe passage's price is {price:.2f}")
else:
    price = dist * 0.45
    print(f"\nThe passage's price is {price:.2f}")