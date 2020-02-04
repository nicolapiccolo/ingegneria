from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image

import os
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
from dataset import Dataset

class Riconoscitore:
    model= ""
    dataset = ""


    def __init__(self,dataset,epochs):
        self.dataset = dataset
        train = dataset.getTrainImage()
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
        self.fitModel(train,epochs)



    def compileModel(self):
        self.model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])


    def fitModel(self,train,epochs):
        total_train = train.samples
        batch_train = train.batch_size
        self.model.fit_generator(
            train,
            steps_per_epoch=total_train // batch_train,
            epochs=epochs,
        )


    def predictImage(self,path):
        img = self.loadImg(path)
        imgplot = plt.imshow(img)
        plt.show()
        predict = self.model.predict(img)
        print(predict)



    def loadImg(self,filename):
        np_image = Image.open(filename)
        new_image = np_image.resize((self.dataset.IMG_WIDTH, self.dataset.IMG_HEIGHT))
        np_image = np.array(new_image).astype('float32') / 255
        np_image = np_image.reshape((64,64,3))
        return np_image

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
        return predictions

    def saveModel(self,name):
        self.model.save(name)







