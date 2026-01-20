
# Importing libraries
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping
from glob import glob



# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a third convolutional layer
#classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
#classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

# Sauvegarde les poids à chaque epoch : si ça plante, on peut récupérer les poids
checkpoint = ModelCheckpoint(
    filepath="weights_epoch_{epoch:02d}.h5",
    save_weights_only=True,
    save_best_only=False,
    verbose=1
)

# Arrête l'entraînement si la validation loss n'a pas diminué depuis 3 epochs
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)
weights = sorted(glob("weights_epoch_*.h5"))
if weights:
    classifier.load_weights(weights[-1])
    print(f"Reprise depuis {weights[-1]}")

classifier.fit_generator(
    training_set,
    steps_per_epoch=training_set.samples // training_set.batch_size,
    epochs=20,
    validation_data=test_set,
    validation_steps=test_set.samples // test_set.batch_size,
    callbacks=[checkpoint, early_stop] # Activation de la sauvegarde et de l'arrêt précoce
)

# Part 3 - Making new predictions

import numpy as np
from tensorflow.keras.utils import load_img, img_to_array

test_image = load_img(
    'dataset/single_prediction/cat_or_dog_1.jpg',
    target_size=(64, 64)
)
test_image = img_to_array(test_image)

test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'