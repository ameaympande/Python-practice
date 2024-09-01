numbers = [5,6,3,53,1,2,87,5,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)