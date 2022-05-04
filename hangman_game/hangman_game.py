from playsound import playsound
import time
import pyttsx3
import random



class Gamer:

    def __init__(self, name, n_turns, life = 8, points = 0,):
        self.name = name
        self.life = life
        self.points = points
        self.tajenka = [random.choice(open('mystery_words.csv').read().split()).strip() for _ in range(n_turns)]


def introduction():
    rules = """Before you start playing, please allow me to introduce you to the rules of the game.
Each player starts with a ten of lives and zero points.
Each player will guess a few words throughout the game. This number
is related to the number of rounds you agree on.
For every letter that is not in the guessed word, you will lose one
life, for every word guessed, that player will gain one point and one life.
The game ends when there is no one left to guess, or
the number of rounds have elapsed.
The player with the most points wins.
All words are in English.
Now agree how many rounds you will play and how many you will be and we can begin. """
    talking(rules)
    time.sleep(0)
    gamers = int(input("Enter number of players ?\n:"))
    turns = int(input("How much turns would you play ?\n:"))
    return gamers, turns



def game():
    n_gamers, n_turns = introduction()
    gamers = []
    for i in range(n_gamers):
        name = input("Type name of gamer\n:")
        gamers.append(Gamer(name, n_turns))
    print("************************")
    print("Game begins!")
    time.sleep(0.5)
    for turn in range(n_turns):
        print("************************\n")
        print(f"Turn {turn+1}: \n")
        for gamer in gamers:
            print("************************")
            print("Now plays: *" + gamer.name.upper() + "*")
            gamer = mystery_word(gamer, turn)
        gamers = [gamer for gamer in gamers if gamer.life > 0]
        if len(gamers) < 1:
            print("There is no winner.")
    return victory(gamers)


def victory(lst):
    if len(lst) == 1:
        print(f"The winner is {lst[0].name} with {lst[0].points}. Good job!.")
    elif len(lst) > 1:
        names = " and ".join([gamer.name for gamer in lst])
        print(f"This a draw between " + names + ".")


def mystery_swap(letter, guessed_word, guess):
    r_letter = guessed_word.rindex(letter)
    for i in range(0,r_letter+1):
        if letter == guessed_word[i]:
            guess = guess[0:i] + guessed_word[i] + guess[i+1:]
    return guess


def mystery_word(obj, num):
    guessed_word = obj.tajenka[num-1].lower()
    guess = len(guessed_word) * "_"
    guesses = []
    while obj.life > 0 and guess != guessed_word:
        print("Your secret word is " + guess)
        tested_letter = input("Type which you think it could be in your secret word:\n>")
        if tested_letter in guesses and tested_letter.isalpha():
            print("You already tried this letter. Type a different one.")
            continue
        else:
            if tested_letter in guessed_word:
                guess = mystery_swap(tested_letter, guessed_word, guess)
                print("************************")
                print("This letter is in your word. Nice!")
                print("************************")
            else:
                print("************************")
                obj.life -= 1
                print("That letter doesn't appear in the word, you have " + str(obj.life)+" lives.")
                print("************************")
            guesses.append(tested_letter)

    if obj.life == 0:
        print("Your secret word was " + guessed_word)
        return obj
    else:
        print("Your guessed the word. Great job!")
        obj.life += 1
        obj.points += 1
        return obj


def vocabulary():
    talking("Welcome at enhancing our vocabulary. You can try to insert any english word into,but"
          "try to avoid words with apostrophes, spaces and similar symbols, thank you.")
    sentence = True
    while sentence:
        file = open("mystery_words.csv","r+")
        inserted_word = input("Try a new word:\n")
        lst = file.read().split("\n")
        if inserted_word not in lst:
            file.write("\n"+inserted_word)
            print("Your word was saved into our vocabulary. Hurray!!!!")
            file.close()
        else:
            print("This word is already in our vocabulary.")
            sentence = input("If you want to try another word, type yes:\n:")
            if sentence.lower() != "yes":
                sentence = False
    talking("Thank you for your effort to improve our game.")
    return


def talking(txt):
    text_speech = pyttsx3.init()
    answer = txt
    text_speech.setProperty("rate",110)
    text_speech.say(answer)
    text_speech.runAndWait()


def main():
    talking("""Hello players, welcome to the Hangman's Game!
    You can choose to try insert new world into our vocabulary, play the hangman or end this game.""")
    print("\n")
    while True:
        try:
            decision = int(input("For game type 1, for new world type 2, for quit type 3.\n:"))
            if decision == 1:
                victory(game())
            elif decision == 2:
                vocabulary()
            elif decision == 3:
                talking("""It was nice to have you here. Bye.""")
                break
        except ValueError:
            print("You probably used wrong number or symbol, try again.")


if __name__ == "__main__":
    game()