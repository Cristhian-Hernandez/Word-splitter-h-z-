quote = input("Enter a quote: ")
print("-" * 80)
print("This is your quote: '" + quote + "'\n")

# Removing unwanted separators to make separating words easier
abc = string.ascii_lowercase + string.ascii_uppercase + " "
newQuote = ""

for char in quote:
    if char in abc:
        newQuote += char

# Quote ready to be split into single words
print("-" * 80)
print("These are your words split apart: '" + newQuote + "'\n")

hz = string.ascii_lowercase[7:] + string.ascii_uppercase[7:]
word = ""
start = 0
space = newQuote.find(" ")

print("-" * 80)
print("Here are the words whose first letter is between h and z:\n")
while space != -1:
    word = newQuote[start:space]
    if word[0] in hz: # Word will print if first letter (index 0) is a letter between h and z
        print("Word: '" + word + "'\n")
    start = space + 1
    space = newQuote.find(" ", space + 1)   
    if space == -1 and newQuote[start] in hz:
        print("Word: '" + newQuote[start:] + "'\n")
        
print("-" * 80 + "\n")
# End of code
