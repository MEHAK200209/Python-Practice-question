user_input = input("Enter a list of numbers separated by space: ")
lst = user_input.split()
n = len(lst)

if n % 3 != 0:
    print("List cannot be divided into 3 equal chunks.")
else:
    chunk_size = n // 3
    chunk1 = lst[:chunk_size][::-1]
    chunk2 = lst[chunk_size:2*chunk_size][::-1]
    chunk3 = lst[2*chunk_size:][::-1]

    print("Reversed chunks:")
    print("Chunk 1:", chunk1)
    print("Chunk 2:", chunk2)
    print("Chunk 3:", chunk3)