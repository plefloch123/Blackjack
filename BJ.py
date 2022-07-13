#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Pierre Le Floch
# Created Date: 13/07/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" This is the first Version of my Blackjack Game"""
# ---------------------------------------------------------------------------
# Imports random
# ---------------------------------------------------------------------------

import random

# Creating the deck card
Card_Deck = {"Ace_of_Clubs": [1, 11], "Two_of_Clubs": 2, "Three_of_Clubs": 3, "Four_of_Clubs": 4, "Five_of_Clubs": 5,
             "Six_of_Clubs": 6, "Seven_of_Clubs": 7, "Eight_of_Clubs": 8, "Nine_of_Clubs": 9, "Ten_of_Clubs": 10,
             "Jack_of_Clubs": 10, "Queen_of_Clubs": 10, "King_of_clubs": 10, "Ace_of_Diamonds": [1, 11],
             "Two_of_Diamonds": 2, "Three_of_Diamonds": 3, "Four_of_Diamonds": 4, "Five_of_Diamonds": 5,
             "Six_of_Diamonds": 6, "Seven_of_Diamonds": 7, "Eight_of_Diamonds": 8, "Nine_of_Diamonds": 9,
             "Ten_of_Diamonds": 10, "Jack_of_Diamonds": 10, "Queen_of_Diamonds": 10, "King_of_Diamonds": 10,
             "Ace_of_Hearts": [1, 11], "Two_of_Hearts": 2, "Three_of_Hearts": 3, "Four_of_Hearts": 4,
             "Five_of_Hearts": 5, "Six_of_Hearts": 6, "Seven_of_Hearts": 7, "Eight_of_Hearts": 8, "Nine_of_Hearts": 9,
             "Ten_of_Hearts": 10, "Jack_of_Hearts": 10, "Queen_of_Hearts": 10, "King_of_Hearts": 10,
             "Ace_of_Spades": [1, 11], "Two_of_Spades": 2, "Three_of_Spades": 3, "Four_of_Spades": 4,
             "Five_of_Spades": 5, "Six_of_Spades": 6, "Seven_of_Spades": 7, "Eight_of_Spades": 8, "Nine_of_Spades": 9,
             "Ten_of_Spades": 10, "Jack_of_Spades": 10, "Queen_of_Spades": 10, "King_of_Spades": 10,
             }

#  Adjust few values
k = 1
i = 2
j = 1

# The Game Starts

# Player takes two random cards
player_card = random.sample(list(Card_Deck.items()), 2)
# If the first card of the dealer is an Ace
if player_card[0][1] == [1, 11]:
    player_score = player_card[0][1][1] + player_card[1][1]
# If the second card of the dealer is an Ace
elif player_card[1][1] == [1, 11]:
    player_score = player_card[0][1] + player_card[1][1][1]
# If both cards of the dealers are Ace
elif player_card[0][1] == [1, 11] and player_card[1][1] == [1, 11]:
    player_score = player_card[0][1][0] + player_card[1][1][1]
# If the dealer do not draw any Ace
else:
    player_score = player_card[0][1] + player_card[1][1]
print("The Player hand is ", player_card[0][0], " and ", player_card[1][0], "\nThe Player Score is ", player_score)

Card_Deck.pop(player_card[0][0])
Card_Deck.pop(player_card[1][0])

# Dealer takes one cards
dealer_card = random.sample(list(Card_Deck.items()), 1)
# If the first card of the dealer is an Ace
if dealer_card[0][1] == [1, 11]:
    dealer_score = dealer_card[0][1][1]
# If the dealer do not draw any Ace
else:
    dealer_score = dealer_card[0][1]

print("The dealer hand is ", dealer_card[0][0], "\nThe dealer Score is ", dealer_score)

if player_score == 21:
    while dealer_score < 16:
        dealer_card.append(random.choice(list(Card_Deck.items())))
        print("The dealer drew the card ", dealer_card[k][0])
        Card_Deck.pop(dealer_card[k][0])
        if dealer_card[k][1] == [1, 11]:
            if dealer_score <= 10:
                dealer_score = dealer_score + dealer_card[k][1][1]
                print("The dealer score is ", dealer_score)
            else:
                dealer_score = dealer_score + dealer_card[k][1][0]
                print("The dealer score is ", dealer_score)
        else:
            dealer_score = dealer_score + dealer_card[k][1]
            print("The dealer score is ", dealer_score)
        k += 1
    if dealer_score == player_score:
        print("It's a Tie !")
    else:
        print("You won !!")

Card_Deck.pop(dealer_card[0][0])

# The player is given a Choice, either Stand or Hit

while player_score < 21:
    choice = input("Please choose 'Hit' or 'Stand': ").lower()
    # If the Choice is not clear, ask again
    while choice not in ["h", "s", "hit", "stand", "H", "S", "Hit", "Stand"]:
        choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()
    if choice in ["hit", "h", "H", "Hit"]:
        player_card.append(random.choice(list(Card_Deck.items())))
        print("You drew the card ", player_card[i][0])
        Card_Deck.pop(player_card[i][0])
        if player_card[i][1] == [1, 11]:
            if player_score <= 10:
                player_score = player_score + player_card[i][1][1]
            else:
                player_score = player_score + player_card[i][1][0]
        else:
            player_score = player_score + player_card[i][1]
        i += 1
        if player_score > 21:
            print("You're busted, Your score is ", player_score)
            break
        if player_score < 21:
            print("Your score is ", player_score)
            continue
    if choice in ["s", "stand", "S", "Stand"]:
        print("You decided to stand, your score is ", player_score)
        break

if player_score < 21:
    while dealer_score < 16:
        dealer_card.append(random.choice(list(Card_Deck.items())))
        print("The dealer drew the card ", dealer_card[j][0])
        Card_Deck.pop(dealer_card[j][0])
        if dealer_card[j][1] == [1, 11]:
            if dealer_score <= 10:
                dealer_score = dealer_score + dealer_card[j][1][1]
                print("The dealer score is ", dealer_score)
            else:
                dealer_score = dealer_score + dealer_card[j][1][0]
                print("The dealer score is ", dealer_score)
        else:
            dealer_score = dealer_score + dealer_card[j][1]
            print("The dealer score is ", dealer_score)
        j += 1
    if dealer_score > 21 and player_score < 22:
        print("You won !")
    elif dealer_score == player_score:
        print("It's a tie !")
    elif 22 > dealer_score > player_score:
        print("You lost...")
    elif dealer_score < 22 and dealer_score < player_score:
        print("You won !")
