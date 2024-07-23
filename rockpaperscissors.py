import random

print("Welcome to rock, paper, scissors!")
player1_name = input("What is player1's name? ")
player2_name = input("What is player2's name? ")

i = 1
while i != 0:
    options = ['rock', 'paper', 'scissors']

    player1 = random.choice(options)
    player2 = random.choice(options)
    print("player1 has", player1, "player2 has", player2)

    if player1 == player2:
        print("tie!")
        i = 1

    if player1 == 'rock' and player2 == 'paper':
        print(player2, "wins!")
        i = 0

    if player1 == 'paper' and player2 == 'rock':
        print(player1, "wins!")
        i = 0

    if player1 == 'rock' and player2 == 'scissors':
        print(player1, "wins!")
        i = 0

    if player1 == 'scissors' and player2 == 'rock':
        print(player2, "wins!")
        i = 0

    if player1 == 'scissors' and player2 == 'paper':
        print(player1, "wins!")
        i = 0

    if player1 == 'paper' and player2 == 'scissors':
        print(player2, "wins!")
        i = 0
