import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
# import path
# import sys


# dir = path.Path(__file__).abspath()
# sys.path.append(dir.parent.parent)

# load model
# path_to_model = './h5/Xception_BT.h5'
# Load the trained model
model = tf.keras.models.load_model('Xception_BT.h5')

# Define classes
classes = ['No Tumor', 'Tumor']

# Function to preprocess the image
def preprocess_image(image):
    # Resize image to the required input size of the model
    image = image.resize((224, 224))
    # Convert image to numpy array
    image_array = np.array(image)
    # Normalize pixel values
    image_array = image_array / 255.0
    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Streamlit app
def main():
    st.title('Brain MRI Tumor Detection')

    # Upload image
    uploaded_image = st.file_uploader("Upload a brain MRI image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)

        # Get class label
        predicted_class = np.argmax(prediction)

        # Display prediction result
        st.write(f"Prediction: {classes[predicted_class]}")
        st.write(f"Confidence: {prediction[0][predicted_class]*100:.2f}%")

if __name__ == "__main__":
    main()
