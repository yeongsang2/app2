from fastapi import FastAPI, File, HTTPException
import cv2
from keras.applications.vgg16 import preprocess_input
import keras.utils as image
from tensorflow import keras
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO
import io

app = FastAPI()
@app.get("/")
def read_root():
    return {"ping"}

@app.post("/clothes-type")
async def detect_clothes_return_json_result(file: bytes = File(...)):
    
    full_model = keras.models.load_model('/user/app/model')

    img =Image.open(io.BytesIO(file)).convert("RGB")
    img = img.resize((224, 224)) 

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    c=full_model.predict(x)
    classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Romper', 'Shorts', 'Skirts', 'Sweater', 'Sweatpants', 'Tank', 'Tee', 'Top']

    Predicted_Class=np.argmax(c, axis = 1)
    return { 'type' : classes[int(Predicted_Class)]}