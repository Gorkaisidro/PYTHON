def greet(name):
    print(f"Hello, {name}!")
greet("Gorka")

print("----")
numbers = [1,5,2,2,3,4,5,5,6,7]

#1. Write a function that takes a list of numbers as an argument and returns the sum of the odd numbers in the list.
def sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum(numbers))
print("----")

#2. Write a function that takes a list of numbers and returns a new list with unique elements of the first list.
def unique_numbers(numbers):
    list = []
    for i in numbers:
        if i not in list:
            list.append(i)
    return list
print(unique_numbers(numbers))
print("----")

#3. Write a function that takes a list and returns a new list with unique elements of the first list, in the same order.
#4. Write a function that takes a list of numbers and returns a new list with only the even numbers from the first list.
def even_numbers(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even
print(even_numbers(numbers))
print("----")

#5. Write a function that takes a list of numbers and returns a new list with only the odd numbers from the first list.
def odd_numbers(numbers):
    odd = []
    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
    return odd
print(odd_numbers(numbers))
print("----")

#6. Write a function that takes a list of numbers and returns a new list with only the prime numbers from the first list.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers(numbers):
    prime = []
    for i in numbers:
        if is_prime(i):
            prime.append(i)
    return prime
print(prime_numbers(numbers))
print("----")

#7. Write a function that takes a list of numbers and returns a new list with only the palindromes from the first list.