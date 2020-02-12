from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D


from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
from sklearn.model_selection import StratifiedKFold

dir_path = "monumenti"
generator = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)


gen = generator.flow_from_directory(dir_path,batch_size=3,shuffle=True,target_size=(64,64),class_mode='categorical')
#val_gen = generator.flow_from_directory(dir_path,batch_size=3,shuffle=True,target_size=(64,64),class_mode='categorical', subset='validation')

X=[]
Y=[]
root = dir_path
i = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if not name.startswith('.'):
            X.append(os.path.join(path, name))
            Y.append(str(i))
    i+=1


X = np.array(X)
Y = np.array(Y)
#dataset = pd.DataFrame({'label': Y, 'images': list(X)}, columns=['label', 'images'])
#print(dataset)

cvscores=[]
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=7)
cvscores = []
for train, test in kfold.split(X,Y):

    X_train = np.array(X[train])
    Y_train = np.array(Y[train])

    X_test = np.array(X[test])
    Y_test = np.array(Y[test])

    #print(X1)
    train = pd.DataFrame({'label': Y_train, 'images': list(X_train)}, columns=['label', 'images'])
    test = pd.DataFrame({'label': Y_test, 'images': list(X_test)}, columns=['label', 'images'])

    #print(dataset)



    train_generator = generator.flow_from_dataframe(
        dataframe=train,
        x_col="images",
        y_col="label",
        target_size=(64, 64),
        batch_size=3,
        class_mode='categorical')

    test_generator = generator.flow_from_dataframe(
        dataframe=test,
        x_col="images",
        y_col="label",
        target_size=(64, 64),
        batch_size=1,
        class_mode='categorical')

    model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    total_train = train_generator.samples
    batch_train = train_generator.batch_size


    total_val = test_generator.samples
    batch_val = test_generator.batch_size

    model.fit_generator(
        train_generator,
        steps_per_epoch=total_train // batch_train,
        epochs=15,
        validation_data=test_generator,
        validation_steps=total_val // batch_val
    )

    scores = model.evaluate_generator(test_generator,batch_val,max_queue_size=10, workers=1)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))