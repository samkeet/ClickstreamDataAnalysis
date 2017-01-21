# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:26:13 2016

@author: samk33t
"""
import pandas as pd
def feature3func():
		
	df=pd.read_csv('Phase2_data/Feature1.csv',header=0,delimiter=',')
	#feature : relative clicks
	temp=df.groupby(['Session_ID']).max().reset_index()
	del temp['Unnamed: 0']
	del temp['Item_ID']
	temp=temp.rename(columns={'No_of_Appearances':'Max_Click_Session'})
	df=df.merge(temp,on='Session_ID')
	df['Relative_Clicks']=df['No_of_Appearances']/df['Max_Click_Session']
	df.to_csv('Phase2_data/Feature3.csv',sep=',')