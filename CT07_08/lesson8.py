# print("Hello from lesson 8")
# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# clean = []
# count = 0
# dupe = 0
# for i in range(0,len(student_indexes)):
#     if student_indexes[i] not in clean:
#         clean.append(student_indexes[i])
#         count += 1
#     else:
#         dupe += 1
# print("Number of students attended is " + str(count))
# print("Number of students duplicated is " + str(dupe))
# Isalpha = ""
# while Isalpha != True:
#     Name = input("What is your Name?")

#     Isalpha = Name.isalpha()
# Isnum = ""
# while Isnum != True:
#     Age = input("What is your Age?")
# Isnum = Age.isnumeric()
# Isalnum = ""
# while Isalnum != True:
#     User = input("What is your username?")
#     if len(User) > 5 and len(User) < 10:
#         Isalnum = True



# while True:
#     number = input("Enter your number.")
#     if number.isnumeric and len(number) == 8:
#         print("Number is valid ")
#         break
#     else:
#         print("Number is invalid")
#         print("Try again")

# while True:
#     birthYear = input("Birth Year: ")
#     if birthYear.isnumeric and int(birthYear) > 1899 and int(birthYear) < 2027:
#         break
# while True:
#     Vol = input("Volume: ")
#     if Vol.isnumeric and int(Vol) > -1 and int(Vol) < 101:
#         break
# input_sentence = input("Please enter a sentence: ")
# mocking_sentence = ""
# for i in range(len(input_sentence)):
#     if i % 2 == 0:
#         mocking_sentence += input_sentence[i].upper()
#     else:
#         mocking_sentence += input_sentence[i].lower()
# print("Mocking sentence: " + mocking_sentence)
# SG = "Singapore"
# a = SG[0:4]
# print(a)
# b = SG[3:6]
# print(b)
# c = SG[5:9]
# print(c)
# d = SG[0:9:2]
# print(d)
# word = ""
# while True:
#     if word == "end":
#         break
#     word = input("Enter a word: ")
#     wejn = len(word)
#     if word == word[::-1]:
#         print("Yes " + word + " is a palindrome.")
#     else:
#         print("No " + word + " is not a palindrome.")
# names = ["Alice", "Bob", "Carl", "Dylan"]
# name = ""
# while name == "":
#     name = input("What is your name? ")
#     if name != "":
#         if name in names:
#             print("WELCOME")
#             break
#         else:
#             print("Get out.")
# nricc = input("What is your full NRIC? ")
# if len(nricc) != 9:
#     print("Invalid!")
# elif not nricc[0].isupper() or not nricc[-1].isdigit():
#     print("Invalid!")
# elif nricc[0] not in ("M","S", "T", "F", "G"):
#     print("Invalid!")
# elif nricc[1:8].isdigit():
#     print("Valid")
upper = False
lower = False
digit = False
noother = False
password = input("What is Your password? ")
if len(password) > 8:
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit(): 
            digit = True
        if i.isalnum():
            noother = True
        else:
            noother = False
if upper == True and lower == True and digit == True and noother == True:
    print("Password is Valid.")
else:
    print("Password is not Valid")
    

