import pandas as pd
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from PIL import Image

# Set up the title
st.title("WELCOME TO GENRE GUESSTIMATOR")

# Load your pre-trained model
model = load_model('genre_detection_model.h5')

# Set up file uploader for the movie poster
file = st.file_uploader("Upload movie poster (only in jpg format)", type='jpg')

if file is not None:
    # Open the uploaded image
    file_img = Image.open(file)
    
    # Display the uploaded image
    st.image(file_img, caption='Uploaded Image.', use_column_width=True)

    # Define the dimensions for resizing the image
    width = 350
    height = 350

    # Preprocess the image for prediction
    img = file_img.resize((width, height))  # Resize the image
    img = image.img_to_array(img)  # Convert image to array
    img = img / 255.0  # Normalize the image
    img = img.reshape(1, width, height, 3)  # Reshape to match model's input shape

    # Define your genre classes
    classes = ['Genre_Adventure', 'Genre_Animation', 'Genre_Biography', 'Genre_Comedy',
               'Genre_Crime', 'Genre_Documentary', 'Genre_Drama', 'Genre_Family',
               'Genre_Fantasy', 'Genre_History', 'Genre_Horror', 'Genre_Music',
               'Genre_Musical', 'Genre_Mystery', 'Genre_N/A', 'Genre_News',
               'Genre_Reality-TV', 'Genre_Romance', 'Genre_Sci-Fi', 'Genre_Short',
               'Genre_Sport', 'Genre_Thriller', 'Genre_War', 'Genre_Western']

    # Make a prediction
    y_pred = model.predict(img)

    # Get top 3 predicted genres
    top3 = np.argsort(y_pred[0])[:-4:-1]

    # Display the top 3 predicted genres on the Streamlit app
    st.write("Predicted Genres:")
    for i in range(3):
        st.write(f"{i+1}. {classes[top3[i]]} with confidence {y_pred[0][top3[i]]:.2f}")
