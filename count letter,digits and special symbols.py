text = input("Enter a string: ")

letters = digits = symbols = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", symbols)