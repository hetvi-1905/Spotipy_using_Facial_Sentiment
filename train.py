from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.optimizers import Adam
# from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # ✅ Correct
from tensorflow.keras.layers import Lambda
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.models import Model
from tensorflow.keras import Input

train_dir = 'data/train'
val_dir = 'data/test'
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (48,48),
    batch_size = 64,
    color_mode = "grayscale",
    class_mode = 'categorical'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size = (48,48),
    batch_size = 64,
    color_mode = "grayscale",
    class_mode = 'categorical'
)

emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape = (48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))

emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001, decay=1e-6),metrics=['accuracy'])

emotion_model_info = emotion_model.fit_generator(
    train_generator,
    steps_per_epoch = 28709 // 64,
    epochs=75,
    validation_data = val_generator,
    validation_steps = 7178 // 64
)

emotion_model.save_weights('model.h5') # -----------------> 60% accuracy ! by 75 epochs

# ------------------------------------------------------------------------------------------------------------------

# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D, Lambda
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import EfficientNetB0
# from tensorflow.keras import Input

# # ✅ 1. Data Preprocessing
# train_dir = 'data/train'
# val_dir = 'data/test'

# train_datagen = ImageDataGenerator(rescale=1./255)
# val_datagen = ImageDataGenerator(rescale=1./255)

# train_generator = train_datagen.flow_from_directory(
#     train_dir,
#     target_size=(48, 48),  
#     batch_size=64,
#     color_mode="grayscale",  
#     class_mode='categorical'
# )

# val_generator = val_datagen.flow_from_directory(
#     val_dir,
#     target_size=(48, 48),
#     batch_size=64,
#     color_mode="grayscale",
#     class_mode='categorical'
# )

# # ✅ 2. Convert Grayscale to RGB
# def grayscale_to_rgb(x):
#     return tf.image.grayscale_to_rgb(x)

# inputs = Input(shape=(48, 48, 1))  
# x = Lambda(grayscale_to_rgb, name="grayscale_to_rgb")(inputs)  # Convert to RGB
# x = tf.keras.layers.Resizing(224, 224)(x)  # Resize to 224x224

# # ✅ 3. Load EfficientNetB0 Pretrained Model
# base_model = EfficientNetB0(weights="imagenet", include_top=False, input_tensor=x)  
# base_model.trainable = False  # Freeze pretrained weights

# # ✅ 4. Add Custom Layers
# x = GlobalAveragePooling2D()(base_model.output)  # Corrected
# x = Dense(256, activation='relu')(x)  
# x = Dropout(0.3)(x)  
# outputs = Dense(7, activation='softmax')(x)  

# model = Model(inputs, outputs)

# # ✅ 5. Compile Model
# model.compile(optimizer=tf.keras.optimizers.Adam(0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# # ✅ 6. Train Model
# history = model.fit(
#     train_generator,
#     validation_data=val_generator,
#     epochs=10,  # Less epochs for quick training
#     verbose=1
# )

# # ✅ 7. Save Model
# model.save('emotion_detection_efficientnetb0.h5')
# print("Model saved as emotion_detection_efficientnetb0.h5")




