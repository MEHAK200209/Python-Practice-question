#Linear Search

# def linear_search(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#     return -1
#
# user_input = input("Enter the array elements separated by spaces: ")
# arr = list(map(int, user_input.split()))
#
# target = int(input("Enter the target element to search: "))
#
# result = linear_search(arr, target)
#
# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found in the array")


def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


while True:
    try:
        arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
        break
    except ValueError:
        print("Please enter only numbers!")

while True:
    try:
        target = int(input("Enter the target number: "))
        break
    except ValueError:
        print("Please enter a valid number!")


result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
