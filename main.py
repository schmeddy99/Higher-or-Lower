from art import logo, vs
from game_data import data
import random

# ✅ High score should persist across all rounds
high_score = 0


def game():
    global high_score  # Keep track of high score across multiple games
    print(logo)
    
    score = 0
    compare_a = random.choice(data)

    while True:
        # ✅ Ensure compare_b is always different
        compare_b = random.choice(data)
        while compare_b == compare_a:
            compare_b = random.choice(data)

        # ✅ Display current choices
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']} ")
        print(vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']} ")

        empty_line()

        # ✅ Input validation
        compared = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        while compared not in ['A', 'B']:
            print("Invalid input! Please type 'A' or 'B'.")
            compared = input("Who has more followers? Type 'A' or 'B': ").capitalize()

        # ✅ If correct, continue the game
        if compare(compared, compare_a, compare_b):
            score += 1
            print(f"You're right! Current score: {score}")
            empty_line()
            compare_a = compare_b  # ✅ Carry forward correct choice
        else:
            # ✅ If wrong, display final score and high score
            print(f"Sorry, that's wrong. Final score: {score}")
            if score > high_score:
                high_score = score
                print(f"🎉 New High Score: {high_score} 🎉")
            else:
                print(f"🏆 High Score: {high_score}")

            # ✅ Ask if player wants to play again (ONLY when they lose)
            play_again = input("Do you want to play again? (Y/N): ").strip().upper()
            if play_again != 'Y':
                print("Thanks for playing!")
                break  # ✅ Exit game loop if they choose not to replay

            # ✅ Restart the game with a new set
            score = 0
            compare_a = random.choice(data)  # Start fresh with a new `compare_a`



def compare(input_choice, a, b):
    """Returns True if the user's choice is correct, False otherwise"""
    if (input_choice == 'A' and a['follower_count'] >= b['follower_count']) or \
       (input_choice == 'B' and b['follower_count'] >= a['follower_count']):
        return True
    else:
        correct_choice = "A" if a['follower_count'] >= b['follower_count'] else "B"
        print(f"Wrong! The correct answer was {correct_choice}.")
        return False


def empty_line():
    print("\n" + "-" * 50 + "\n")  # Adds a separator for better readability


# ✅ Run the game
game()
