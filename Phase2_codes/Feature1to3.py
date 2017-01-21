# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 20:27:45 2016

@author: Sony_owner
"""


import pandas as pd
import timeit
from pandas import DataFrame

def Features1to3func():
	start = timeit.default_timer()

	data1 = pd.read_csv("Phase1_data/testMod.csv", low_memory=False, usecols=[1,2,3,4,5,6])
	data1=data1.reset_index()

	#Feature 1: First Clicked Item in Session
	data4=data1.groupby(['Session_ID']).first()
	data1['FirstClick']=0
	data1.ix[data4['index'],'FirstClick']=1

	#Feature 2: First Clicked Item in Session
	data4=data1.groupby(['Session_ID']).last()
	data1['LastClick']=0
	data1.ix[data4['index'],'LastClick']=1

	data6=(data1.groupby(['Session_ID','Item_ID']).max()).reset_index()

	#Feature 3: Time between first and last click on that item
	data2=(data1.groupby(['Session_ID','Item_ID']).max()).reset_index()
	data3=(data1.groupby(['Session_ID','Item_ID']).min()).reset_index()
	data2['TimeFirstLastTest']=(pd.to_datetime(data2.Timestamp)-pd.to_datetime(data3.Timestamp))
	for i, row in data2.iterrows(): 
	    data2.set_value(i,'TimeFirstLast',data2.iloc[i,9].total_seconds()/60)
	    
	data6['TimeFirstLast']=data2.TimeFirstLast
	#del data6['Timestamp']
	data6 = data6.drop(['Timestamp','index','Category'], axis=1)

	data6.to_csv('Phase2_data/features1-3.csv',sep=',')

	stop = timeit.default_timer()
	print stop - start 