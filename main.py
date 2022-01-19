cost=0

sandwich= input("Pick a Sandwich, beef ($6.25), chicken (5.25$) , or tofu ($5.75)   ")
if sandwich == "beef":
  print("You picked beef")
  cost = cost+6.25
if sandwich == "chicken":
  print("You picked chicken")
  cost = cost+5.25
if sandwich == "tofu":
  print("You picked tofu")
  cost = cost+5.75

drink = input("Would you like a drink?   ")
if drink == ("yes"):
  beverage= input("Pick a Beverage, large ($2.25), medium ($1.75), small ($1.00)   ")
  if beverage == "large":
    print("You picked large")
    cost= cost+2.25
  if beverage == "medium":
    print("You picked medium")
    cost= cost+1.75
  if beverage == "small":
    print("You picked small")
    cost= cost+1.00
if drink ==("no"):
  print("You choose no drink")
print (cost)

