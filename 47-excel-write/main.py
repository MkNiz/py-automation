import openpyxl
import dogs

print("Creating workbook...")
book = openpyxl.Workbook()
print("Setting up sheet...\n")
sheet = book.get_active_sheet()
sheet.title = "Dogs"
print("Working on sheet:", sheet.title)

print("Populating sheet with data from 'dogs'...")
# Write header row
sheet['A1'] = "Name"
sheet['B1'] = "Breed"
sheet['C1'] = "Age"
print("Headers inserted in row 1")
# Write data rows
for ix, dog in enumerate(dogs.data):
    row_str = str(ix+2)
    name_cell = 'A' + row_str
    breed_cell = 'B' + row_str
    age_cell = 'C' + row_str
    
    sheet[name_cell] = dog['name']
    sheet[breed_cell] = dog['breed']
    sheet[age_cell] = dog['age']
    print("Data for " + dog['name'] + " inserted in row " + row_str)
print("")

# Make a new sheet for adoption status data
print("Creating a new sheet, 'Adoptions'...")
sheet2 = book.create_sheet(title="Adoptions")
print("Working on sheet:", sheet2.title)

print("Populating sheet with data from 'dogs'...")
#Write header row
sheet2['A1'] = "Name"
sheet2['B1'] = "Adopted"
print("Headers inserted in row 1")
#Write data rows
for ix, dog in enumerate(dogs.data):
    row_str = str(ix+2)
    name_cell = 'A' + row_str
    adoption_cell = 'B' + row_str
    
    sheet2[name_cell] = dog['name']
    sheet2[adoption_cell] = dog['adopted']
    print("Adoption status for " + dog['name'] + " inserted in row " + row_str)
print("")

book.save('dogs.xlsx')
    
    
    
    
    
    
