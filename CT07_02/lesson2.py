# # print("Hello from lesson 2")
# 
# num = -1
# for i in range(0,21,1):
#     num = num + 1
#     print(num)
# 
# for i in range(1,31):  
#     print(i)
# 
# for i in range(2,25,2):
#     print(i)
# 
# num = 1
# while True:
#     print(num)
#     num = num + 1
#     if num == 11:
#         break
# 
# counter = 1
# while counter <11:
#     print(counter)
#     counter +=1
#     if counter == 6:
#         break
# 
# inputer = ""
# toppings = ""
# while True:
#     inputer = input("TOPPING????????????????????????")
#     if inputer == "end":
#         break
#     toppings += inputer + ","
#     print(toppings)
# 
user_input = ""
max_attempt = 3
score = 0
qn_ans = [
        "what is 1+1","2",
        "what is 1+2","3",
        "what is 1+4","5"  ]
for i in range(0,len(qn_ans),2):
    question = qn_ans[i]
    ans = qn_ans[i+1]
    attempt = 0

    while attempt < max_attempt:
        user_input = input(question)
        if user_input.lower() == ans.lower():
            print("corrrect")
            score += 1
            break
        elif user_input.lower() == "skip":
            print("skipped")
            break
        else:
            


# while True:
#     qn1 = input("Which famous play features a character named Romeo? 1.Romeo and Juliet 2.67 ANS:")
