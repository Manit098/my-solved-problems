# Problem 1: Print "Hello, World!"
print("Hello, World!")

# Problem 2: Input and Print
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Problem 3: Sum of Two Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)

# Problem 4: Area of a Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("Area of the circle:", area)

# Problem 5: Check Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Problem 6: Factorial of a Number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Problem 7: Fibonacci Series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Problem 8: Reverse a String
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# Problem 9: Count Vowels in a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# Problem 10: Find Largest of Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print("Largest number is:", largest)

# Problem 11: Palindrome Check
word = input("Enter a word: ")
if word == word[::-1]:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")

# Problem 12: Count Words in a Sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# Problem 13: Sum of Digits
number = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in number)
print("Sum of digits:", digit_sum)

# Problem 14: Print Multiplication Table
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Problem 15: Check Prime Number
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(num, "is prime." if is_prime else "is not prime.")

# Problem 16: Find GCD of Two Numbers
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = math.gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", gcd)

# Problem 17: Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Problem 18: Count Consonants in a String
text = input("Enter a string: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = sum(1 for char in text if char in consonants)
print("Number of consonants:", count)

# Problem 19: Find the Length of a List
my_list = input("Enter elements of the list separated by space: ").split()
print("Length of the list:", len(my_list))
