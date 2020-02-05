from dataset import Dataset
from myModel import MyModel

path = "monumenti"
dataset = Dataset(path,3,3)

myModel = MyModel(train=dataset.getTrainImage(),val=dataset.getTestImage(),epochs=15)
myModel.compileModel()
myModel.fitModel()
scores = myModel.evaluateModel()

print("%s: %.2f%%" % (myModel.getModel().metrics_names[1], scores[1] * 100))

myModel.getModel().save('mymodel.h5')