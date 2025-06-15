s1 = input("Enter the base string: ")
s2 = input("Enter the string to insert: ")

mid = len(s1) // 2
result = s1[:mid] + s2 + s1[mid:]
print("Result:", result)