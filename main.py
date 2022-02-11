import random

letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

codeLimit = int(input("How many codes do you need? "))
codeLength = int(input("How long should each code be? (characters) "))

# Combine all arrays for our possible characters array
characters = letters_upper + letters_lower + numbers

# Create an array to store the new codes
codeList = []

# Loop 20 times
for item in range(0, codeLimit):

  setThrough = False

  # Loop until current new code is added to the list
  while(setThrough == False):

    # Reset newCode tag
    newCode = ''

    # Loop to create a 7 character-long code
    for item in range(0, codeLength):

      # Shuffle array for extra randomity
      random.shuffle(characters)
      newCode += characters[random.randint(0,len(characters) - 1)]

    # Check if the new code is our list so far
    if newCode not in codeList:
      codeList.append(newCode)
      print(str(len(codeList)) + ' - ' + newCode)
      setThrough = True

print(codeList)

possibleUniqueCodes = len(characters) ** codeLength
print(f"There are {possibleUniqueCodes} possible unique codes using {codeLength} characters long")