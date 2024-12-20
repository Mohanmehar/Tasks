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

    
