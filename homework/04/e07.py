from e06 import lotto_user_input
from e04 import generate_lotto_numbers

# player must give numbers via console  (using e06's function)
user_lotto = lotto_user_input()
print(f"Your lotto row is:\n{user_lotto}")

# the method from e05 will be modified
# so that the costs and wins from lottos will be taken into account
costs = 0
wins = 0
random_lotto =  set()
highscore = 0
week = 1
year = 0

while highscore < 7:
    costs = costs + 1
    random_lotto = generate_lotto_numbers()
    weeks_highscore = len(user_lotto.intersection(random_lotto))

    if weeks_highscore == 4:
        wins = wins + 10
    if weeks_highscore == 5:
        wins = wins + 30
    if weeks_highscore == 6:
        wins = wins + 1000
    if weeks_highscore == 7:
        wins = wins + 3000000

    if weeks_highscore > highscore:
        highscore = weeks_highscore
        print(f"You got {highscore} correct! New highscore!")
        print(f"It took {year} years.")

    week = week + 1
    if week == 53 :
        week = 1
        year = year + 1

total_wins = wins - costs
print(f"Wow dude, you won {total_wins} euros! (not taking inflation and the devaluation of the currency into account)")