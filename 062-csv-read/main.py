import csv

weaponFile = open('weapons.csv')
weapon_r = csv.reader(weaponFile)
data_list = list(weapon_r)

# Accessing a value by row and column within the list
print("\nValue at row 3, column 4:")
print(data_list[2][3])

# Putting a list of the data into a for loop
print("List:\n")
for row in data_list:
    row_str = ""
    for val in row:
        row_str += val + "  "
    print(row_str)
    