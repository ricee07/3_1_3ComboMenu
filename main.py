cost=0
discount=0
order=[]
packet_number=""
sandwich_flag=0
drink_flag=0
drink_size_flag=0
fry_flag=0
fry_size_flag=0
fry_megasize_flag=0



while sandwich_flag == 0 :
  sandwich= input("Pick a Sandwich, beef ($6.25), chicken ($5.25) , tofu ($5.75), or none   ")
  if sandwich == "beef" or sandwich == "chicken" or sandwich == "tofu" or sandwich == "none":
    if sandwich == "beef":
      sandwich_flag=sandwich_flag+1
      print("You picked beef")
      cost = cost+6.25
      discount = discount+1
      order.append("Beef Sandwhich")
    if sandwich == "chicken":
      sandwich_flag= sandwich_flag+1
      print("You picked chicken")
      cost = cost+5.25
      discount = discount+1
      order.append("Chicken Sandwhich")
    if sandwich == "tofu":
      sandwich_flag= sandwich_flag+1
      print("You picked tofu")
      cost = cost+5.75
      discount = discount+1
      order.append("Tofu Sandwhich")
    if sandwich == "none":
      sandwich_flag= sandwich_flag+1
      print("You chose no sandwich")
      order.append("No Sandwich")
  else:
    print("Please enter correct information")
    sandwich_flag=0

while drink_flag ==0:
  drink = input("Would you like a drink?   ")
  if drink == "yes" or drink== "no":
    if drink == ("yes"):
      drink_flag = drink_flag+1
      discount = discount+1
      while drink_size_flag ==0:
        drink_size= input("Pick a Beverage Size, large ($2.25), medium ($1.75), or small ($1.00)   ")
        if drink_size == "large" or drink_size == "medium" or drink_size == "small":
          if drink_size == "large":
            drink_size_flag = drink_size_flag+1
            print("You picked large")
            cost= cost+2.25
            order.append("Large Drink")
            
          if drink_size == "medium":
            drink_size_flag = drink_size_flag+1
            print("You picked medium")
            cost= cost+1.75
            order.append("Medium Drink")
            
          if drink_size == "small":
            drink_size_flag = drink_size_flag+1
            print("You picked small")
            cost= cost+1.00
            order.append("Small Drink")
        else:
          print("Please enter correct information")
      
        
    if drink ==("no"):
      drink_flag=drink_flag+1
      print("You choose no drink")
      drink_size=("no")
      order.append("No Drink")
  else:
    print("Please enter correct information")
    drink_flag =0


while fry_flag==0:
  fries = input("Would you like fries?   ")
  if fries == "yes" or fries == "no":
    if fries == ("yes"):
      fry_flag = fry_flag+1
      discount = discount+1
      while fry_size_flag ==0:
        fry_size =input("Pick a size of fry, large ($2.00), medium ($1.50), or small($1.00)   ") 
        if fry_size == "large" or fry_size == "medium" or fry_size == "small":
          if fry_size == "large":
            fry_size_flag = fry_size_flag+1
            print ("You picked large")
            cost=cost+2.00
            order.append("Large Fry")
            
          if fry_size == "medium":
            fry_size_flag = fry_size_flag+1
            print ("You picked medium")
            cost=cost+1.50
            order.append("Medium Fry")
          
          if fry_size == "small":
            while fry_megasize_flag == 0:
              megasize= input("Would you like to megasize your fries?  ")
              if megasize == "yes" or megasize == "no":
                if megasize == ("yes"):
                  fry_size_flag = fry_size_flag+1
                  fry_megasize_flag = fry_megasize_flag+1
                  print("You megasized!")
                  cost=cost+2.00
                  order.append("Large Fry")
                if megasize == ("no"):
                  fry_size_flag = fry_size_flag+1
                  fry_megasize_flag = fry_megasize_flag+1
                  print ("You picked small")
                  cost=cost+1.00
                  order.append("Small Fry")
              else:
                print("Please enter correct information")
                fry_megasize_flag = 0
        else:
          print("Please enter correct information")
          fry_size_flag=0
        
    if fries == ("no"):
      fry_flag=fry_flag+1
      print("You choose no fries")
      fry_size=("no")
      order.append("No Fry")
  else:
    print("Please enter correct information")
    fry_flag=0


ketchup_packets = int(input("How many packets of ketchup would you like?   "))
cost=cost+((ketchup_packets)*(.25))
packet_number=(ketchup_packets)
order.append(packet_number)

if discount ==(3):
  print("Final Order:" ,order)
  print("you get a dollar discount!")
  cost=cost-1.00
  print("Total Cost:",cost)
else:
  print("Final Order:" ,order)
  print("you do not qualify for a discount")
  print("Total Cost: ",cost)