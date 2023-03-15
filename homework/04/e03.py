def generate_lotto_numbers(first_number, last_number):
    if first_number > last_number:
        raise Exception("First number of the lotto must be smaller than the last")
    if first_number < 1:
        raise Exception("First number cannot be zero or negative.")
    lotto_numbers = set()
    for i in range (first_number, last_number + 1):
        lotto_numbers.add(i)
    return lotto_numbers

# outputs seven random unique numbers (int) between 1 - 40
# print(generate_lotto_numbers(1, 40))

# outputs seven random unique numbers (int) between 1 - 50
# print(generate_lotto_numbers(1, 50))