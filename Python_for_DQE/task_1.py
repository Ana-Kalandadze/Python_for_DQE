# create list of 100 random numbers from 0 to 1000

import random

random_numbers = [random.randint(0,1000) for _ in range(100)]

# sort list from min to max (without using sort())

for i in range(0, len(random_numbers)):
    for j in range(i+1, len(random_numbers)):
        if random_numbers[i] >= random_numbers[j]:
            random_numbers[i], random_numbers[j] = random_numbers[j],random_numbers[i]
 

# calculate average for even and odd numbers

even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

avg_even = sum(even_numbers) / len(even_numbers)
avg_odd = sum(odd_numbers) / len(odd_numbers)

# print both average result in console 

print(f'average of even numbers is {avg_even}\naverage of odd numbers is {avg_odd}')
