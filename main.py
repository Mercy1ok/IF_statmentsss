"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = float(35.00)
num_chars = float(input( "How many characters? " ))

color = input("Color of characters: ")
color_charge = float(0.00)

wood_type = input("Color of wood: ")
wood_type_charge = float(0.00)


if color == "gold" :
  color_charge = float(15.00)
elif color == "black" or color == "white":
  color_charge = float(0.00)

if wood_type == "oak":
  wood_type_charge = float(20.00)
elif wood_type == "pine":
  wood_type_charge = float(0.00)

if num_chars > 5:
  num_chars = float(num_chars - 5) * float(4.00)

Total_amount = (charge + num_chars + float(color_charge) + float(wood_type_charge))
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(Total_amount))