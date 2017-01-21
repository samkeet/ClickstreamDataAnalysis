import csv
import pandas as pd
import os

def mergeResultfunc():
	data1 = pd.read_csv("Phase2_data/mergedFeaturesMod.csv", usecols=['Session_ID','Item_ID'], header=0)
	data2 = pd.read_csv("Phase2_data/ItemsBought.csv", header=None, low_memory="false")

	data2.columns = ['b']
	data2.to_csv('Phase2_data/outputTest_temp.csv')

	data2 = pd.read_csv("Phase2_data/outputTest_temp.csv", usecols=['b'], low_memory="false")

	data3=data1
	data3['ItemPrediction']=data2
	data3.to_csv('Phase2_data/ItemsBoughtinSession.csv', delimiter=',')
	os.remove('Phase2_data/outputTest_temp.csv')

	print data3 
