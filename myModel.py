from dataset import Dataset
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
import numpy
from tensorflow.keras.preprocessing.image import ImageDataGenerator


seed = 7
numpy.random.seed(seed)

class MyModel:

    model = ''
    epochs = 0
    train = ''
    val = ''

    def __init__(self,train,val,epochs):
        self.train = train
        self.val = val
        self.epochs = epochs
        self.model = Sequential([
            Conv2D(16, 3, padding='same', activation='relu', input_shape=(64, 64, 3)),
            MaxPooling2D(),
            Conv2D(32, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Conv2D(64, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Flatten(),
            Dense(512, activation='relu'),
            Dense(train.num_classes, activation='softmax')
        ])

    def getModel(self):
        return self.model

    def compileModel(self):
        self.model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

    def fitModel(self):
        total_train = self.train.samples
        batch_train = self.train.batch_size

        total_val = self.val.samples
        batch_val = self.val.batch_size

        self.model.fit_generator(
            self.train,
            steps_per_epoch=total_train // batch_train,
            epochs=self.epochs,
            validation_data=self.val,
            validation_steps=total_val // batch_val
        )

    def evaluateModel(self):
        scores = self.model.evaluate_generator(self.val,self.val.batch_size, max_queue_size=10, workers=1)
        return scores



"""
dir_path = "monumenti"
generator = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.1)

train_gen = generator.flow_from_directory(dir_path,batch_size=3,shuffle=True,target_size=(64,64),class_mode='categorical',subset='training')
val_gen = generator.flow_from_directory(dir_path,batch_size=3,shuffle=True,target_size=(64,64),class_mode='categorical', subset='validation')


model = Sequential([
            Conv2D(16, 3, padding='same', activation='relu', input_shape=(64,64,3)),
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


total_train = train_gen.samples
batch_train = train_gen.batch_size

total_val = val_gen.samples
batch_val = val_gen.batch_size

model.fit_generator(
    train_gen,
    steps_per_epoch=total_train // batch_train,
    epochs=15,
    validation_data=val_gen,
    validation_steps=total_val // batch_val
)


scores = model.evaluate_generator(val_gen, 5, max_queue_size = 10,workers = 1)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
"""







