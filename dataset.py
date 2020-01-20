import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class Dataset:
    PATH = ''

    train_dir = ''
    validation_dir = ''

    IMG_HEIGHT = 64
    IMG_WIDTH = 64

    batch_train = 0
    batch_test = 0



    def __init__(self,path,batch_train,batch_test):
        self.PATH = path
        self.batch_train = batch_train
        self.batch_test = batch_test



    def plotImages(self,images_arr):
        fig, axes = plt.subplots(1, 3, figsize=(10,10))
        axes = axes.flatten()
        for img, ax in zip(images_arr, axes):
            ax.imshow(img)
            ax.axis('off')
        plt.tight_layout()
        plt.show()

    def getTrainImage(self):
        train_dir = os.path.join(self.PATH, 'train')
        train_image_generator = ImageDataGenerator(rescale=1. / 255)  # Generator for our training data
        train_data_gen = train_image_generator.flow_from_directory(batch_size=self.batch_train,
                                                                   directory=train_dir,
                                                                   shuffle=True,
                                                                   target_size=(self.IMG_HEIGHT,self.IMG_WIDTH),
                                                                   class_mode='categorical')
        return train_data_gen

    def getTestImage(self):
        test_dir = os.path.join(self.PATH, 'test')
        test_image_generator = ImageDataGenerator(rescale=1. / 255)  # Generator for our training data
        test_data_gen = test_image_generator.flow_from_directory(batch_size=self.batch_test,
                                                                   directory=test_dir,
                                                                   shuffle=True,
                                                                   target_size=(self.IMG_HEIGHT,self.IMG_WIDTH),
                                                                   class_mode='categorical')
        return test_data_gen

    def showTest(self,test_data):
        sample_test_images, _ = next(test_data)
        self.plotImages(sample_test_images[:self.batch_test])




