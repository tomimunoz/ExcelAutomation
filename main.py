#ONLY IS POSSIBLE TO CHANGE SHEET1
from functions.ExcelModifier import process_workbook
from functions.FileSearcher import xlsx_searcher

filename = xlsx_searcher()
print(filename)
column_modify = int(input('Column you want to edit: '))
column_data = int(input('New data column: '))
column_name = input('Column name: ')
ans = input('Do you want to make a chart? Y/N').upper()
if ans == 'Y':
    boolean = True
else:
    boolean = False

process_workbook(filename, column_modify, column_data, boolean, column_name)