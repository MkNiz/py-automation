import openpyxl

book = openpyxl.load_workbook("data.xlsx")

# Get sheet names
all_sheets = book.get_sheet_names()
print("Sheets:")
for ix, sheet in enumerate(all_sheets):
    print("\t" + str(ix+1) + ".) " + sheet)
print("")

# Get active sheet
active = book.get_active_sheet()
print("Active Sheet:", active.title)

print("Holds data on {0}, {1}, and {2}.".format(active['A1'].value, active['B1'].value, active['C1'].value))

# Display the column contents
def print_column(col):
    """Prints the openpyxl object column pertaining to the passed column"""
    for ix, cell in enumerate(active[col]):
        if ix != 0:
            print("\t" + str(cell.value))
    print("")

print("All data in {0}:".format(active['A1'].value))
print_column('A')

print("All data in {0}:".format(active['B1'].value))
print_column('B')

print("All data in {0}:".format(active['C1'].value))
print_column('C')

# Display all row data
for row in active.iter_rows(row_offset=1):
    if row[0].value == None:
        break
    
    print(row[0].value)
    print("Breed: " + row[1].value)
    print("Age  : " + str(row[2].value))
    print("")
