weight = 25
ground_shipping_premium = 125

#Ground shipping

if weight <= 2 :
  cost_shipping = weight * 1.5 + 20

elif weight > 2 and weight <= 6 :
  cost_shipping = weight * 3.0 + 20

elif weight > 6 and weight <= 10 :
  cost_shipping = weight * 4.0 + 20

elif weight > 10 :
  cost_shipping = weight * 4.75 + 20

else:
  "Check with the manager"

print( "$" , cost_shipping)

# Drone shipping

if weight <= 2 :
  cost_drone_shipping = weight * 4.50

elif weight > 2 and weight <= 6 :
  cost_drone_shipping = weight * 9.00

elif weight > 6 and weight <= 10 :
  cost_drone_shipping = weight * 12.00

elif weight > 10 :
  cost_drone_shipping = weight * 14.25

else:
  "Check with the manager"

print("$", cost_drone_shipping)

if cost_shipping < ground_shipping_premium and cost_shipping < cost_drone_shipping :
  print ("Customer will take the Ground shipping ", "$",cost_shipping)

elif ground_shipping_premium < cost_shipping and ground_shipping_premium < cost_drone_shipping :
  print ("Customer will take Ground shipping premium ","$", ground_shipping_premium)
  
  
elif cost_drone_shipping < cost_shipping and cost_drone_shipping < ground_shipping_premium :
  print ("Customer will take Drone shipping","$", cost_drone_shipping)
  
  
  



