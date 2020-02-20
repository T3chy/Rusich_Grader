import qq
import json
import xlrd
import glob, os
def downloadfromsheet(loc):
        init = 0
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0) 
        for i in range(sheet.nrows):
                if i == 0:
                        continue
		keyandscores = []
                print(i)
                fileid = sheet.cell_value(i,4)
                print(fileid)
                qq.main(fileid,str(init))
                init = init + 1
                print('download completed for file '+str(i)+' of '+str(sheet.nrows-1))
        print('Download Complete!')
sss = []
os.chdir('/home/t3chy/venvs/Rusich_Grader/')
for file in glob.glob("*.xlsx"):
    sss.append(file)
print(sss)
for ss in sss:
        print(ss)
        downloadfromsheet(ss)
