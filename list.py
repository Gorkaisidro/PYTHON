
favorite_foods = ["pizza", "jomon", "hamburguesa"]

#2. Add a food to the beginning and end of the list.

favorite_foods.insert(0, "kebab")
favorite_foods.append("sushi")

#3. Print the list and make sure the new items were added.
print(favorite_foods)
print("----")

#4. Print the second item in the list.
print(favorite_foods[1])
print("----")

#5. Print the last item in the list.
print(favorite_foods[-1])
print("----")

#6. Change the second item in the list to something new.
favorite_foods[1] = "Salmon"
print(favorite_foods)
print("----")

#7. Remove the last item from the list & print the new list.
favorite_foods.pop(-1)
print(favorite_foods)
print("----")

#8. Create a list of numbers from 1 to 10.
numeros = list(range(1,11))

#9. Print the numbers 1 to 5.
print(numeros[0:5])
print("----")

#10. Print the even numbers from the list.
for i in numeros:
    if i % 2 == 0:
        print(i)
print("----")
print(numeros[1::2])
print("----")

#11. Print the odd numbers from the list.
for i in numeros:
    if i % 2 != 0:
        print(i)
print("----")
print(numeros[::2])
print("----")

#12. Print the multiples of 5 from the list.
for i in numeros:
    if i % 5 == 0:
        print(i)
print("----")
print(numeros[4::5])
print("----")