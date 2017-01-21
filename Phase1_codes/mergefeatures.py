import pandas as pd
def mergefeaturesfunc():
	a = pd.read_csv('Phase1_data/features1-5.csv',sep=',', low_memory=False, usecols=[1,2,3,4,5,6,7])
	b = pd.read_csv('Phase1_data/features6-8.csv',sep=',', low_memory=False,usecols=[1,2,3,4])
	merged = a.merge(b, on='Session_ID')
	b = pd.read_csv('Phase1_data/features9-10.csv',sep=',', low_memory=False,usecols=[1,2,3])
	merged = merged.merge(b, on='Session_ID')
	merged[['BuyOrNot']] = merged[['BuyOrNot']].astype(int)
	merged.to_csv('Phase1_data/features1-10.csv', delimiter=',')



