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
list2 = range(0,8)

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
