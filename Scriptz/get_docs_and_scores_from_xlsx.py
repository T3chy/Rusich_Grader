import qq
import xlrd
import glob, os
def downloadfromsheet(loc):
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	print(sheet.cell_value(1, 1)) 
	for i in range(sheet.nrows):
		fileid = sheet.cell_value(i,5)
		qq.main(fileid)
		print('download completed for file'+i+'of'+sheet.nrows)
sss = []
os.chdir('/home/t3chy/venvs/Rusich_Grader/')
for file in glob.glob("*.xlsx"):
    sss.append(file)
