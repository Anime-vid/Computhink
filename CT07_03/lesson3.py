# while True:
#     qn = input("I'm not a blanket, yet I cover the ground; a crystal from heaven that doesn't make a sound. What am I?")
#     if qn == "snowflake" or "Snowflake":
#         print("CORRECT!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         break
# import time
# study = input("How many minutes you want to study?")
# study = study * 60
# time.sleep(study)
# print("GOOD JOB YOU ARE DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# 
# savings = 0
# while savings < 100:
#     savings = savings +int(input("How much did you save today?"))
# print("Congratulations for saving $100 or more!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# 
import random
lives = 3
qn_num = 0
qn = ""
stnum = 0
ndnum = 0
ans = 0
while True:
    stnum = random.randint(2,20)
    ndnum = random.randint(2,20)
    ans = stnum * ndnum
    ans = int(ans)
    while True:
        qn = int(input("What is " + str(stnum) + " X " + str(ndnum) ))
        if ans != qn:
            lives = lives - 1
        if lives == 0:
            print("GO AND SEE MS TAN FOR REMEDIAL")
            break
        break
        if ans == qn:
            break
    qn += 1
    if qn == 15:
        print("YA DID IT")
        break