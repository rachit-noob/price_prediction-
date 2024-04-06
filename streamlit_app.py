import streamlit as st
import joblib

def load_model():
    # Load the pre-trained model
    model = joblib.load("regmodel.pkl")
    return model

@st.cache
def predict(model, input_data):
    # Perform prediction using the loaded model
    prediction = model.predict(input_data.reshape(1, -1))
    return prediction

def main():
    # Load the model
    model = load_model()

    # Set title and header
    st.title("Boston House Price Prediction")
    st.header("Enter the details to predict house price")

    # Input form for user input
    CRIM = st.text_input("CRIM")
    ZN = st.text_input("ZN")
    INDUS = st.text_input("INDUS")
    CHAS = st.text_input("CHAS")
    NOX = st.text_input("NOX")
    RM = st.text_input("RM")
    Age = st.text_input("Age")
    DIS = st.text_input("DIS")
    RAD = st.text_input("RAD")
    TAX = st.text_input("TAX")
    PTRATIO = st.text_input("PTRATIO")
    B = st.text_input("B")
    LSTAT = st.text_input("LSTAT")

    # Convert input values to numpy array
    input_data = [CRIM, ZN, INDUS, CHAS, NOX, RM, Age, DIS, RAD, TAX, PTRATIO, B, LSTAT]
    input_data = [float(i) for i in input_data]

    # Check if all inputs are provided
    if all(input_data):
        # Make prediction
        prediction = predict(model, input_data)

        # Display prediction
        st.write("Prediction:", prediction)
    else:
        st.write("Please provide all input values")

if __name__ == "__main__":
    main()
