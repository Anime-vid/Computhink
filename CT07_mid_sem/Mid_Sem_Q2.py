# """
# ============================================================
# Q2. Food Order System
# ============================================================
# Write a PYTHON program that simulates a restaurant order
# system using list and while loop.

# Requirements:
# - Use a while loop
# - Ask: "What would you like to order?"
# - Store each order into a list
# - Stop when user enters "end"
# - After ending, print all orders in numbered format

# ============================================================
# """

# ============================================================
# Step 1: Initialize variables
# ============================================================
lst = []
Order = ""
itmNum = 0


# ============================================================
# Step 2: Create a loop
# ============================================================
while Order != "end":
    Order = input("What would you like to order?")
    if Order != "end":
        itmNum += 1
        lst.append(str(itmNum) + ". " + str(Order))


# ============================================================
# Step 3: Print the final order summary
# ============================================================
# Print the final order in this format:
# You have ordered the following:
# 1. Item1
# 2. Item2
# 3. Item3
# ============================================================
print("You have ordered the following:")
for i in range(0,len(lst)):
    print(lst[i])