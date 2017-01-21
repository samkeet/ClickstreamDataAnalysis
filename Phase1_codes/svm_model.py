import graphlab as gl
import csv
def svm():
	data =  gl.SFrame.read_csv('Phase1_data/features1-10.csv')
	model = gl.load_model('Phase1_codes/SVM_Model')
	predictions = model.predict(data)
	results = model.evaluate(data)
	predictions.save('Phase1_data/outputSVM.csv',format='csv')
