# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("HAPPY NEW YEAR")
# planets = [
#     "Mercury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune"
# ]
# planets[3] = "REDBALLLLLLLLLL"
# planets.append("Pluto")
# planets.insert(2,"Lalaland")
# planets.pop(4)
# print(planets)
# for i in range(len(planets)):
#     if planets[i] == "Earth":
#         print(str(planets[i]) + " is my home.")
#     elif planets[i] == "REDBALLLLLLLLLL":
#         print(str(planets[i]) + " i conqured this.")
#     elif planets[i] == "Lalaland":
#         print(str(planets[i]) + " i created this.")
#     else:
#         print(planets[i])
# visiting = [       
#     ]
# while True:
#     countriesvisiting = input("what countries to visit? ")
#     if countriesvisiting == "end":
#         break
#     visiting.append("I would like to visit " + countriesvisiting)
# print(visiting)
menu = [       
    ]
while True:
    manager = input("what food items on the menu? ")
    if manager == "end":
        break
    menu.append(manager)
print(menu)
while True:
    customer = input("What would you like to eat?")
    if customer in menu:
        print("Yes we sell that please have a seat.")
    else:
        print("Sorry, please go next door, BYE.  *kicks you oUt the window*")