'''
Assignment:

- Create a math calculator program
- It should:
  1. be able to calculate non whole number digits.
  2. takes in user input for the numbers.
  3. is able to calculate using all basic arithmetic operations(addition, subtraction, multiplication, division, power) - you can also go the extra mile by including roots.
  4. does not produce an error when user does not input a number.

- (optional): Create another type of calculator inside the program (example: BMI calculator, financial calculators, etc)
'''


a = "hello"

b = " world"

print(a+b)

#importing math module for extra functions
import math

#defining several functions for operations
def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
def exponent (a,b):
    return a**b
def sqrt (a):
    return math.sqrt(a)
def percentage (a,b):
    return (a*b) // 100
def remain (a,b):
    return a%b
def fact (a):
    return math.factorial(a)
def bmi (a,b):
    return a/(b**2)

#printing guide for users to read
print("Hello, I'm a calculator! (with restriction: each operation only allows at most, two inputs)")
print("What would you like me to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
print("6. Percentage")
print("7. Remainder")
print("8. Factorial")
print("9. Square root")
print("10. Body Mass Index Calculator")

#while loop to allow continuous different choices and less error
while True:
    #let the user choose what operation from the input
    choice=input("Choose an option: 1/2/3/4/5/6/7/8/9/10:")
    #conditional to determine operations that require 2 numbers
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        #try and except to prevent Invalid input, please try again! and no error message
        try:
            num1=int(input("Input your first number please:"))
            num2=int(input("Input your second number please:"))
        except ValueError:
            print("Invalid input, please try again! :(")
            continue
        #next conditional to actually perform operations with function calling depending on user choice
        if choice=='1':
            print(num1,'+', num2,'=', add(num1,num2))
        elif choice=='2':
            print(num1,'-',num2,'=', subtract(num1,num2))
        elif choice=='3':
            print(num1,'x', num2,'=', multiply(num1,num2))
        elif choice=='4':
            print(num1,'/',num2,'=', divide(num1,num2))
        elif choice=='5':
            print(num1, "to the power of", num2, "=", exponent(num1,num2))
        elif choice=='6':
            print(num1,"% of", num2,"=", percentage(num1,num2))
        elif choice=='7':
            print("Remainder of", num1, '/', num2, "=", remain(num1,num2))
    #operations 8 to 10 require 1 number or different values
    elif choice in ('8'):
        try:
            num1=int(input("Input your number please:"))
            print("The factorial of", num1, 'is', fact(num1))
        except ValueError:
            print("Invalid input, please try again! :(")
            continue
    elif choice in ('9'):
        try:
            num1=int(input("Input your number please:"))
            print("The square root of", num1, 'is', sqrt(num1))
        except ValueError:
            print("Invalid input, please try again! :(")
            continue
    elif choice in('10'):
        try:
            height=int(input("Please input your height in centimeters:"))
            weight=int(input("Please input your weight in kilograms:"))
            #converting height in cm to height in meters
            new_height=height/100
            result=bmi(weight,new_height)
            #rounding the result to have 1 significant figure
            rounded=round(result,1)
            print("Your BMI is", rounded, "kg/m^2")
            #next conditional (with 2 conditions that can be fulfilled) using "or"
            if rounded<=24.9 and rounded>=18.5:
                print("Fortunately, you are within the range of a healthy BMI!")
            else:
                print("Unfortunately your BMI is not within a healthy range :(")
        except ValueError:
            print("Invalid input, please try again! :(")
    else:
        print("Invalid input, please try again!, please try again!")
    #asking users if they would like to perform another operation
    next_calculation=input("Would you like to try again? (yes/no)")
    #prompting the code to end
    if next_calculation=='no':
        print("Thank you!")
        break
    elif next_calculation=='yes':
        continue
    else:
        print("Unknown input, goodbye!")
        break
        

    

