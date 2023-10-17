#1.Write a Python function that takes a tuple of numbers as input and returns a new
# tuple containing the square of each number in the original tuple.

def square_tuple(numbers):
  tupleList = []
  for i in numbers:
    num = i**2
    tupleList.append(num)
  return tupleList

numbers = (1, 2, 3, 4, 8)
result = square_tuple(numbers)
print(result)
print("----")

#2.Write a Python function that takes two sets as input and returns a new set containing the 
# elements that are common to both sets (intersection).

def set_intersection(set1, set2):
  return set1.intersection(set2)

set1 = {1, 2, 3, 4, 6}
set2 = {4, 5, 6, 7, 8}
result = set_intersection(set1, set2)
print(result)
print("----")

#3.Write a Python function that takes two dictionaries as input and returns a new dictionary 
# that is a merge of the input dictionaries. If there are common keys, use the values from the second dictionary.

def merge_dictionaries(dict1, dict2):
  dict1.update(dict2)
  return dict1

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(dict1["b"])
result = merge_dictionaries(dict1, dict2)
print(result)
print(dict1["b"])
print("----")

#4.Write a Python function that takes a list of strings as input and returns a dictionary where the keys 
# are the strings, and the values are the lengths of the strings.

def string_length_dictionary(strings):
  return {cadena: len(cadena) for cadena in words}

words = ["apple", "banana", "cherry"]
result = string_length_dictionary(words)
print(result)