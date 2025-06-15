text = input("Enter a string: ")

lower = ''.join([c for c in text if c.islower()])
upper = ''.join([c for c in text if c.isupper()])

result = lower + upper
print("Reordered string:", result)