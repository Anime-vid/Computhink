# Lesson 8 - Input Validation

## Recap 1: List Manipulation
You have a list of student index numbers who attended the Math Enrichment class. 
However, some students’ attendance were recorded more than once due to a human error.
Your task is to clean the list and produce a list of unique Student Indexes

Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
Sort the cleaned list in ascending order.
- Print the final list and also print how many duplicates were removed.
- Print the count of how many students attended the Math Enrichment Class.

student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

## Task 1: Data Format Check

### Task 1a
Ask the user to input their first name until it is a valid name. 
A valid name only contains alphabets.
Keep asking for a name until a valid name is input.

### Task 1b
Ask the user to input their age until it is a valid number. 
Keep asking for a name until a valid number is input.

### Task 1c
Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

## Task 2: Length Check (using a while loop)

### Task 2a
Ask the user to input their phone number until it is valid using a while loop.
Make sure to check if the input is the correct data type as well!

### Task 2b
Ask the user to a username and check if it is between 5 to 18 characters long.

## Task 3: Range Check (using a while loop)

### Task 3a
Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.

### Task 3b
Ask the user to input their volume setting and check if it is between 0 and 100.

## Task 4: Mocking Text Generator
Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

1. Using input(), ask the user for a sentence
2. Use loops to iterate through each letter in the sentence
3. Alternate between .upper() and .lower() for each letter
4. Print the result.

## Task 5: Slice String
word = “SINGAPORE”

Slice the string and print these words:
a. SING
b. GAP
c. PORE
d. SNAOE

## Task 6: Palindrome
Ask the user for an input and check if it is a palindrome, until the input is ‘end’.

You can try this list of words:
- civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

## Task 7: Presence and Existence Checks
You are hosting a Birthday Party and have invited your friends.

Create a list with your friends’ names
- e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

Write a program to ask for the visitor’s name and check if:
- Name is entered (presence check)
- Name is in your friend list (existence check)

Ask for an input again if a name was not entered.
Accept the visitor if they are in the list, else deny their entry.

## Task 8: Format Check
Ask the user to input their NRIC you need to check:
1. First and last character are alphabets in upper case
2. First letter must be S, T, F, G, or M.
3. Have 7 digits between the alphabets
4. Be 9 characters long

## Task 9: Password Validation
A website requires all passwords to
1. Be at least 8 characters long
2. Contain an upper and lower case
3. Contain a number
4. No other characters except alphabets or numbers.

Write a program that will ask the user for a password, and check if the password fits all criteria

You may use some of the following passwords to test your program:
- PassW0rd
- H3ll0W0r1d
- BestF00d
- pa55Me