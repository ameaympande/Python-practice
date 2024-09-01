weight = float(input("Weight :"))
unit = input("(L)bs or (K)g :")

if unit.lower() == "k":
    weight *= 2.20462
elif unit.lower() == "l":
    weight /= 2.20462

if unit.lower() == "k":
    print("Weight is {:.2f} in Kilos.".format(weight))
elif unit.lower() == "l":
    print("Weight is {:.2f} in Pound.".format(weight))