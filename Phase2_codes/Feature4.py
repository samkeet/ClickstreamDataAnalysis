# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 14:09:12 2016

@author: Sony_owner
"""

import pandas as pd
import timeit
from pandas import DataFrame
import numpy as np

def feature4func():

	start = timeit.default_timer()
	data1 = pd.read_csv("Phase1_data/testMod.csv", low_memory=False, usecols=[1,2,3,4,5,6])

	#Feature : Total time spent on an item
	data1['TimeBtwClicksTemp']=(pd.to_datetime(data1.Timestamp)-pd.to_datetime(data1.Timestamp.shift()))
	for i, row in data1.iterrows(): 
	    data1.set_value(i,'TimeBtwClicks',data1.iloc[i,6].total_seconds()/60)

	count1=data1['TimeBtwClicks'].size-2
	for i, row in data1.iterrows(): 
	     if i>count1:
	            break    
	     if data1.iloc[i,1]!=data1.iloc[i+1,1]:
	        data1.set_value(i+1,'TimeBtwClicks',0)

	count2=data1['TimeBtwClicks'].size-2
	for i, row in data1.iterrows(): 
	    if i>count2:
	            break    
	    data1.set_value(i,'TimeBtwClicks',data1.iloc[i+1,7])
	data2=DataFrame({'TotalTimeItem': data1.groupby(['Session_ID','Item_ID'])['TimeBtwClicks'].sum()}).reset_index()

	'''
	#Feature : Max time spent on a partiular item
	data3=DataFrame({'MaxTimeItem': data1.groupby(['Session_ID','Item_ID'])['TimeBtwClicks'].max()}).reset_index()
	data2['MaxTimeItem']=data3.MaxTimeItem
	'''

	data2.to_csv('Phase2_data/feature4.csv',sep=',')

	stop = timeit.default_timer()
	print stop - start 