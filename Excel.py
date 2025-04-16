from openpyxl import load_workbook 

file_path = r"C:\Users\stars\OneDrive\Desktop\Phone_number_scrapping\Air Con and Electrical (Yellow Page).xlsx"
workbook = load_workbook(filename = file_path)

# the first row is title

print(workbook.sheetnames)

#find the last cell of the worksheet
def find_last_row(sheetname):
    for row in workbook[sheetname].iter_rows(max_col=1):
        for cell in row:
            if cell.value is not None:
                last_cell = cell.coordinate
                col = last_cell[:1]
                row = int(last_cell[1:]) + 1
                return(col + str(row))
        
print(find_last_row("QLD"))