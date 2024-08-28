#Concession stand program

menu={"pizza":3.00,
      "nachos": 4.50,
      "popcorn":6.00,
      "rice": 12.00,
      "chips": 1.00,
      "soda": 4.00,}

carts=[]
total=0

print("------Menu------")
for key,value in menu.items():
    print(f"{key:10}${value:02}")
print("----------------")
while True:
    food=input("Enter food (q to quit): ").lower()

    #print(food_price)
    #print (food)
    if food=="q":
        break
    elif food is not None:
        food_price = menu.get(food)
        carts.append(food)
        total += food_price
    else:
        print(f"Food Item not available \n")

print(f"Tolal price is ${total}")
for cart in carts:
    print(cart,end=" ")
