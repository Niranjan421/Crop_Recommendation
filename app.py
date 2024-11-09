import streamlit as st
import numpy as np
import joblib
from PIL import Image
import base64
from io import BytesIO

# Load the model
app = joblib.load('crop app')

# Crop dictionary for output interpretation
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
    7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
    12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
    17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea", 22: "Coffee"
}

# Function to convert image to base64 for display
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Home", "Crop Prediction"])

# Home Page
if page == "Home":
    st.markdown(
    """
    <h1 style='text-align: center; 
               background-image: linear-gradient(to right, #12c2e9, #c471ed, #f64f59);
               -webkit-background-clip: text;
               color: transparent;'>
        Crop Prediction Application
    </h1>
    """, 
    unsafe_allow_html=True
)

    # Display home section image
    home_image = Image.open("img\\3.jpg")  # Change the path to your image
    st.image(home_image, width=600)  # Display the image with column width adjustment

    # Apply linear gradient to subheader "About the Project" with increased size
    st.markdown("""
    <h3 style='background-image: linear-gradient(to right, #C917D1, #A8EB12); 
               -webkit-background-clip: text; 
               color: transparent;
               font-size: 36px;'>About the Project</h3>
""", unsafe_allow_html=True)


    # Adding style for scrollable section
    st.markdown("""
    <style>
        .scrollable-text {
            height: 400px;
            overflow-y: scroll;
            padding-right: 15px;
            
            padding: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Scrollable content for About the Project
    st.markdown("""
    <style>
        .scrollable-text {
            height: 300px;
            overflow-y: scroll;
            padding-right: 15px;
        }
    </style>
    <div class="scrollable-text">
        <ul>
            <li><b>This project aims to provide an AI-powered application to predict the most suitable crop based on environmental conditions.</b> The model uses key factors such as nitrogen content, phosphorus content, potassium content, temperature, humidity, soil pH, and rainfall to determine the best crop to cultivate in a given region. By leveraging these environmental factors, the application enables farmers and agriculturalists to make informed decisions, ensuring optimal crop yield.</li>
            <li><b>In this project, we use the Random Forest Classifier, a powerful machine learning algorithm known for its ability to handle complex, high-dimensional data and for providing robust predictions in classification tasks.</b> Random Forest works by constructing multiple decision trees during training and outputs the mode of the classes (the most frequent class) as the prediction. This ensemble method makes the model more accurate and less prone to overfitting, which is crucial for agricultural predictions where data variability is high.</li>
            <li><b>The dataset used for training the model was sourced from Kaggle, a leading platform for data science competitions and datasets.</b> Kaggle provides a rich variety of datasets related to agriculture, including those containing environmental conditions and crop yields, which are essential for training the model.</li>
            <li><b>This combination of environmental data, machine learning, and the Random Forest algorithm provides a comprehensive tool for precision farming, helping optimize crop choice and improve yield outcomes by recommending crops that are best suited to the local climate and soil conditions.</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)



# Crop Prediction Page
if page == "Crop Prediction":
    st.markdown(
    """
    <h1 style='text-align: center; 
               background-image: linear-gradient(to right, #12c2e9, #c471ed, #f64f59);
               -webkit-background-clip: text;
               color: transparent;'>
        Crop Prediction Application
    </h1>
    """, 
    unsafe_allow_html=True
)

    st.write("Enter the environmental conditions to predict the best crop.")

    # Collecting user input for each feature
    with st.form("crop_form"):
        # First row: Nitrogen, Phosphorus, Potassium
        col1, col2, col3 = st.columns(3)
        with col1:
            N = st.number_input("Nitrogen Content (mg/kg)", min_value=0.0, max_value=100.0, value=0.0)
        with col2:
            P = st.number_input("Phosphorus Content (mg/kg)", min_value=0.0, max_value=100.0, value=0.0)
        with col3:
            K = st.number_input("Potassium Content (mg/kg)", min_value=0.0, max_value=100.0, value=0.0)

        # Second row: Temperature, Humidity
        col4, col5 = st.columns(2)
        with col4:
            temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=0.0)
        with col5:
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0)

        # Third row: Soil pH, Rainfall
        col6, col7 = st.columns(2)
        with col6:
            ph = st.number_input("Soil pH Level", min_value=0.0, max_value=14.0, value=6.5)
        with col7:
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=0.0)


    

        # Submit button
        submit_button = st.form_submit_button("Predict Crop")

    # Prediction processing after submission
    if submit_button:
        # Prepare the feature list and reshape for prediction
        features = np.array([N, P, K, temp, humidity, ph, rainfall]).reshape(1, -1)
        
        # Model prediction
        prediction = app.predict(features)
        
        # Check if the prediction is a valid crop
        crop = prediction[0]  # Assuming prediction is the crop name directly
        
        # Check if the crop is valid
        if crop in crop_dict.values():
            st.success(f"The best crop for these conditions is: **{crop}**")
            
            # Load and display the success image
            image = Image.open('img\\23.jpg')  # Replace with the path to your success image
            st.markdown(
                "<div style='display: flex; justify-content: center;'>"
                f"<img src='data:image/jpeg;base64,{image_to_base64(image)}' width='500'/>"
                "</div>", 
                unsafe_allow_html=True
            )
        else:
            st.warning("No suitable crop found for these conditions.")
            
            # Load and display the "no crop" image
            no_crop_image = Image.open('img\\45.jpg')  # Replace with the path to your "no crop" image
            st.markdown(
                "<div style='display: flex; justify-content: center;'>"
                f"<img src='data:image/jpeg;base64,{image_to_base64(no_crop_image)}' width='300'/>"
                "</div>", 
                unsafe_allow_html=True
            )
            # Footer section
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #FFFFFF;
            text-align: center;
            padding: 10px;
            font-size: 0.9em;
            
        }
    </style>
    <div class="footer">
        &copy; 2024 Niranjan Jha. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)

