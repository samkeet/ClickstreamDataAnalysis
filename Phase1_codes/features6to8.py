# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:41:32 2016

@author: Sony_owner
21mins to run
"""
import pandas as pd
import timeit
from pandas import DataFrame
def features6to8func():

	# print "start"
	start = timeit.default_timer()
	data1 = pd.read_csv('Phase1_data/testMod.csv' , sep=',', low_memory=False, usecols=[1,2,3,4,5,6])
	# print "loaded"
	# F6: Maximum No of Clicks on any item
	#Number of clicks per item in a session
	datagrp = (data1.groupby(['Session_ID','Item_ID']).size())
	datagrpframe=datagrp.reset_index()
	#print ("No of clicks per item in a session")#datagrpgrame
	#maximum no of clicks on one item
	data2= DataFrame({'MaxClicksItems': datagrpframe.groupby(['Session_ID'],sort=False)[0L].max()}).reset_index()
	# print "done6"

	#F7: No of Distinct Items in a Session
	data5=DataFrame({'DistinctItems': datagrpframe.groupby(['Session_ID'],sort=False).size()}).reset_index()
	data2['Distinct_Items']=data5['DistinctItems']
	# print "done7"

	#F8: Session Time
	data3=DataFrame(data1.groupby(['Session_ID']).max()).reset_index()
	# print "done 8.1"  
	data4=DataFrame(data1.groupby(['Session_ID']).min()).reset_index()
	# print "done 8.2"    
	data3['Session_Time_temp']=(pd.to_datetime(data3.Timestamp)-pd.to_datetime(data4.Timestamp))
	for i, row in data3.iterrows(): 
	    data3.set_value(i,'Session_Time',data3.iloc[i,6].total_seconds()/60)
	data2['Session_Time']=data3.Session_Time

	stop = timeit.default_timer()
	# print stop - start 

	data2.to_csv("Phase1_data/features6-8.csv",sep=',')
