# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 17:11:31 2016

@author: Sony_owner
"""

import pandas as pd
import timeit
from pandas import DataFrame
import numpy as np

def featureExfunc():
	start = timeit.default_timer()
	data1 = pd.read_csv("Phase1_data/testMod.csv", low_memory=False, usecols=[1,2,3,4,5,6])

	data2=DataFrame(data1.groupby(['Session_ID','Item_ID'])['Timestamp'].count()).reset_index()
	data3=DataFrame({'MaxClicks': data2.groupby(['Session_ID'])['Timestamp'].max()}).reset_index()

	data2=data2.merge(data3, on='Session_ID')
	data2['RelativeClicks']=data2.Timestamp/data2.MaxClicks

	data2.to_csv('Phase2_data/featureExtra.csv',sep=',')


	stop = timeit.default_timer()
	print stop - start