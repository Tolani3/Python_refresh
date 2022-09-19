import copy

# Arithmetic Operaters
print(1+1)
print(1-1)
print(5*10)
print(10/5)
print(10//5)#Integer divison
print(((6+9)*3)+3)
print(6 % 2)#Modulus gives you the remainder Ans=0
print(6 ^ 2)
print(6 ** 2)#6 to the power of 2

# Variables - snake_case
age = 25

#Integers are immutable
a = 1
b = a
a = "POOL"
print(a,b)

a = 1
b = a
a = a-1

#Lists are mutable
list_1 = [1, 2, 3]
list_2 = list_1
list_2 = [4, 5, 6]
print(list_1)
print(list_2)

list_1 = [1 ,2, 3]
list_2 = list_1
list_2[0] = -1
print(list_2)

#Copies - Shallow Copy
a = [1, 3, 5, 7]
b = copy.copy(a)
b[0] = -1
print(a)
print(b)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a,b]
d = copy.copy(c)
a[0] = -1
c[0][1] = -3
print(d)

#Copies - Deep Copy
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a,b]
d = copy.deepcopy(c)
a[0] = -1
c[0][1] = -3
print(d)

#Equality of objects ==, is
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print (a == b)
print (a == c)
print (a is b)
print (a is c)


#Problems with dynamically typed languages
a = [1, 2, 3]
a = 1
#a[0] = 1

#Variables
age, name, gender = 22, "Tolani", "Male"
blood_type = "Targeryon"


#region Numeric data types
bank_balance = 50000000000
print(bank_balance)

x = 7
y =3
z = x/y
print(z)
print(type(z))

w = int (3.7)
some_value = float(3)

#region Strings
name = "Tolani"
print(name)
print(type(name))

dialogue = 'Luke said "Hello World"'
dialogue = 'Luke said "Hello World", to which the world responded with "You\'re the best Luke"'

segment_one = "I\'m getting old"
segment_two = " Yes?"
full_sentence = segment_one + segment_two
print(full_sentence)
print(len(full_sentence*10))


#region Booleans
this_course_is_the_best = True
this_course_is_not_the_best = False

comparison = 1 > 2
print(comparison)

print((1 < 2) and (2 < 3))
print((1 < 2) or (2 > 3))
print((1 < 2) or (2 < 3))
print(not(1 < 2))


#region Methods
movie_title = "Nope"
print(movie_title.upper())
print(movie_title.lower())
print(movie_title.count('a'))


#region Collections - Lists
names = ["Gemma", "Tadas", "Luke"]
print(names[0])
#print(names[100])
random_variables = [True, False, "Hello", 3, 3.3]
print(len(random_variables))
length = len(random_variables)
print(random_variables[-1])

#Slicing
ordered_numbersLong = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ordered_numbers = list(range(0,11))
print(ordered_numbers)
print(ordered_numbers[0:5])
print(ordered_numbers[:7])
print(ordered_numbers[2:])


every_fifth = list(range(0, 101, 5))
print(every_fifth)

months = ["Jan", "Feb", "Mar"]
print("Jan" in months)
print("Jun" in months)

course = "Smart Tech"
print("art" in course)

#Endregion


numbers = [1, 2, 3, 4]
print(len(numbers))
print(max(numbers))

the_very_bad_list = ["Luke","Liam","Richard","Aaron","Tadas"]
print(max(the_very_bad_list))
print(sorted(the_very_bad_list))




























