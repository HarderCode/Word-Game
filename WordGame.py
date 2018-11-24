import sys
ar_1 = sys.argv[0]
ar_2 = sys.argv[1]
ar_3 = sys.argv[2]
if ar_3 == "" or ar_2 == "" or ar_1 =="":
    print("Please run with 3 arguments")
num_check = ar_1.isnumeric()
num_check2 = ar_2.isnumeric()
num_check3 = ar_3.isnumeric()
if num_check == True:
    print("Argument" ,ar_1, "is not a word.  All arguments should be word")
if num_check2 == True:
    print("Argument" ,ar_2, "is not a word.  All arguments should be word")
if num_check3 == True:
    print("Argument" ,ar_3, "is not a word.  All arguments should be word")

arg_list = []
arg_list = ar_1.split(",")
arg_list.append(ar_2)
arg_list.append(ar_3)
normal_list = []
normal_list.append(ar_1)
normal_list.append(ar_2)
normal_list.append(ar_3)
count_char = len(ar_1)
count_char2 = len(ar_2)
count_char3 = len(ar_3)
if count_char == count_char2 or count_char == count_char3 or count_char2 ==count_char3 :
    print("Arguments should be a different length")
for x in arg_list[0]:
    arg_list.append(x)
for y in arg_list[1]:
    arg_list.append(y)
for z in arg_list[2]:
    arg_list.append(z)
arg_list.remove(arg_list[0])
arg_list.remove(arg_list[1])
arg_list.remove(arg_list[2])
arg_list.remove(arg_list[0])
arg_list.append(arg_list[3])
arg_list.sort()
print("Find the longest word using letters given below")
print(arg_list)
longest_word = str(input("Guess a longest word:"))

if longest_word == normal_list[0]:
    print("You found a word from list")
    print("You won 10 points")
elif longest_word == normal_list[1]:
    print("You found a word from list")
    print("You won 10 points")
elif longest_word == normal_list[2]:
    print("You found a word from list")
    print("You won 10 points")
else:
    print("The word you guessed is not in the list")