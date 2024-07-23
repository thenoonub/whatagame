# 0 5 10 15 20 
# 2 players guess a number in 5 of above number
# each hand can be 0 or 5, and calculate the total of 4 hands
# correct guess wins the game, and loser drinks
import random
winner = 0
# options = [0, 5, 10, 15, 20]
while winner == 0: 
    hands = [0, 5]
    player1 = int(input("player 1 guess a number in (0,5, 10, 15, 20): "))
    player2 = int(input("player 2 guess a number in (0,5, 10, 15, 20): "))
    print("player 1 guessed number: ", player1)
    print("player 2 guessed number: ", player2)
    player1_leftHand = random.choice(hands)
    player1_rightHand = random.choice(hands)
    player2_leftHand = random.choice(hands)
    player2_rightHand = random.choice(hands)
    print("player 1 left hand: " , player1_leftHand)
    print("player 1 right hand: ", player1_rightHand)
    print("player 2 left hand: " , player2_leftHand)
    print("player 2 right hand: ", player2_rightHand)
    sum = int(player1_leftHand + 
            player1_rightHand + player2_leftHand + player2_rightHand)

    if sum == player1:
        print("player 1 wins")
        winner = 1
    elif sum == player2:
        print("player 2 wins")
        winner = 2
    else:    
        print("no winner")