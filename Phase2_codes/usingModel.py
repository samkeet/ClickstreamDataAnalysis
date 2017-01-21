import graphlab as gl
import csv
def RandomForestfunc():

	data =  gl.SFrame.read_csv('Phase2_data/mergedFeaturesMod.csv')
	model = gl.load_model('Phase2_codes/Random_Forest_Model')
	predictions = model.predict(data)
	results = model.evaluate(data)
	print results
	predictions.save('Phase2_data/ItemsBought.csv',format='csv')
