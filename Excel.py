from openpyxl import load_workbook 

file_path = r"C:\Users\stars\OneDrive\Desktop\Phone_number_scrapping\Air Con and Electrical (Yellow Page).xlsx"
workbook = load_workbook(filename = file_path)

# the first row is title
dict = {'Name': 'Homedeal Air Conditioning QLD', 'Phone': '(07) 3186 0287', 'Address': 'Coorparoo QLD 4151', 'Website': 'http://www.homedealairconditioning.com.au'}

#find the first cell that not filled with value
def find_last_row(sheetname):
    for row in workbook[sheetname].iter_rows(max_col=1):
        for cell in row:
            if cell.value is not None:
                last_cell = cell.coordinate
                col = last_cell[:1]
                row = int(last_cell[1:]) + 1
                
                
    return(col + str(row))

#fill in the information of the company according to the state
def fill_in_value(sheetname, coordinate, company_info):
    row = coordinate[1:] #get the row number

    workbook[sheetname]["A"+str(row)] = company_info["Name"]
    workbook[sheetname]["B"+str(row)] = company_info["Phone"]
    workbook[sheetname]["C"+str(row)] = company_info["Address"]
    workbook[sheetname]["D"+str(row)] = company_info["Website"]

    workbook.save(file_path)

#find out the state name
def state_name(company_info):
    state = ["QLD", "NSW", "VIC", "SA", "ACT", "WA", "NT", "TAS"]
    if company_info["Address"].split(" ")[1] in state:
        state = company_info["Address"].split(" ")[1]
    elif company_info["Address"].split(" ")[2] in state:
        state = company_info["Address"].split(" ")[2]
    else:
        return "No state"
    
    return state

#check if there is duplicate
def check_duplicate(sheetname, company_info):
    company_name = company_info["Name"]
    company_address = company_info["Address"]
    for row in range(2, workbook[sheetname].max_row+1):
        name = workbook[sheetname].cell(row=row, column =1)
        address = workbook[sheetname].cell(row=row, column =4)
        if name == company_name and address == company_address:
            return True 
        else:
            continue

        # for cell in row:
        #     column_number = cell.column
        #     address_cooridnate = "C" + str(column_number)
        #     print(workbook[sheetname][address_cooridnate].value)
        #     print(company_address)
        #     if cell.value == company_name and workbook[sheetname][address_cooridnate].value == company_address:
        #         return True 
        #     else:
        #         continue
    return False
