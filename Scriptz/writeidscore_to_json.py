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

		keyandscores = {"key":str(sheet.cell_value(i,4)),
		"purpose/organziation":str(sheet.cell_value(i,5)),
		"evidence and elaboration":str(sheet.cell_value(i,6)),
		"conventions":str(sheet.cell_value(i,7)),
		"growth":str(sheet.cell_value(i,8)),
		"interpreteation":str(sheet.cell_value(i,9))}
		#finish adding all the scoring categories
		with open('idscores.json') as jj:
			jjson = json.load(jj)
			temp = jjson['essays']
			temp.append(keyandscores)
		write_json(data)
		print(json.dumps('idscores.json'))
		print(fileid)
		qq.main(fileid,str(init))
		init = init + 1
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
