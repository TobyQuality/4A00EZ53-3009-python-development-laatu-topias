from e04 import generate_lotto_numbers

user_lotto = {1, 2, 3, 4, 5, 6, 7}
random_lotto =  set()
highscore = 0
week = 1
year = 0

while highscore < 7:
    random_lotto = generate_lotto_numbers()
    weeks_highscore = len(user_lotto.intersection(random_lotto))

    if weeks_highscore > highscore:
        highscore = weeks_highscore
        print(f"You got {highscore} correct! New highscore!")
        print(f"It took {year} years.")

    week = week + 1
    if week == 53 :
        week = 1
        year = year + 1