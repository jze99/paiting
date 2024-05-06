import tensorflow as tf
from PIL import Image
import numpy as np

# Загрузка сохраненной модели
model = tf.keras.models.load_model("model_1.h5")

# Загрузка изображения для классификации
def II():
    image_path = "temp.png"  # Путь к вашему изображению
    image = Image.open(image_path).convert('L')  # Предполагая, что изображение ч/б и нужно конвертировать его в grayscale
    image = image.resize((28, 28))  # Изменение размера изображения до размеров, на которых обучалась модель
    image_array = np.array(image) / 255.0  # Нормализация изображения

    input_image = image_array.reshape(1, 28, 28,)

    # Predict the class of the image
    predictions = model.predict(input_image)

    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(predictions)

    # Output the predicted class
    return predicted_class_index +1
