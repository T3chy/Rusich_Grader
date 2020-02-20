#import qq
import csv
import xlrd
import glob, os
def sheet2json(loc):
	init = 0
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	for i in range(sheet.nrows):
		if i == 0:
			continue
		keyandscores = []
		print(i)

		keyandscores = [str(sheet.cell_value(i,4)),
		str(sheet.cell_value(i,5)),
		str(sheet.cell_value(i,6)),
		str(sheet.cell_value(i,7)),
		str(sheet.cell_value(i,8)),
		str(sheet.cell_value(i,9))]
		#finish adding all the scoring categories
		with open(r'idscores.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerow(keyandscores)
      # print('download completed for file '+str(i)+' of '+str(sheet.nrows-1))
      #  print('Download Complete!')
sss = []
os.chdir('/home/t3chy/venvs/Rusich_Grader/')
for file in glob.glob("*.xlsx"):
	sss.append(file)
print(sss)
for ss in sss:
	print(ss)
	sheet2json(ss)
