import writetodoc
import csv
with open(r'idscores.csv','r') as id:
        reader = csv.DictReader(id)
        for i in reader:
                if i == 0:
                        continue
                writetodoc.writedoc(i['FILE_KEY'])

