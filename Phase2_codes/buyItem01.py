# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 18:09:58 2016

@author: SONY
"""

import pandas as pd
import csv
def buyItem01func():

	# w = csv.writer(open(, "w"))
	data1 = pd.read_csv('Phase2_data/mergedFeatures.csv')
	# w.writerow(data1.columns.values)
	data1["Buys"]=0
	data2 = pd.read_csv("Phase1_data/PredictedBuysOnly.csv")
	data3=data2[data2.Buys!=0]
	for j in range(data3.shape[0]):
		for i in range(data1.shape[0]):
			if (data1.iloc[i]["Session_ID"]==data3.iloc[j]["Session_ID"]):
				print data1.iloc[i]["Session_ID"]
				data1['Buys']=1

	data4=data1[data1.Buys==1]
	data4.to_csv('Phase2_data/mergedFeaturesMod.csv',sep=',')


