import random

chosen_numbers = set()
while len(chosen_numbers) < 7:
    random_number = random.randint(1,40)
    chosen_numbers.add(random_number)

print(chosen_numbers)
