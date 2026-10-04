# Practicing Sesison:
while True:
    change = float(input("Change: "))
    if change >= 0:
        break

cents = round(change * 100)
coins = 0

for coin in [25, 10, 5, 1]:
    coins += cents // coin
    cents %= coin

print(coins)