#Create an list from 1-6
my_list = [1, 2, 3, 4, 5, 6]

#randomize list 
import random
random.shuffle(my_list)
message = my_list[0]
print(message)

#Create if/then statement for the magic ball

if message == 1 or message == 2:
    print("Yes")
elif message == 3:
    print("Maybe")
elif message >= 3 and message <= 6:
    print("Definetily not")
else:
    print("Try again")


