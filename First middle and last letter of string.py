text = input("Enter a string: ")
if len(text) > 0:
    first = text[0]
    middle = text[len(text)//2]
    last = text[-1]
    result = first + middle + last
    print("Result:", result)
else:
    print("Empty string.")