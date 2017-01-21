import pandas as pd
def mergeFeaturefunc():
		
	a = pd.read_csv('Phase2_data/features1-3.csv',sep=',')
	b = pd.read_csv("Phase2_data/feature4.csv",sep=',')
	merged = a.merge(b, on=['Session_ID','Item_ID'])
	b = pd.read_csv('Phase2_data/featureExtra.csv',sep=',')
	merged=merged.merge(b, on=['Session_ID','Item_ID'])
	b = pd.read_csv('Phase2_data/Feature1.csv',sep=',')
	merged=merged.merge(b, on=['Session_ID','Item_ID'])
	b = pd.read_csv('Phase2_data/Feature3.csv',sep=',')
	merged=merged.merge(b, on=['Session_ID','Item_ID'])
	b = pd.read_csv('Phase2_data/Feature4S.csv',sep=',')
	merged=merged.merge(b, on=['Session_ID','Item_ID'])
	merged.to_csv('Phase2_data/mergedFeatures.csv', delimiter=',',columns=None)


