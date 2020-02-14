import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd


class Dataset:
    PATH = ''

    IMG_HEIGHT = 64
    IMG_WIDTH = 64

    generator = ''
    train_gen = ''
    val_gen = ''
    batch_train = 0
    batch_val = 0

    @classmethod
    def getLabel(cls, index):
        df = pd.read_csv("monumenti/label.csv")
        return df["Monumenti"][index]

    def __init__(self, path, batch_train, batch_val):
        self.PATH = path
        self.batch_train = batch_train
        self.batch_val = batch_val

        self.generator = ImageDataGenerator(
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            validation_split=0.1)

        self.train_gen = self.generator.flow_from_directory(path, batch_size=batch_train, shuffle=True,
                                                            target_size=(64, 64),
                                                            class_mode='categorical', subset='training')

        self.val_gen = self.generator.flow_from_directory(path, batch_size=batch_val, shuffle=True,
                                                          target_size=(64, 64),
                                                          class_mode='categorical', subset='validation')

    def plotImages(self, images_arr):
        fig, axes = plt.subplots(1, 3, figsize=(10, 10))
        axes = axes.flatten()
        for img, ax in zip(images_arr, axes):
            ax.imshow(img)
            ax.axis('off')
        plt.tight_layout()
        plt.show()

    def getTrainImage(self):
        return self.train_gen

    def getTestImage(self):
        return self.val_gen

    def showTest(self):
        sample_test_images, _ = next(self.getTestImage())
        self.plotImages(sample_test_images[:self.batch_val])
