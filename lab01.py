
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin no.: 2004176
'''

# Task 02: Implementating a 2-way Morse Code Translator

lookUpTable = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}


def encode(file):
    with open(file) as f:
        text = f.readlines()
    morseText = ""
    for line in text:
        for char in line:
            if char.isalpha():
                morseText += lookUpTable[char.upper()] + ","
            elif char.isspace():
                morseText += " "
            else:
                morseText += " "
    return morseText


def decode(file):
    with open(file) as f:
        morse = f.readlines()

    text = ""
    for line in morse:
        words = line.split(",")
        print(words)
        for word in words:
            if word == " ":
                text += " "
            for key, value in lookUpTable.items():
                if value == word:
                    text += key
        text += "\n"
    return text

print(encode("textSOS.txt"))

# # Task 04: Implementing Alogrithm D

# def guessing(maxNum):
#     guessed = False
#     numGuess = 0
#     candidates = [i for i in range(1, maxNum + 1)]
#     # numCandidates = maxNum

#     while not guessed:
#         breakPointIndex = (len(candidates) // 2)
#         breakpoint = candidates[breakPointIndex]
#         print(f"Is the number smaller than {breakpoint}?")

#         if input(f"'y' or 'n'? ").lower() == 'y':
#             candidates = candidates[: breakPointIndex]
#         else:
#             candidates = candidates[breakPointIndex:]

#         numGuess += 1
#         if len(candidates) == 1:
#             guessed = True
#     print(f"It took {numGuess} to guess: {candidates[0]}")


# guessing(int(input("Enter the range: ")))
