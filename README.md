<a id="readme-top"></a>


# Crop_Recommendation
## Explanatory Video for Sign Language Interpreter
https://github.com/user-attachments/assets/9aa7f949-1ef5-4624-a7d6-abc706ebc684


## Index: 
- [About The Project](#About-The-Project)
- [Key Features](#Key-Features)
- [Deployment](#Deployment)



  
## About The Project
This AI-powered crop prediction application helps farmers select the most suitable crops based on environmental factors like nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall. After testing various models, RandomForestClassifier was chosen for its accuracy. Built with Streamlit, the app provides a user-friendly interface where users can input environmental data to receive crop recommendations or, if none are suitable, a message indicating no match. This project demonstrates the practical application of machine learning in supporting agricultural decision-making.

# Key Features:
* Real-time Crop Prediction: The application uses input data to recommend optimal crops based on current environmental conditions, helping users make informed decisions in real time.
* Customizable Input Parameters: Built with a focus on agriculture, it uses a tailored set of parameters, including nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall, for precise crop recommendations.
* Model Training with Machine Learning Algorithms: Multiple models were tested (logistic regression, DecisionTreeClassifier, and RandomForestClassifier), with RandomForestClassifier ultimately chosen for its high accuracy.
* Deployment with Streamlit: The application is deployed using Streamlit, offering an interactive and user-friendly interface for seamless user engagement and accessibility.
* Future Expansion: Plans to refine the model further and potentially include additional environmental factors for even more accurate and broad crop prediction capabilities.:smile:

## Deployment

To deploy this project run
```bash
pip install streamlit
```
```bash
  streamlit run app.py
```

<p align="center">(<a href="#readme-top">back to top</a>)</p>
