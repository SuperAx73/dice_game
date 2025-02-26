import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_tot/Users/axielurendam/Desktop/ScreenTimeRecordal
def main():
    player1=input("Enter player 1's name\n")
    player2=input("Enter player 2's name\n")
    /Users/axielurendam/Desktop/ScreenTimeRecord
    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f'{player1} got {roll1} and {player2} got {roll2}')

    if roll1>roll2:
        print(f'{player1} wins')
    if roll2>roll1:
        print(f'{player2} wins')
    if roll1==roll2:
        print("It's a tie")
main()