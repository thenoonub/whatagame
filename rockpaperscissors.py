import random

options = ['rock', 'paper', 'scissors']

player1 = random.choice(options)
player2 = random.choice(options)
print("player1 has", player1, "player2 has", player2)

if player1 == player2:
    print("tie!")

if player1 == 'rock' and player2 == 'paper':
    print("player2 wins!")

if player1 == 'paper' and player2 == 'rock':
    print("player1 wins!")

if player1 == 'rock' and player2 == 'scissors':
    print("player1 wins!")

if player1 == 'scissors' and player2 == 'rock':
    print("player2 wins!")

if player1 == 'scissors' and player2 == 'paper':
    print("player1 wins!")

if player1 == 'paper' and player2 == 'scissors':
    print("player2 wins!")
