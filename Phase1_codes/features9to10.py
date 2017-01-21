import pandas as pd
from pandas import DataFrame
import numpy as np
import timeit

def features9to10func():
	start = timeit.default_timer()
	# print start
	data1 = pd.read_csv('Phase1_data/testMod.csv' , sep=',', low_memory=False, usecols=[1,2,3,4,5,6])
	# print "done"
	#data1 = data1.sort(['Session_ID', 'Timestamp'], ascending=[True, True])#console execution

	#F9 & F10: Maximum time between clicks & Avergae time between clicks
	data1['TimeBtwClicksTemp']=(pd.to_datetime(data1.Timestamp)-pd.to_datetime(data1.Timestamp.shift()))

	# print "done 0"
	for i, row in data1.iterrows(): 
	    data1.set_value(i,'TimeBtwClicks',data1.iloc[i,6].total_seconds()/60)
	    
	# print "done1"
	count1=data1['TimeBtwClicks'].size-2
	for i, row in data1.iterrows(): 
	     if i>count1:
	            break    
	     if data1.iloc[i,1]!=data1.iloc[i+1,1]:
	        data1.set_value(i+1,'TimeBtwClicks',np.nan)
	# print "done2"
	count2=data1['TimeBtwClicks'].size-2
	for i, row in data1.iterrows(): 
	    if i>count2:
	            break    
	    data1.set_value(i,'TimeBtwClicks',data1.iloc[i+1,7])
	# print "done3"
	data2=DataFrame({'MaxTimeBtwClicks': data1.groupby(['Session_ID'],sort=False)['TimeBtwClicks'].max()}).reset_index()
	# print "done4"
	data3=DataFrame({'AvgTimeBtwClicks': data1.groupby(['Session_ID'],sort=False)['TimeBtwClicks'].mean()}).reset_index()
	data2['AvgTimeBtwClicks']=data3['AvgTimeBtwClicks']
	# End of F9 & F10
	# print "done5"
	stop = timeit.default_timer()
	# print stop - start 

	data2.to_csv("Phase1_data/features9-10.csv",sep=',')