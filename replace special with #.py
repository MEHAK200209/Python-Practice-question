# text = input("Enter a string: ")
#
# modified = ''.join('#' if not char.isalnum() else char for char in text)
#
# print("Modified string:", modified)

#2 methid
text = input("Enter a string: ")

result = ""

for char in text:
    if char.isalnum():
        result += char
    else:
        result += "#"

print("Modified string:", result)