weight = 41.5
# Ground Shipping
if weight <= 2:
  coust_ground = weight * 1.50 + 20.00
elif weight <= 6:
  coust_ground = weight * 3.00 + 20.00
elif weight <= 10:
  coust_ground = weight * 4.00 + 20.00
else:
  coust_ground = weight * 4.75 + 20.00
print("Ground Shipping: ",coust_ground)

# Ground Shipping Premium
coust_ground_pro = 125.00
print ("Coust Premium PRO: ",coust_ground_pro)

# Drone Shipping
if weight <= 2:
  coust_ground = weight * 4.50 + 0.00
elif weight <= 6:
  coust_ground = weight * 9.00 + 0.00
elif weight <= 10:
  coust_ground = weight * 12.00 + 0.00
else:
  coust_ground = weight * 14.25 + 0.00
print("Drone Shipping coust: ",coust_ground)


