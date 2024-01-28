# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string

letters = ['a', 'b', 'c', 'd']
random_dicts = [{letter: random.randint(0,100) for letter in letters} for _ in range(10)]


# 2. get previously generated list of dicts and create one common dict:

# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

common_dict = {}

for letter in letters:
    max_value = max(d[letter] for d in random_dicts if letter in d)
    common_dict[letter] = max_value
