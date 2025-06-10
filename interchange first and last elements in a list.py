#interchange first and last elements in a list
#
# def swapList(newList):
#     size = len(newList)
#
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
#
#     return newList
#
#
# newList = [12, 35, 9, 56, 24]
#
# print(swapList(newList))
#
# Method 2
user_input = input("Enter numbers separated by spaces: ")

user_list = list(map(int, user_input.split()))

def swapList(lst):
    if len(lst) < 2:
        return ("Please enter atleast 2 elements")
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print("List after swapping:", swapList(user_list))
