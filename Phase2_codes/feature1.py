import pandas as pd
def feature1func():	
	df=pd.read_csv("Phase1_data/testMod.csv", low_memory=False, usecols=[1,2,3,4,5,6])
	#feaure : no of appearance of each item in a session
	df=df.groupby(['Session_ID','Item_ID']).size().reset_index()
	df=df.rename(columns={0:'No_of_Appearances'})
	df.to_csv('Phase2_data/Feature1.csv',sep=',')