num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
for i in range(0,len(num_list)):
    if isEven(num_list[i]):
        print(str(num_list[i]) + " is even.")
    else:
        print(str(num_list[i]) + " is odd.")