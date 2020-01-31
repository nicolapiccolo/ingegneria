from dataset import Dataset
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
import numpy

seed = 7
numpy.random.seed(seed)

data = Dataset('monumenti',1,1)
it = data.getTrainImage()

print(len(it))

X=[]
Y=[]
i=0
while i<len(it):
    image, label = next(it)
    X.append(image)
    Y.append(label)
    #print(i, label)
    i+=1

print(len(X))
print(len(Y))

X = numpy.array(X)
Y = numpy.array(Y)

print(X.shape)
print(Y.shape)

#X = [numpy.concatenate(i) for i in X]

X = X.reshape(X.shape[1], -1)

print(X[0])

"""t = 0
for i in it:
    
    t = t+1"""


kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
kfold.split(X, Y)
cvscores = []

"""
for train, test in kfold.split(X, Y):
    # create model


    model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(10, activation='softmax')])

    # Compile model
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    # Fit the model

    model.fit(X[train], Y[train], epochs=15, batch_size=5, verbose=0)

    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
"""


