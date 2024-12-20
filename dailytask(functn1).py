<<<<<<< HEAD
#.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(names):
    for name in names:
        print(f"Hello, {name}!")

greet(["mohanmehar"])

#.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add_numbers(a,b):
    return a + b
numbers = [(10,20),(20,30)]
for number in numbers:
    result = add_numbers(number[0], number[1])

    print(f"Sum of {number[0]} and {number[1]} is {result}")   

    
#Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(number):
    return number %2 == 0
m1 = is_even(6)
m2 = is_even(5)
m3 = is_even(8)

print("6 is even number",m1)
print("5 is even number",m2)
print("8 is even number",m3)

#Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
#def factorial():


#Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
def find_max(x,y,z):

    return max(x,y,z)


print(find_max(10,30,50))
print(find_max(7.5,9,6.8))
print(find_max(-5,-6,-9))
print(find_max(100,500,250))

#Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(m):
    count = 0
    for char in m:
        if char in 'aeiouAEIOU':
            count += 1

        return count
print(count_vowels("MoHAN MehAr"))

#Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise        

def is_prime(m):
    if m <= 1:
        return False

    for i in range(2, int(m**0.5) + 1):
        if m%1 == 0:
            return False
        return True

print(is_prime(2))  
print(is_prime(1))
print(is_prime(5))
print(is_prime(4))  

#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(m):
    if m <= 0:
        return 0
    else:
        return m + recursive_sum(m-1)

print(recursive_sum(12))
print(recursive_sum(20))
print(recursive_sum(0))             


# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result

def calculator(num1,num2,operator):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

print(calculator(10,20,"+"))
print(calculator(10,20,"-"))
print(calculator(10,20,"*"))
print(calculator(10,20,"/"))   
print(calculator(10,0,"/"))
print(calculator(10,20,"=="))  


#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
 
def find_common_elements(list1,list2):

    return list(set(list1)&set(list2))

print(find_common_elements([1,2,3,4],[4,3,2,5])) 
print(find_common_elements([7,6,8,9],[1,5,6,9]))
print(find_common_elements([1,2,2,1],[2,1,3,4]))
print(find_common_elements([8,9,3,4],[]))    
   
#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
       
def reverse_string(m):
    return m[::-1]

print(reverse_string("mehar"))    

#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
def sort_dict_by_value():

    return sorted(d.items(),key=lambda x:x[1])

print(sort_dict_by_value({'a': 6,'b':7, 'c':8}))
print(sort_dict_by_value({'x':3,'y':1,'z':2}))
print(sort_dict_by_value({'apple':50,'orange':30, 'grapes':20}))
 
 
 
=======
#.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(names):
    for name in names:
        print(f"Hello, {name}!")

greet(["mohanmehar"])

#.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add_numbers(a,b):
    return a + b
numbers = [(10,20),(20,30)]
for number in numbers:
    result = add_numbers(number[0], number[1])

    print(f"Sum of {number[0]} and {number[1]} is {result}")   

    
>>>>>>> cefb354b3a0cacf114eaf95c5635a19047049ab1
