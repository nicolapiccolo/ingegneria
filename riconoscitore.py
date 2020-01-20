from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt
from dataset import Dataset

class Riconoscitore:
    model= ""
    dataset = ""


    def __init__(self,dataset,epochs):
        self.dataset = dataset
        train = dataset.getTrainImage()
        test = dataset.getTestImage()
        self.model = Sequential([
            Conv2D(16, 3, padding='same', activation='relu', input_shape=(dataset.IMG_HEIGHT,dataset.IMG_WIDTH, 3)),
            MaxPooling2D(),
            Conv2D(32, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Conv2D(64, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Flatten(),
            Dense(512, activation='relu'),
            Dense(train.num_classes, activation='softmax')
        ])
        self.compileModel()
        self.fitModel(train,test,epochs)
        self.predictImg(test)


    def compileModel(self):
        self.model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    def fitModel(self,train,test,epochs):
        total_train = train.samples
        total_test = train.samples
        batch_train = train.batch_size
        batch_test = test.batch_size
        self.model.fit_generator(
            train,
            steps_per_epoch=total_train // batch_train,
            epochs=epochs,
            validation_data=test,
            validation_steps=total_test // batch_test
        )

    def predictImg(self,test_data):

        STEP_SIZE_TEST = test_data.n // test_data.batch_size
        test_data.reset()
        pred = self.model.predict_generator(test_data,
                                       steps=STEP_SIZE_TEST,
                                       verbose=1)

        predicted_class_indices = np.argmax(pred, axis=1)

        labels = (test_data.class_indices)
        print(labels)
        labels = dict((v, k) for k, v in labels.items())
        predictions = [labels[k] for k in predicted_class_indices]

        # for i in range(yp.size):
        self.dataset.showTest(test_data)
        print(predictions)






