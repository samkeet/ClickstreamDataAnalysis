# -*- coding: utf-8 -*-
"""
Created on feb 18
adding buy not but to solution file

"""
import pandas as pd
def testDataBuys01func(filename):
	data1 = pd.read_csv(filename,sep=',')

	data1['Buy']=0
	data1.to_csv('Phase1_data/testMod.csv',delimiter=',')