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
#print("cost:",cost)

drink = input("Would you like a drink?   ")
if drink == ("yes"):
  drink_size= input("Pick a Beverage Size, large ($2.25), medium ($1.75), or small ($1.00)   ")
  if drink_size == "large":
    print("You picked large")
    cost= cost+2.25
  if drink_size == "medium":
    print("You picked medium")
    cost= cost+1.75
  if drink_size == "small":
    print("You picked small")
    cost= cost+1.00
if drink ==("no"):
  print("You choose no drink")
#print("cost:",cost)

fries = input("Would you like fries?   ")
if fries == ("yes"):
  fry_size =input("Pick a size of fry, large ($2.00), medium ($1.50), or small($1.00)   ") 
  if fry_size == "large":
    print ("You picked large")
    cost=cost+2.00
  if fry_size == "medium":
    print ("You picked medium")
    cost=cost+1.50
  if fry_size == "small":
    megasize= input("Would you like to megasize your fries?  ")
    if megasize == ("yes"):
      print("You megasized!")
      cost=cost+2.00
    if megasize == ("no"):
      print ("You picked small")
      cost=cost+1.00
if fries == ("no"):
  print("You choose no fries")
print("cost:",cost)

ketchup_packets = input("How many packets of ketchup would you like?   ")
