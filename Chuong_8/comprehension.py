# list
input_list = range(20)
list_using_comp = [var+1 for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)
# list
original_prices = [3.12, -2.32, 12.12, 13.14, -6.43]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)
# set
quote = "Python is easy"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
# dictionary
squares = {i: i * i for i in range(10)}
print(squares)