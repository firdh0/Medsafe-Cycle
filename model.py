from google.cloud import storage
from keras.models import load_model
import keras.utils as image
import numpy as np
import os

PROJECT_NAME = 'medsafe-cycle'
CREDENTIALS = 'medsafe-cycle-api-ml.json'
BUCKET_NAME = 'medsafe-cycle-ml'
MODEL_PATH = 'capstone.h5'

MODEL_FILE_PATH = "capstone.h5"
cached_model = None
cached_model_timestamp = None

# Load the model from Google Cloud Storage (GCS) and cache it
def load_cached_model():
    global cached_model, cached_model_timestamp
     
    if cached_model is not None and os.path.exists(MODEL_FILE_PATH):
        local_timestamp = os.path.getmtime(MODEL_FILE_PATH)
        
        if local_timestamp >= cached_model_timestamp:
               # Cached model is up to date
            return
     
    if cached_model is None:
        if os.path.exists(MODEL_FILE_PATH) is not True:
            client = storage.Client.from_service_account_json(CREDENTIALS)
            bucket = client.bucket(BUCKET_NAME)
            blob = bucket.get_blob(MODEL_PATH)
               
            blob.download_to_filename(MODEL_FILE_PATH)
               
        cached_model = load_model(MODEL_FILE_PATH)
        cached_model_timestamp = os.path.getmtime( MODEL_FILE_PATH)

def predictions(image_path):
    load_cached_model()
    target_size = (256, 256)
     
    img = image.load_img(image_path, target_size=target_size)
     
    # Preprocessing image
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = img_array / 255.0  # Normalize pixel values to the range [0, 1]

    # Process the preprocessed image using the loaded model
    predictions = cached_model.predict(preprocessed_img)
     
    # Prediction Results
    class_names = ['Sitoktoksik', 'Infeksius', 'Patologis', 'Farmasi']

    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(predictions[0])

    # Get the corresponding class name and its probability
    predicted_class = class_names[predicted_class_index]
    probability = predictions[0][predicted_class_index]

    data = {
        'category': predicted_class,
        'probability': probability
    }
        
    return data

# result = predictions('pharmaceutical.jpg')
# print(result)