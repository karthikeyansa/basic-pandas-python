import pandas as pd
import csv
col_list = ["Time","data1","data2"]
df = pd.read_csv('convertcsv.csv',usecols=col_list,sep=';')
c = list(df['data1'])
d = list(df['data2'])
leng = len(c)
count = 31
l = []
r = []
j = 0
for i in range(0,leng,31):
	try:
		l.append(sum(c[j:count])//31)
		r.append(sum(d[j:count])//31)
		j = count
		count += 31
	except:
		print('out of range')
		break
#to see data
#print('data 1')
#print()
#print(*l,sep='\n')
#print('data 2')
#print()
#print(*r,sep='\n')
#writing files
try:
	with open('avg_data1.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(['Sl', 'avg_data1'])
	    for i in range(len(l)):
	    	writer.writerow([i,l[i]])
	with open('avg_data2.csv','w',newline= '') as file:
		writer = csv.writer(file)
		writer.writerow(['Sl','avg_data2'])
		for i in range(len(r)):
			writer.writerow([i,r[i]])
	print('done')
except:
	print('files cannot be created')