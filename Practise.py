# 1
# n = input("Enter the number of terms : ")
#
# if n.isdigit() and int(n) > 0:
#     n = int(n)
#     a, b = 0, 1
#
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
# else:
#     print("Invalid input. Please enter a positive whole number.")
# class Myclass: 

#   def __init__(self, hostname): 

#     self.hostname = hostname 

   

#2   @staticmethod

#   def Marks(marks):
#     return marks
# if __name__ == '__main__':
#   obj1= Myclass("152.45.85.463")
#   print(Myclass.Marks(5))
#   print(obj1.hostname)
 

#3 ENCAPSULATION
# class Car:
#   def __init__(self, brand, color):
#     self.__color = color
#     self.__brand = brand
#   def drive(self):
#     return self.__brand
#   def brand_name(self, brand):
#       self.__brand = brand 

   

#4   def get_color(self):
#     return self.__color
# if __name__ == '__main__':
#   obj1 = Car("Toyoto", "Red")
#   print(obj1.get_color())
#   print(obj1.drive())
#   obj1.brand_name("Hyundai")
#   print(obj1.drive()) 


#5 IMHERITANCE
# class Animal:
#   def species(self, year):
#     print("Animal has many species")
#     self.year= year
#     print(f" they live for {self.year} years")

# class Dog(Animal):
#   def species(self, year):
#     print("Dogs has many species" )
#     self.year= year
#     print(f"They live for {self.year} years")

# Dog1 = Dog()
# animal = Animal()
# Dog1.species(15)
# animal.species(80) 


#6 from abc import ABC, abstractmethod

# class Shape:
#   @abstractmethod
#   def Shape(self):
#     pass

# class Circle(Shape):
#   def __init__(self, radius):
#     self.radius = radius
#   def area(self):
#     return 3.14 * self.radius* self.radius

# circle = Circle(5)

# print(circle.area()) 


#7 string = "Hello Mehak!"
# reversed_string = string[::-1]
# print(reversed_string)

#8 string = "Hello Mehak!"
# reversed_string =''.join(reversed(string))
# print(reversed_string)

#8 def is_palindrome(text):

#   text = text.replace(" ", "").replace(",", "").lower() 

#   print(text)  

 

#   return text == text[::-1]
# text2 = "civic, madam, radar, deified"
# print(is_palindrome(text2)) # Expected output: True 


#9 def count_vowel(text):
#   vowels = 'aeiouAEIOU'
#   count = 0
#   text_vowel = ""
#   for char in text:
#    if char in vowels:
#     text_vowel+=char
#   return text_vowel

#10 string = "my name is mehak"
# print(count_vowel(string))
# def count_vowel(text):
#   vowels = 'aeiouAEIOU'
#   for char in text:
#    if char in vowels:
#     new_text= "".join([char for char in text if char not in vowels])
#   return new_text

#11 string = "my name is mehak"
# print(count_vowel(string))
# def remove_duplicate(text):
#   return ''.join(sorted(set(text), key = text.index))

#12 string = "mahimma"
# print(remove_duplicate(string))

# def remove_duplicate(text):
#   return ''.join(sorted(set(text), key = text.index))
# string = "mahimma"
# print(len(string))
# print(remove_duplicate(string))
# print(string.upper()) 


#13 def count_occurence(text, char):
#   return text.count(char)
# string = "Mahimma"
# string = string.lower()
# print(count_occurence(string, 'm'))

# def find_occurence(text, char):
#   return text.find(char)
# string = "Mahimma"
# string = string.lower()
# print(find_occurence(string, 'm'))

# to find all indices 

# def find_all_occ(text, char): 

#   return [i for i, c in enumerate(text) if c== char] 

 

# string = "mahimma" 

# print(find_all_occ(string, 'm')) 


#14 def find_all_occ(text, char):

#   indices = [] 

#   for i in range(len(text)): 

#     if text[i] ==char: 

#       indices.append(i) 

#   return indices 

 

# string = "mahimma" 

# print(find_all_occ(string, 'm')) 


#15 def contains_substring(text, substring):

#   return substring in text 

# def concatenate(text1, text2): 

#   return text1 +" " + text2 

# string2= "I am Mehak"  

# string= "hello world" 

# substring = "lo" 

# print(contains_substring(string, "hello")) 

# print(string.find(substring)) 

# print(string.split()) 

# print(concatenate(string, string2)) 


#16 def contains_substring(text, substring, new_substring):

#   return text.replace(substring,new_substring)
# string2= "I am Mehak, I am 22 years old. I work in an IT company. I am a Btech graduate"
# print(contains_substring(string2, "I","Mehak")) 


#17 def start_with( text, prefix):
#   return text.startswith(prefix)
# def end_with( text, suffix):
#   return text.startswith(suffix) 


#18 string = "juli is a girl"
# print(start_with(string, "juli"))
# print(end_with(string, "boy")) 


#19 def fibonacci(n):

#   sequence = []
#   a, b = 0, 1
#   for _ in range(n):
#     sequence.append(a) #for list
#     print(a, end = " ")  #for non-list
#     a, b = b, a + b
#   return sequence 


# # Example: Get the 10th Fibonacci number
# print(fibonacci(10)) # Output: 55
 



#20 def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))  

  

#21 def check_prime(n):

#   if n<= 1:
#     return False
#   for i in range(2, int(n**0.5)+1):
#     if n%i == 0:
#       return False
#   return True
# print(check_prime(10))   


#22 def factorial(n):
#   if n <= 0:
#     return 1
#   return n * factorial(n-1)
# print(factorial(5)) 


#23 def sum_of_NN(n):

#   return (n*(n+1))//2
# print(sum_of_NN(5)) 


