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
input_sentence = input("Please enter a sentence: ")
mocking_sentence = ""
for i in range(len(input_sentence)):
    if i % 2 == 0:
        mocking_sentence += input_sentence[i].upper()
    else:
        mocking_sentence += input_sentence[i].lower()
print("Mocking sentence: " + mocking_sentence)

                                                                    






























