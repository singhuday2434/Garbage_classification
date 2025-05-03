# from flask import Flask, request, jsonify
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image
# import io

# app = Flask(__name__)
# model = load_model('garbage_classifier.keras')  # Update: use .keras model

# class_names = ['Bandages_gauze', 'Batteries', 'Biodegradable Waste', 'Chargers & Cables',
#                'Circuit boards', 'Headphones', 'Keyboards & Mice', 'Laptops_Tablets',
#                'Medicine containers_blisters', 'Mobile Phones', 'Printers_Scanners',
#                'Recyclable Waste', 'Remote controls', 'Surgical masks & PPE',
#                'Syringes_Needles', 'Television_Monitors', 'Used cotton swabs', 'Used gloves']

# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['file']

#     # ✅ Convert file to PIL.Image using BytesIO
#     img = Image.open(io.BytesIO(file.read()))
#     img = img.resize((128, 128))  # same size as training
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0) / 255.0  # normalize

#     predictions = model.predict(img_array)
#     predicted_class = class_names[np.argmax(predictions[0])]
#     confidence = float(round(100 * np.max(predictions[0]), 2))


#     return jsonify({
#     'class': predicted_class,
#     'confidence': confidence
# })


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)
model = load_model("garbage_classification.keras")  # Your trained model
class_names = ['Bandages_gauze', 'Batteries', 'Biodegradable Waste', 'Chargers & Cables',
              'Circuit boards', 'Headphones', 'Keyboards & Mice', 'Laptops_Tablets',
               'Medicine containers_blisters', 'Mobile Phones', 'Printers_Scanners',
               'Recyclable Waste', 'Remote controls', 'Surgical masks & PPE',
               'Syringes_Needles', 'Television_Monitors', 'Used cotton swabs', 'Used gloves'] # Update based on your model

@app.route("/")
def index():
    return "Garbage Classification Flask API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['file']
    img = Image.open(file.stream).resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]

    return jsonify({'prediction': predicted_class})
