# ZIP - merge two or more lists

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)


# RANGE - generates numbers starting at 0 and ending at the number before the input.
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


# SLICING ---------------------------------------------------------------------------------
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

# COUNT ---------------------------------------------------------------------------------
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

print(jake_votes)

# SORT ---------------------------------------------------------------------------------
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

#  SORTED ---------------------------------------------------------------------------------
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games)
print(games_sorted)

# REVIEW ---------------------------------------------------------------------------------
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]

inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]

twin_beds = inventory.count('twin bed')
inventory.sort()
