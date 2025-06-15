text = input("Enter a sentence: ")

words = text.split()
alnum_words = []

for word in words:
    has_alpha = any(char.isalpha() for char in word)
    has_digit = any(char.isdigit() for char in word)
    if has_alpha and has_digit:
        alnum_words.append(word)

print("Words with both alphabets and numbers:", alnum_words)