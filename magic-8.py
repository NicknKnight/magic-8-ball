#Create if/then statement for the magic ball

my_list = [1, 2, 3, 4, 5, 6]
if my_list == 1:
    print("Yes")
elif my_list == 2 or 3:
    print("Maybe")
elif my_list > 3 and my_list < 6:
    print("Definetily not")
else:
    print("Try again")
