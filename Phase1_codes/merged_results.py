import csv
import pandas as pd
import os

def merged_results():
	#SVM output merge with session id so as to view which sessions have a purchase
	data1 = pd.read_csv("Phase1_data/features1-10.csv", usecols=['Session_ID'], header=0)
	data2 = pd.read_csv("Phase1_data/outputSVM.csv", header=None, low_memory="false")

	data2.columns = ['b']
	data2.to_csv('Phase1_data/outputTest_temp.csv')

	data2 = pd.read_csv("Phase1_data/outputTest_temp.csv", usecols=['b'], low_memory="false")

	data1['Buys']=data2

	os.remove('Phase1_data/outputTest_temp.csv')
	print data1
	data1=data1[data1.Buys !=0]
	data1.to_csv("Phase1_data/PredictedBuysOnly.csv", delimiter=',')

	

	f2 = file('Phase1_data/PredictedBuysOnly.csv', 'r')
	f1 = file('Phase1_data/testMod.csv', 'r')
	f3 = file('Phase1_data/resultMod.csv', 'w')

	c1 = csv.reader(f1)
	c2 = csv.reader(f2)
	c3 = csv.writer(f3)

	masterlist = list(c2)

	for hosts_row in c1:
	    row = 1
	    found = False
	    for master_row in masterlist:
	        results_row = hosts_row
	        if hosts_row[2] == master_row[1]:
	            # results_row.append('FOUND in master list (row ' + str(row) + ')')
	            found = True
	            c3.writerow(results_row)
	            break
	        row = row + 1
	    
	    
	f1.close()
	f2.close()
	f3.close()
	data1 = pd.read_csv("Phase1_data/resultMod.csv", header=0)




	data1.to_csv("Phase1_data/testMod.csv", delimiter=',')
	


