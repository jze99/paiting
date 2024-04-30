from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Загрузка сохраненной модели
model = load_model('model_.h5')

# Загрузка исходного изображения
image = Image.open('dataset/b2.png').convert('L')  # Преобразование в оттенки серого

# Изменение размера изображения (если это необходимо)
resized_image = image.resize((28, 28))

# Преобразование изображения в массив numpy
image_array = np.array(resized_image)

# Нормализация значений пикселей (если это необходимо)
normalized_image = image_array / 255.0

# Преобразование изображения в вектор для подачи на вход модели
input_vector = normalized_image.reshape(1, 28, 28, 1)

reshaped_input = np.reshape(input_vector, (1, 784))

# Получение предсказания от модели
prediction = model.predict(reshaped_input)

# Вывод результатов
print("Prediction:", prediction)