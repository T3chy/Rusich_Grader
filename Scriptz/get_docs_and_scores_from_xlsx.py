import xlrd
loc = '/home/t3chy/venvs/Rusich_Grader/Sample.xlsx' 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
print(sheet.cell_value(1, 1)) 

