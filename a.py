#Question 1

#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello " + user_name + "!")
hello_name("Bianca")

#Question 2
#
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    print (odd_numbers)
odd_numbers = list(range(1,100,2))
for value in range(1,100,2):
    print (value)
  
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):  
    print(a_list)
a_list = list(range(1,23000))
print (max(a_list))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2023)) 

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def are_consecutive_numbers(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i+1] - a_list[i] != 1:
            return False
    return True
numbers1 = [2, 3, 4, 5, 6, 7]
numbers2 = [1, 2, 4, 5]

print(are_consecutive_numbers(numbers1))
print(are_consecutive_numbers(numbers2))