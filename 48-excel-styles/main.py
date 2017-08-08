import openpyxl
from openpyxl.styles import Font, NamedStyle

book = openpyxl.load_workbook("data.xlsx")
sheet = book.get_active_sheet()
sheet.row_dimensions[1].height = 24

bold18 = Font(size=18, bold=True)
headerStyle = NamedStyle(name="Header", font=bold18)

for cell in ['A1', 'B1', 'C1']:
    sheet[cell].style = headerStyle
    
book.save("data-styled.xlsx")
print("Spreadsheet styled and saved as data-styled.xlsx")