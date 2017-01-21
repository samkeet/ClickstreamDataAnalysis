'''
18:24 hrs
'''
import pandas as pd
import timeit
import csv
import numpy as np
import time
import itertools
from functools import wraps
from pandas import DataFrame
import dateutil.parser
# import timeit
# start = timeit.default_timer()
# #1251.36390868 seconds
# k=0
# j=0
# for k in range(0,2):
# 	#opening merged file
# 	data1 = pd.read_csv('F:/Dakshil/BE_PROJECT/BE_PROJECT/yoochoose_data/final_data_22jan/clicks_sorted_final.csv', header = 0,skiprows=range(k,j), nrows=1000000)
	#creating data frame of session_ID, clicks in session. 
	#DATA1 IS MAIN DATASET,DATA2 IS FINAL DATASET FOR FEATURES
def features1to5func():
	data1 = pd.read_csv('Phase1_data/testMod.csv',sep=',', low_memory=False, usecols=[1,2,3,4,5,6])

		#F1: No of Clicks per Session
	data2=DataFrame({'Clicks': data1.groupby(['Session_ID']).size()}).reset_index()
		#average clicks per session
	# print data2['Clicks'].mean()
		#demo method(method to append column to dataframe)
		##data3=DataFrame({'Clicks': data1.groupby(['Session_ID']).size()}).reset_index()
		##data2['demo']=data3.Clicks
		#end of demo method

	data1['Day']=0
	data1['Month']=0
	data1['Hour']=0
	data1['Day_Of_Week']=0
	for i, row in data1.iterrows(): 
		d=dateutil.parser.parse(data1.iloc[i,2],ignoretz=True)  
		data1.set_value(i,'Day',d.day)
	   	data1.set_value(i,'Month',d.month)
	   	data1.set_value(i,'Hour',d.hour)
	   	data1.set_value(i,'Day_Of_Week',d.weekday())
	   	# if(i%10000==0):
	   	#     print i

		#group by to calculate mean of values for every session   
	data3=DataFrame(data1.groupby(['Session_ID']).mean()).reset_index()   

		#F2: Month of Year
	data2['Month']=data3.Month

		#F3: Day of Maonth
	data2['Day_Of_Month']=data3.Day

		#F4: Day of Week
	data2['Day_Of_Week']=data3.Day_Of_Week+1


	data2['Time_Of_Day']=data3['Hour']
		#F5: Time of Day
	data2['Time_Of_Day']=np.where((data2['Time_Of_Day']>=0) & (data2['Time_Of_Day']<=6),1,data2['Time_Of_Day'])
	data2['Time_Of_Day']=np.where((data2['Time_Of_Day']>6) & (data2['Time_Of_Day']<=12),2,data2['Time_Of_Day'])
	data2['Time_Of_Day']=np.where((data2['Time_Of_Day']>12) & (data2['Time_Of_Day']<=18),3,data2['Time_Of_Day'])
	data2['Time_Of_Day']=np.where((data2['Time_Of_Day']>18) & (data2['Time_Of_Day']<=24),4,data2['Time_Of_Day'])

		#Target Column: Buy or Not
	data2['BuyOrNot']=data3.Buy
	data2.to_csv('Phase1_data/features1-5.csv',sep=',')
		# file_name='final_features1_33mil'
		# file_name+=str(k)
		# file_name+='.csv'
		# data2.to_csv(file_name,sep=',')
		# j=1000000
		# k=k+1

	# stop = timeit.default_timer()
	# print stop - start 