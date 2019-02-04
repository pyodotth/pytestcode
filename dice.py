import random


def dice_int():
    while True:
        yield random.randint(1, 6)


if __name__ == "__main__":
    x = y = dice_int()
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
    print(f"Dice X : {next(x)} / Dice Y : {next(y)}")
