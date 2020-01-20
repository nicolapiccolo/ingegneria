import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt



PATH = 'monumenti'

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'test')

train_colosseo_dir = os.path.join(train_dir, 'colosseo')  # directory with our training cat pictures
train_pisa_dir = os.path.join(train_dir, 'pisa')  # directory with our training dog pictures
train_duomo_dir = os.path.join(train_dir, 'duomo')

validation_colosseo_dir = os.path.join(validation_dir, 'colosseo')  # directory with our validation cat pictures
validation_pisa_dir = os.path.join(validation_dir, 'pisa')  # directory with our validation dog pictures
validation_duomo_dir = os.path.join(validation_dir, 'duomo')

num_colosseo_tr = len(os.listdir(train_colosseo_dir))
num_pisa_tr = len(os.listdir(train_pisa_dir))
num_duomo_tr = len(os.listdir(train_duomo_dir))

num_colosseo_val = len(os.listdir(validation_colosseo_dir))
num_pisa_val = len(os.listdir(validation_pisa_dir))
num_duomo_val = len(os.listdir(validation_duomo_dir))

total_train = num_colosseo_tr + num_pisa_tr + num_duomo_tr
total_val = num_colosseo_val + num_pisa_val + num_duomo_val

print('total training colosseo images:', num_colosseo_tr)
print('total training pisa images:', num_pisa_tr)
print('total training duomo images:', num_duomo_tr)

print('total validation colosseo images:', num_colosseo_val)
print('total validation pisa images:', num_pisa_val)
print('total validation duomo images:', num_duomo_val)

print("--")
print("Total training images:", total_train)
print("Total validation images:", total_val)

batch_size = 3
epochs = 15
IMG_HEIGHT = 64
IMG_WIDTH = 64

classes = ['colosseo', 'torre di pisa', 'duomo']
train_image_generator = ImageDataGenerator(rescale=1. / 255)  # Generator for our training data
validation_image_generator = ImageDataGenerator(rescale=1. / 255)  # Generator for our validation data

train_data_gen = train_image_generator.flow_from_directory(batch_size=3,
                                                           directory=train_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                           class_mode='categorical')

val_data_gen = validation_image_generator.flow_from_directory(batch_size=3,
                                                              directory=validation_dir,
                                                              target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                              class_mode='categorical')

sample_training_images, _ = next(train_data_gen)
sample_test_images, _ = next(val_data_gen)


# This function will plot images in the form of a grid with 1 row and 5 columns where images are placed in each column.
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(7, 7))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


plotImages(sample_training_images[:2])

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='sigmoid')
])

"""    
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(64,64)),
    tf.keras.layers.Dense(100, activation=tf.nn.relu),
    tf.keras.layers.Dense(2)
])


model.compile(loss="sparse_categorical_crossentropy", 
              optimizer="adam",
              metrics=["accuracy"])
"""

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit_generator(
    train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=total_val // batch_size
)

plotImages(sample_test_images[:3])

STEP_SIZE_TEST = val_data_gen.n // val_data_gen.batch_size
val_data_gen.reset()
pred = model.predict_generator(val_data_gen,
                               steps=STEP_SIZE_TEST,
                               verbose=1)

predicted_class_indices = np.argmax(pred, axis=1)


labels = (train_data_gen.class_indices)
print(labels)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

# for i in range(yp.size):
print(predictions)



print('prova')