# Shopping cart program

foods= []
prices =[]

while True:
    food= input("Enter food (press q to quit): ")

    if food.lower()== "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of a${food}: "))
        prices.append(price)

print("----YOUR CART----")
for i in foods:
    print (i, end=" ")
total=0
for price in prices:
    total += price
print(f"Total price is ${total}")