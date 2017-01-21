# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:34:06 2016

@author: samk33t
"""

#feature : clicks on item divided by average clicks in a session
#use dataframe with NoOfAppearances column
#need 2 different databases one is the original one and one is with no_of_appearances column

import pandas as pd
def feature4Sfunc():

	df=pd.read_csv("Phase1_data/testMod.csv", low_memory=False, usecols=[1,2,3,4,5,6])
	total_session=df.groupby(['Session_ID']).size().reset_index()
	total_item=df.groupby(['Session_ID','Item_ID']).size().reset_index()
	total_session=total_session.rename(columns={0:'S_Temp'})
	total_item=total_item.groupby(['Session_ID']).size().reset_index()
	total_item=total_item.rename(columns={0:'I_Temp'})
	total_item=total_item.merge(total_session,on='Session_ID')
	total_item['Avg']=total_item['S_Temp']/total_item['I_Temp']

	temp=pd.read_csv('Phase2_data/Feature1.csv',header=0,delimiter=',')
	temp=temp.merge(total_item,on='Session_ID')
	temp['ClicksPerAvg']=temp['No_of_Appearances']/temp['Avg']
	#temp=temp.drop(columns={'S_Temp','I_Temp','Unnamed: 0'},axis=1)
	temp.to_csv('Phase2_data/Feature4S.csv',sep=',')