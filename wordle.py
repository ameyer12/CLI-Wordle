from english_words import get_english_words_set
import random
from termcolor import colored

web2lowerset = get_english_words_set(['web2'], lower=True)

class Wordle:
    def __init__(self):
        self.letters = 5
        self.tries = self.letters
        self.currentRow = 0
        self.isFound = False
        self.words = {
            w for w in web2lowerset if len(w) == 5
        }
        self.word = random.choice(list(self.words))
        self.gameBoard = [
            ["*"] * self.letters for i in range(len(self.word))      
        ]
        self.keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                         ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'], 
                         ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]

    def main(self):
        while self.tries > 0 and self.isFound == False:
            self.printGameBoard()
            self.printKeyBoard()
            self.isValidWord()
            self.updateGameBoard(attempt)
            self.updateKeyboard(attempt)

            if attempt == self.word:
                self.wonGame()
                break

            self.currentRow += 1
            self.tries -= 1
        
        if self.tries == 0:
            self.lostGame()

    def printGameBoard(self):
        print(self.word)
        print("\n     --- Game Board ---      \n")
        for row in self.gameBoard:
            print("          " + " ".join(row))

    def printKeyBoard(self):
        print("\n      --- Keyboard ---       \n")
        for row in self.keyboard:
            print("      " + " ".join(row))

    # Await user input and check to make sure the entry is a 6 letter word
    # and is a valid word
    def isValidWord(self):
        while True:
            print("\n" + str(self.tries) + " tries left")
            print("\nEnter your word here: ")
            global attempt
            attempt = input().lower()

            if len(attempt) != 5:
                print("Invalid entry. Please enter a 5 letter word.")
                continue
            elif attempt not in self.words:
                print("Invalid entry. Please enter a valid word.")
                continue
            else:
                break

    def updateGameBoard(self, attempt):
        for i in range(len(attempt)):
            char = attempt[i]
            duplicateCount = 0

            # Duplicate letter detection
            if char in self.gameBoard[self.currentRow] or colored(char, "green") in self.gameBoard[self.currentRow] or colored(char, "yellow") in self.gameBoard[self.currentRow]:
                duplicateCount += 1

                if duplicateCount <= self.word.count(char) and char in self.word:
                    if char == self.word[i]:
                        self.gameBoard[self.currentRow][i] = colored(char, "green") 
                        duplicateCount += 1
                    else:
                        self.gameBoard[self.currentRow][i] = colored(char, "yellow") 
                        duplicateCount += 1
                else:
                    self.gameBoard[self.currentRow][i] = char
                    duplicateCount += 1
            
            if char in self.word:
                if attempt.index(char) == self.word.index(char):
                    self.gameBoard[self.currentRow][self.word.index(char)] = colored(char, "green")
                else:
                    self.gameBoard[self.currentRow][attempt.index(char)] = colored(char, "yellow")
            else:
                self.gameBoard[self.currentRow][attempt.index(char)] = char


    def updateKeyboard(self, attempt):
        for char in attempt:
            if char not in self.word:
                if char.upper() in self.keyboard[0]:
                    self.keyboard[0][self.keyboard[0].index(char.upper())] = "*"
                elif char.upper() in self.keyboard[1]:
                    self.keyboard[1][self.keyboard[1].index(char.upper())] = "*"
                elif char.upper() in self.keyboard[2]:
                    self.keyboard[2][self.keyboard[2].index(char.upper())] = "*"


    def wonGame(self):
        self.printGameBoard()
        self.printKeyBoard()
        print("\nYou won!" + " The word was: " + self.word + "\n")
        print("You had " + str(self.tries) + " tries to spare.\n")
    
    def lostGame(self):
        print("Sorry you lose! The word was: " + self.word)


if __name__ == '__main__':
    wordle = Wordle()
    wordle.main()