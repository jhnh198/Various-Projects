# hangman game
# if you want to post it in a portfolio, you should put the guess function in and have it -1 tries separately

word = "yellow"
wordList = []
wordList[:0] = word
clue = "A bright color"

puzzle = []
for i in wordList:
    puzzle.append("_")

tries = 7
guessedLetters = []

# 1) check if puzzle is solved.
# if puzzle has no _ in it then it is solved
def isSolved(p):
    solved = False
    for i in p:
        if i != "_":
            solved = True
        else:
            solved = False
            break
    return solved


# handle incorrect guess and show what letters have been tried already
# 4) check if input is anywhere in the word
def guess(input):
    safe = False
    for idx, i in enumerate(wordList):
        if input == i:
            puzzle[idx] = i
            safe = True
    return safe

# present puzzle, clue, tries and guessed words to the user
# get input. input can not match any guessed letters
# repeat guess, check, until solved or user runs out of guesses
while tries > 0 and not isSolved(puzzle):
    print(puzzle)
    print(clue)
    print(guessedLetters)

    playerGuess = ""
    while len(playerGuess) == 0 or playerGuess in guessedLetters:
        playerGuess = input("Please guess a letter: ")

    playerGuess = playerGuess[0].lower()
    guessedLetters.append(playerGuess)

    safe = False
    for idx, i in enumerate(wordList):
        if playerGuess == i:
            puzzle[idx] = i
            safe = True

    if not (safe):
        tries -= 1


if isSolved(puzzle):
    print("you won")
else:
    print("you lost")
