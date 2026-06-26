# Word Guessing Game

# word = "biriyani"
# guessed = ["_"] * len(word)
# chances = 5
# used_letters = []

# print("Welcome to the Word Guessing Game!")
# print("You have", chances, "chances to guess the word.")

# while chances > 0 and "_" in guessed:
#     print("\nWord: ", " ".join(guessed))
#     print("Used letters:", " ".join(used_letters))

#     letter = input("Guess a letter: ").lower()

#     # Check if the letter was already guessed
#     if letter in used_letters:
#         print("You already guessed that letter!")
#         continue

#     used_letters.append(letter)

#     # Check if the guessed letter is in the word
#     if letter in word:
#         print("Correct!")
#         for i in range(len(word)):
#             if word[i] == letter:
#                 guessed[i] = letter
#     else:
#         chances -= 1
#         print("Wrong guess!")
#         print("Chances left:", chances)

# # Check if the player won or lost
# if "_" not in guessed:
#     print("\n🎉 Congratulations! You guessed the word:", word)
# else:
#     print("\n😢 Game Over!")
#     print("The correct word was:", word)


# random module 

#print random num in 1-15

import random
num=random.randint(1,15)
print(num)