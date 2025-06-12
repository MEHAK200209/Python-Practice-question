def most_frequent_char(text):
    text = text.replace(" ", "").lower() 
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    max_freq = 0
    result_char = ''

    for char in text:
        if freq[char] > max_freq:
            max_freq = freq[char]
            result_char = char

    return result_char

user_input = input("Enter a string: ")
result = most_frequent_char(user_input)
print(f"The most frequent character is: '{result}'")