from art import logo, vs
from game_data import data
import random


def game():
    print(logo)
    score = 0

    compare_a = random.choice(data)

    while True:
        compare_b = random.choice(data)

        while compare_b == compare_a:
            compare_b = random.choice(data)
   
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']} ")
        print(vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']} ")
        
        empty_line()
        
        compared = input("Who has more followers? Type 'A' or 'B': ").capitalize()

        if compare(compared, compare_a, compare_b):
            score += 1
            print(f"You're right. Current score: {score} ")
            empty_line()
            compare_a = compare_b
        else:
            print(f"Sorry that's wrong. Final score: {score} ")
            break


def compare(input_choice, a, b):
    """Returns True if the user's choice is correct, False otherwise"""
    if (input_choice == 'A' and a['follower_count'] >= b['follower_count']) or \
       (input_choice == 'B' and b['follower_count'] >= a['follower_count']):
        return True
    return False
  
def empty_line():
    print("")

game()