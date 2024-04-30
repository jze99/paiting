import tensorflow as tf
from tensorflow.python.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Путь к вашему датасету
dataset_path = 'путь_к_вашему_датасету/'

# Определение размеров изображений и числа классов
img_height, img_width = 64, 64
num_classes = 10

# Создание генераторов для загрузки и предобработки данных
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    os.path.join(dataset_path, 'train'),  # путь к папке с обучающими изображениями
    target_size=(img_height, img_width),
    batch_size=32,
    class_mode='sparse')

validation_generator = test_datagen.flow_from_directory(
    os.path.join(dataset_path, 'validation'),  # путь к папке с валидационными изображениями
    target_size=(img_height, img_width),
    batch_size=32,
    class_mode='sparse')

# Определение модели нейронной сети
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Проверка каталога для сохранения модели
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)

# Сохранение модели
model.save_weights(checkpoint_prefix)

# При необходимости загрузка модели из сохраненных весов
# model.load_weights(checkpoint_prefix)
