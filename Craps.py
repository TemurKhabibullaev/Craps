# Temur Khabibullaev
# 10/21/2019
import random
import time

# Balance

## According to the instructions, this should be a function definition to get the initial bankroll.
print('''
Welcome to Craps Game!
You will be asked the full amount of money from your bankroll.
And how much you will spend from it for your bet.
The Dice will be rolled!''')
print('ENTER your balance:')
balance = int(input('> '))

# Betting
print("Good! Let's start! Place how much you bet!")
bet = int(input('> '))


def finish():
    print('Good Job! Game is finished. Here is your balance:\n> ', total_amount)

## SHould not define a function inside a loop.  You can call the function in the loop if needed.
while bet <= balance:
    def rollDice():
        total_amount = balance - bet

        first_roll = random.randint(1,6)
        print('Rolling in the deep...')
        time.sleep(3)
        print('This is your first roll: ',first_roll)

        second_roll = random.randint(1,6)
        print('Rolling in the deep...')
        time.sleep(3)
        print('This is your second roll: ',second_roll)
        time.sleep(3)
        points = first_roll + second_roll
        print('And this is your final points: ',points)
        if points == 7 or points == 11:
            won_money = total_amount + bet * 2
            time.sleep(3)
            print('Wow! You won! Your balance is: ', won_money)
        elif points == 2 or points == 3 or points == 12:
            lost_money = total_amount - bet * 2
            time.sleep(3)
            print('You lost. This is your current balance: ', lost_money)
        else:
            print("You didn't loose nor win.")
            print('This is your balance now: ',total_amount)
    decision = input('Are we playing? Know- wins or loses will be cut from your balance. Enter an INTEGER only:\n1) Yes\n2) No\n> ')
    if int(decision) == 1:
        rollDice()
    elif int(decision) != 1:
        print('Good Luck!')
        break
