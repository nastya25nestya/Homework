from random import randint

rezults = []

initial_wins = [7, 11]
initial_looses = [2, 3, 12]
wins = [7]
looses = [4, 5, 6, 8, 9, 12]

for _ in range(10000000):
    roll = randint(1, 6) + randint(1, 6)
    if roll in initial_wins:
        rezults.append(1)
        continue
    elif roll in initial_looses:
        rezults.append(0)
        continue
    else:
        while roll not in (wins + looses):
            roll = randint(1, 6) + randint(1, 6)
        if roll in wins:
            rezults.append(1)
        elif roll in looses:
            rezults.append(0)
print(sum(rezults)/ len(rezults))