#24 string = "mehak"
# print(string[::-1])
# list = [1,2,5,1,7,9]
# print (max(list)) 


#25 def find_max(list):
#   sorted_list = (sorted(list))
#   return sorted_list[-1]
# list = [1,5,4,2,9,4]
# print(find_max(list)) 


#26 def count_words(text):
#   words= text.split()
#   return words , len(words)
# print(count_words("mehak is my name")) 


#27 def common_element(list1, list2):
#   merge_list = (set(list1) & set(list2))
#   return sorted(merge_list)
# print(common_element([1,7,5,4,8,1], [4,1,4,5,2,8])) 


#29 def sum_of_even(list):

#   sum = 0 

#   for i in list: 

#     if i%2 ==0: 

#       sum+=i 

#   return sum 


# print(sum_of_even([1,2,10,4,9]))    


#30 def sum_of_even(list):

#   return sum(x for x in list if x%2 ==0) 


# print(sum_of_even([1,2,10,4,9]))     


#31 def fibonacci(n):

#   a,b = 0,1 

#   for _ in range(n): 

#     print(a, end= " ") 

#     a, b = b , a+b 

 

# print(fibonacci(5)) 


#32 def remove_duplicate(list):
#   list2 = []
#   for i in list:
#     if i not in list2:
#       list2.append(i)
#   return (list2)
# print(remove_duplicate([1,44,1,5,1,5])) 


# easy method
# def remove_duplicate(list):
#   return set(list)
# print(remove_duplicate([1,44,1,5,1,5]))  


#33 def string_length(text):
#   count = 0
#   for char in text:
#     count+=1
#   return count
# print(string_length("MEHAK"))

#34 def merge_dict(dict1, dict2):
#   dict1.update(dict2)
#   return dict1
# print(merge_dict({"name": "mehak", "class:": 12}, {"roll_no": 25501}))
# def multiplication_table(n):
#   for i in range(1,6):
#     print (f"{n} x {i} = {n*i}") 

# print(multiplication_table(5))

#35 def list_intersection(list1,list2):
#   return [value for value in list1 if value in list2]
# print(list_intersection([1,2,3], [3,4,5])) 


#36 def if_anagrams(text1, text2):
#   return sorted(text1) == sorted(text2)
# print(if_anagrams('listen', 'silent')) 

# def second_largest(lst):
#   lst = list(set(lst))
#   lst.sort()
#   return lst[-2]
# print(second_largest([1,8,1,5,9,7])) 


#37 def common_divisors(a,b):

#   divisors = []
#   for i in range(1, min(a,b)+1):
#     if a%i ==0 and b% i == 0:
#       divisors.append(i)
#   return (divisors)
# print(common_divisors(6,12))     


#38 def swap_without_temp(a,b):

#   a,b = b,a 

#   return a,b 

# print(swap_without_temp(2,3)) 


# def even_o_odd(n):

#   if n% 2 ==0:

#     print("Even")

#   else:

#     print("Odd")

# if __name__ =='__main__':

#   even_o_odd(7)

#39 Tic Tac Toe
# # def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
#     print("\n")
#
# def check_win(board, player):
#     # Check rows, columns and diagonals
#     win_conditions = (
#         [row for row in board] +
#         [[board[r][c] for r in range(3)] for c in range(3)] +
#         [[board[i][i] for i in range(3)]] +
#         [[board[i][2 - i] for i in range(3)]]
#     )
#     return [player] * 3 in win_conditions
#
# def check_draw(board):
#     return all(cell != " " for row in board for cell in row)
#
# def get_move(player):
#     while True:
#         try:
#             move = int(input(f"Player {player}, enter position (1-9): ")) - 1
#             if 0 <= move <= 8:
#                 return divmod(move, 3)
#             else:
#                 print("Invalid number. Enter between 1 and 9.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#
#     print("Welcome to Tic Tac Toe!")
#     print_board(board)
#
#     while True:
#         row, col = get_move(current_player)
#
#         if board[row][col] == " ":
#             board[row][col] = current_player
#             print_board(board)
#
#             if check_win(board, current_player):
#                 print(f"Player {current_player} wins!")
#                 break
#             elif check_draw(board):
#                 print("It's a draw!")
#                 break
#
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("That cell is already taken. Try again.")
#
# if __name__ == "__main__":
#     play_game()
#

#40 #count = 0
# number = 180
# while number > 10:
#     # divide number by 3
#     number = number / 3
#     # increase count
#     count = count + 1
# print('Total iteration required', count)
# #
#41 name = 'Jesaa29Roy'
# size = len(name)
# i = 0
# # iterate loop till the last character
# while i < size:
#     # break loop if current character is number
#     if name[i].isdecimal():
#         break;
#     # print current character
#     print(name[i], end=' ')
#     i = i + 1
#
#42 class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#
#     def display_balance(self):
#         print(f"{self.owner}'s balance: {self.balance}")
#
#43 # Test
# acc = BankAccount("Alice", 1000)
# acc.deposit(200)
# acc.withdraw(150)
# acc.display_balance()
#
# def longest_unique_substring(s):
#     char_index = {}
#     start = max_len = 0
#     for i, c in enumerate(s):
#         if c in char_index and char_index[c] >= start:
#             start = char_index[c] + 1
#         char_index[c] = i
#         max_len = max(max_len, i - start + 1)
#     return max_len
#
#44 # Test
# print(longest_unique_substring("abcabcbb"))
#
# def longest_unique_substring(s):
#     char_index = {}
#     start = max_len = 0
#     for i, c in enumerate(s):
#         if c in char_index and char_index[c] >= start:
#             start = char_index[c] + 1
#         char_index[c] = i
#         max_len = max(max_len, i - start + 1)
#     return max_len
# 
# # Test
# print(longest_unique_substring("abcabcbb"))