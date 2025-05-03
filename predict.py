import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os

# Load model
model = load_model('garbage_classifier.keras')

# Load class names
dataset_path = 'wasteDataset'
class_names = sorted(os.listdir(dataset_path))

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    print("Predicted:", predicted_class)

# Example
predict_image('D:\Garbage_classification\download (1).jpeg')
