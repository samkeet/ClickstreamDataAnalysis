import testDataBuys01
import features1to5
import features6to8
import features9to10
import mergefeatures
import svm_model
import merged_results

def phase1(filename):
	testDataBuys01.testDataBuys01func(filename)
	features1to5.features1to5func()
	features6to8.features6to8func()
	features9to10.features9to10func()
	mergefeatures.mergefeaturesfunc()
	svm_model.svm()
	merged_results.merged_results()