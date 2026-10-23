# A tuple of integers
# numbers = (1, 2, 3, 4, 5)
# print(f"Tuple of numbers: {numbers}") 
# print( type(numbers))

# A tuple of strings
# fruits = ("apple", "banana", "cherry")
# print(f"Tuple of fruits: {fruits}") 

# # A tuple with mixed data types
# mixed_tuple = ("hello", 123, 3.14, False, (23, 243, ["sf"]))
# print(f"Mixed tuple: {mixed_tuple}")

nested_tuple = (1, [2, 3], 4, "test")

# print( nested_tuple[1][0] )
nested_tuple[1][0] = 4
nested_tuple[1][1] = 5
# nested_tuple[2] = 8
print(nested_tuple)