# """
# ============================================================
# Q1. Hero Quest
# ============================================================
# A hero goes on an adventure, starting at Full Health.
# He fights monsters and loses health randomly each round.

# Requirements:
# - Start with 100 health
# - Print starting message
# - Lose between 1 to 15 health each round (random)
# - Use a while-loop
# - Continue until health <= 0
# - Print total number of battles fought

# ============================================================
# """

# ============================================================
# Step 1: Import required module
# ============================================================
import random


# ============================================================
# Step 2: Initialize variables
# ============================================================
battles = 0
health = 100
lostHealth = 0
# ============================================================
# Step 3: Print starting message
# ============================================================
print("You are a hero goes on an adventure, starting at Full Health. You fight monsters and lose health randomly each round.")


# ============================================================
# Step 4: Create while-loop for battles
# ============================================================
# - Randomly reduce health between 1 and 15
# - Increase battle counter
# - Print updated health
# ============================================================
while not health <= 0:
    battles += 1
    lostHealth = random.randint(1,15)
    print("You have lost " + str(lostHealth) + " health on the " + str(battles) + " battle")
    health = health - lostHealth
    print("After fighting monsters, his Health is now: " + str(health))



# ============================================================
# Step 5: Print final result
# ============================================================
# Print in this format:
# He fought xxx battles, and died
# ============================================================
print("He fought " + str(battles) + " battles, and died")