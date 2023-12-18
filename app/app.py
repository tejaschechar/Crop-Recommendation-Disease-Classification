# Importing essential libraries and modules
import os
from flask import Flask, render_template, request, Markup, redirect
import numpy as np
import pandas as pd
import requests
import tensorflow as tf
from PIL import Image
import pickle
import config
from utils.disease import disease_dic
from utils.fertilizer import fertilizer_dic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------
# Loading plant disease classification model

disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry___healthy',
                   'Cherry___Powdery_mildew',
                   'Corn___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn___Common_rust',
                   'Corn___healthy',
                   'Corn___Northern_Leaf_Blight',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___healthy',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___healthy',
                   'Potato___Late_blight',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___healthy',
                   'Strawberry___Leaf_scorch',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___healthy',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

#print(len(disease_classes))


disease_model_path = r"E:\Machine Learning-A-Z-Codes-Datasets\major project\efficientnet_model_v1_full_94%"
disease_model = tf.keras.models.load_model(disease_model_path)

crop_recomadation_model_path = r"E:\Machine Learning-A-Z-Codes-Datasets\major project\crop recomadation\model\RandomForest.pkl"
crop_recomadation_model = pickle.load(open(crop_recomadation_model_path, 'rb'))

fertilizer_prediction_path = r"E:\Machine Learning-A-Z-Codes-Datasets\major project\fertilizer prediction\model\RandomForestForFertilizer.pkl"
fertilizer_prediction_model = pickle.load(open(fertilizer_prediction_path,'rb'))



# =========================================================================================
# Custom functions for calculations


# Create a function to import an image and resize it to be able to be used with our model
def load_and_prep_image(img, img_shape=224):
    """
    Reads an image from filename, turns it into a tensor
    and reshapes it to (img_shape, img_shape, colour_channel).
    """
    # Read in target file (an image)
    #img = tf.io.read_file(filename)

    # Decode the read file into a tensor & ensure 3 colour channels 
    # (our model is trained on images with 3 colour channels and sometimes images have 4 colour channels)
    img = tf.image.decode_image(img, channels=3)

    # Resize the image (to the same size our model was trained on)
    img = tf.image.resize(img, size = [img_shape, img_shape])

    # Rescale the image (get all values between 0 and 1)
    img = img/255.
    return img



# Adjust function to work with multi-class
def pred_disease(model, img, class_names):
    """
    Imports an image located at filename, makes a prediction on it with
    a trained model and plots the image with the predicted class as the title.
    """
    # Import the target image and preprocess it
    img = load_and_prep_image(img)

    # Make a prediction
    pred = model.predict(tf.expand_dims(img, axis=0))

    # Get the predicted class
    if len(pred[0]) > 1: # check for multi-class
        pred_class = class_names[pred.argmax()] # if more than one output, take the max
    else:
        pred_class = class_names[int(tf.round(pred)[0][0])] # if only one output, round

    return pred_class



def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None
    
    # ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------

app = Flask(__name__)

# render home page
@ app.route('/')
def home():
    title = 'CultivatePros - Home'
    return render_template('index.html', title=title)


# render crop recommendation form page
@ app.route('/crop-recommend')
def crop_recommend():
    title = 'CultivatePros - Crop Recommendation'
    return render_template('crop.html', title=title)


# render fertilizer recommendation form page
@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'CultivatePros - Fertilizer Suggestion'
    return render_template('fertilizer.html', title=title)



# render disease prediction input page
@ app.route('/disease')
def disease_classification():
    title = 'CultivatePros - disease_classification'
    return render_template('disease.html', title=title)




# ===============================================================================================
# RENDER PREDICTION PAGES


# render crop recommendation result page
@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'CultivatePros - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # state = request.form.get("stt")
        city = request.form.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recomadation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)

        else:

            return render_template('try_again.html', title=title)



# render fertilizer recommendation result page
@ app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'CultivatePros - Fertilizer Suggestion'

    crop_name = str(request.form['cropname'])
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorous'])
    K = int(request.form['pottasium'])
    # ph = float(request.form['ph'])

    df = pd.read_csv(r'E:\Machine Learning-A-Z-Codes-Datasets\major project\fertilizer prediction\dataset\fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))
    return render_template('fertilizer-result.html', recommendation=response, title=title)



'''# render disease prediction result page
@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'CultivatePros - Disease Detection'

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            print("no file")
            return render_template('disease.html', title=title)
        try:
            img = file.read()
            #new_image = load_and_prep_image(filename=img, img_shape=224)
            prediction = pred_disease(model=disease_model, filename=img, class_names=disease_classes)
            prediction = Markup(str(disease_dic[prediction]))
            return render_template('disease-result.html', prediction=prediction, title=title)
        except:
            pass
    return render_template('disease.html', title=title)
'''


@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'CultivatePros - Disease Detection'

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            print("No selected file")
            return render_template('disease_2.html', title=title)

        try:
            # Read the image file
            img = file.read()
            # Perform disease prediction using your model and functions
            prediction = pred_disease(model=disease_model, img=img, class_names=disease_classes)
            predicted_disease_name = Markup(str(disease_dic[prediction]))
            
            # Render the result template with the prediction
            return render_template('disease-result.html', prediction=predicted_disease_name, title=title)
        
        except Exception as e:
            print(f"Error: {e}")
            return render_template('error.html', error_message="Error processing the image. Please try again.")

    return render_template('disease_2.html', title=title)


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)