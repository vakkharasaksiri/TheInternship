import random, sys
from typing import List

#importing file
with open("word1.txt", 'r') as f:
    Data1 = f.read().split(',')

with open("word2.txt", 'r') as f:
    Data2 = f.read().split(',')

with open("word1.txt", 'r') as f:
    Data3 = f.read().split(',')

wordDic =	{
  "StartUp_Name": Data1[:5],
  "StartUp_Hint": Data1[5:],
  "SoftSkill": Data2[:5],
  "SoftSkill_Hint": Data2[5:],
  "HardSkill": Data3[:5],
  "HardSkill_Hint": Data3[5:],
}

GUESS_WORD = []
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
cat = ''



# Functions

def print_word_to_guess(letters: List) -> None:
    """Utility function to print the current word to guess"""
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    """Prints how many chances the player has used"""
    print("You are on guess {0}/{1}.".format(current, total))



def start() -> None:
    """Starts the game"""
    print("Welcome To Hangman Game\n")
    print("Catagory:")
    print("1.StartUp Name\n")
    print("2.SoftSkill\n")
    print("3.HardSkill\n")
    while True:
        choice = input("Please Select the Catagory\n").strip()
        if choice == '1' or choice == '2' or choice == '3':
            if choice == '1':
                cat = "StartUp_Name"
                SECRET_WORD = random.choice(wordDic[cat])
                HINT = wordDic["StartUp_Hint"][wordDic[cat].index(SECRET_WORD)]

            elif choice == '2':
                cat = "SoftSkill"
                SECRET_WORD = random.choice(wordDic[cat])
                HINT = wordDic["SoftSkill_Hint"][wordDic[cat].index(SECRET_WORD)]
            else:
                cat = "HardSkill"
                SECRET_WORD = random.choice(wordDic[cat])
                HINT = wordDic["HardSkill_Hint"][wordDic[cat].index(SECRET_WORD)]
            output = [SECRET_WORD,HINT]
            break
        else:
            print("Please input 1 or 2 or 3")
    print("You choose " + cat)
    return output


def prepare_secret_word() -> None:
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("The word has", LENGTH_WORD, "characters")
    print("You can enter only 1 letter from a-z\n")
    print_word_to_guess(GUESS_WORD)


def guessing() -> None:
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess in ALPHABET: 
            print("Enter a letter from a-z ALPHABET")
        elif guess in letter_storage: 
            print("You have already guessed that letter!")
        else: 
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("You won!")
                    #print("Game Over!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                print("Hint: " + output[1])
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was {0}".format(SECRET_WORD))


if __name__ == "__main__":
    output = start()
    SECRET_WORD = output[0]
    
    LENGTH_WORD = len(SECRET_WORD)
    prepare_secret_word()
    print("Hint: " + output[1])
    guessing()