
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D


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







