"""
Exercise from the course Learn Python 3 by Codecademy.com
__
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. 
This function should return the sum of the values of all even keys.
"""

def sum_even_keys(my_dictionary):
  list_values = [value for key, value in my_dictionary.items() if key%2==0]
  return sum(list_values)
