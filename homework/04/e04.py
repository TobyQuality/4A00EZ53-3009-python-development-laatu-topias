import random

def generate_lotto_numbers(min = 1, max = 40, amount = 7):
    if min > max:
        raise Exception("Min value must be greater than max value.")
    if min < 1:
        raise Exception("The value of min must be 1 or above")
    if amount > max:
        raise Exception("The chosen lotto row has to be less or equal to max number")
    
    lotto_row = set()
    while len(lotto_row) < amount:
        lotto_row.add(random.randint(min, max))
    
    return lotto_row

# outputs seven random unique numbers between 1 - 40
# print(generate_lotto_numbers(1, 40, 7))

# outputs seven random unique numbers between 1 - 40
# print(generate_lotto_numbers(min = 1, max = 40, amount = 7))

# outputs seven random unique numbers between 1 - 40
# print(generate_lotto_numbers())

# outputs four (4) random unique numbers between 1 - 10
# print(generate_lotto_numbers(min=1, max=10, amount=4))

# outputs six (6) random unique numbers between 1 - 6
# (which basically is 1 2 3 4 5 6)
# print(generate_lotto_numbers(min=1, max=6, amount=6))

# crashes (exception) the app, you cannot choose seven (7) unique numbers
# between 1 - 6.
# print(generate_lotto_numbers(min=1, max=6, amount=7))