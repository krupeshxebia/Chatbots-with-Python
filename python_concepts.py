#  TRY EXCEPT ----------------------------------------------------------------------------------------------
try:
    # some statement
except ErrorName:
    # some statement

def raises_value_error():
    try:
        print("First I Try this")
        raise ValueError
    except ValueError:
        print("You raised a ValueError!")
raises_value_error()

# Slice the pizza!
def pizza_serve(pizza_mass):
    try:
        num_slices = int(input("Serve the pizza as how many slices? "))
        slice_mass = pizza_mass / num_slices
    except ValueError:  # Input cannot be interpreted as an int.
        print("Enter an integer, please.")
        continue
    except ZeroDivisionError:  # Input was 0.
        print("Cannot serve it as zero slices.")
        continue
    if num_slices < 0:  # Input was negative.
        print("Cannot serve a negative number of slices.")
        continue
    break


# ZIP -----------------------------------------------------------------------------------------------
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)


# RANGE ---------------------------------------------------------------------------------------------
# range containing numbers starting at 0 and up to, but not including, 9
list1 = range(9)

# range called list2 with the numbers 0 through 7
list2 = range(0, 8)

my_range3 = range(1, 100, 10)
print(list(my_range3))
# [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

# List, Range, Zip review
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(4)


# SLICING ----------------------------------------------------------------------------------------------
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
middle = suitcase[2:4]

print(beginning)

# the first 3 elements of suitcase.
start = suitcase[:3]
# the final two elements of suitcase.
end = suitcase[-2:]

# select the list ['b', 'c'] from mylist:
mylist = ['a', 'b', 'c', 'd', 'e']
mylist[1:3]

# COUNT ------------------------------------------------------------------------------------------------
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

print(jake_votes)

# SORT ------------------------------------------------------------------------------------------------
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place',
             '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
# Sort addresses here:
addresses.sort()
print(addresses)
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
cities.sort()

#  SORTED ------------------------------------------------------------------------------------------------
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games)
print(games_sorted)

# REVIEW --------------------------------------------------------------------------------------------------
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]

inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]

twin_beds = inventory.count('twin bed')
inventory.sort()

# TUPLE --------------------------------------------------------------------------------------------------
my_info = ('Mike', 24, 'Programmer')
my_name = my_info[0]
my_occ = my_info[-1]

name, age, occ = my_info
one_element_tuple = (4,)

# LOOPs --------------------------------------------------------------------------------------------------
"""
- Loops that let us move through each item in a list, called for loops
- Loops that keep going until we tell them to stop, called while loops
- Loops that create new lists, called list comprehensions
"""

promise = "I will not chew gum in class"
#  Prints 5 Times
for i in range(5):
  print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

# BREAK
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# CONTINUE
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age<21:
    continue
  print(age)

# List Comprehension:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height>161]
print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [cel * 9/5 +32  for cel in celsius]
print(fahrenheit)

# LOOPs REVIEW
single_digits = list(range(0,10))
squares = []

for digit in single_digits:
  squares.append(digit**2)
print(squares)

cubes = [digit**3 for digit in single_digits]
print(cubes)