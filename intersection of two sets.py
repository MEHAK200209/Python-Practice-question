input1 = input("Enter elements of the first set (space-separated): ")
input2 = input("Enter elements of the second set (space-separated): ")

set1 = set(input1.split())
set2 = set(input2.split())

common = set1 & set2

set1 = set1 - common

print("Common elements:", common)
print("First set after removing common elements:", set1)