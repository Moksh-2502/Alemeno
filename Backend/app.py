# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate

model = load_model("C:\\Users\\AR\\Alemeno\\Alemeno\\Backend\\cnn_model.h5")  # Load your trained model

# Preprocess uploaded image
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('L')  # Convert to grayscale if needed
    img = img.resize((256, 256))  # Resize to match model input
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=(0, -1))  # Shape: (1, 64, 64, 1)
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img_bytes = file.read()
    processed_img = preprocess_image(img_bytes)

    prediction = model.predict(processed_img)
    predicted_class = int(np.argmax(prediction))

    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
