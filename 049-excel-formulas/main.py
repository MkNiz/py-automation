import openpyxl

book = openpyxl.load_workbook("data.xlsx")
sheet = book.get_active_sheet()

def first_blank(sheet, col):
    """Returns the row number of the first blank cell in a column"""
    rowNum = 1
    for row in sheet.iter_rows():
        rowNum += 1
    return rowNum

# Assign variables to cell names           
empty_row = first_blank(sheet, 1)
label_cell_1 = 'B' + str(empty_row)
sum_cell = 'C' + str(empty_row)

empty_row += 1
label_cell_2 = 'B' + str(empty_row)
avg_cell = 'C' + str(empty_row)

# Display data in cells
sheet[label_cell_1] = "Total:"
sheet[sum_cell] = "=SUM(C2:C12)"

sheet[label_cell_2] = "Average:"
sheet[avg_cell] = "=AVERAGE(C2:C12)"

# Save
book.save("data_with_formulas.xlsx")
print("Saved copy of workbook with formulas to data_with_formulas.xlsx")
