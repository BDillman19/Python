import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwordList = []

# Random letter random case
def getRandomLetter(nrLetters):
    for char in range(1, nrLetters + 1):
        passwordList.append(random.choice(letters))

# Random symbol
def getRandomSymbol(nrSymbols):
    for char in range(1, nrSymbols + 1):
        passwordList.append(random.choice(symbols))

# Random Number between 0-9
def getRandomNumber(nrNumbers):
    for char in range(1, nrNumbers + 1):
        passwordList.append(random.choice(numbers))

if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    nrLetters = int(input("How many letters would you like in your password?\n"))
    nrSymbols = int(input("How many Symbols would you like?\n"))
    nrNumbers = int(input("How many numbers would you like?\n"))

    getRandomLetter(nrLetters)
    getRandomSymbol(nrSymbols)
    getRandomNumber(nrNumbers)

    random.shuffle(passwordList)

    password = ""
    for char in passwordList:
        password += char

    print("Your password is:", password)