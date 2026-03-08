# print("Hello from lesson 1")
# Red = 1
# Blue = 2
# Green = 3  
# spend = Red * 3 + Blue * 5 + Green * 4
# spend = str(spend)
# print("$" + spend)\


# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3
# student_name = "Alex"
# average_score = str(average_score)
# print("Average score for " + student_name + " is: " + average_score)


Grade = input("Grade?")
Grade = int(Grade)
if Grade > 75:
    print("You got an A")
elif Grade in range(60,74):
    print("You got a B")
elif Grade in range(50,59):
    print("You got a C")
else:
    print("YOU FAIL")