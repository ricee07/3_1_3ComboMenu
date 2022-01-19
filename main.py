cost=0
sandwich= input("Pick a Sandwich, beef ($6.25), chicken (5.25$) , or tofu ($5.75)")
if sandwich == "beef":
  print("You picked beef")
  cost = cost+6.25
  print("cost:",cost)
if sandwich == "chicken":
  print("You picked chicken")
  cost = cost+5.25
  print("cost:",cost)
if sandwich == "tofu":
  print("You picked tofu")
  cost = cost+5.75
  print("cost:",cost)
  