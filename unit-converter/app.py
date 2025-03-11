import streamlit as st # Streamlit as a library for building a web apps

# Function to convert units based on predefined conversions factors or formulas 
def convert_units(value, units_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,   # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,    # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,     # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000       # 1 kilogram = 1000 grams
    }

    key = f"{units_from}_{unit_to}" # Generate a key based on the input and output units

    # Logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not found" # return a message if the conversion is not found 
    
st.title("Unit_Converter") # set the title of the web app

# user input: numerical value to convert 
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

units_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"]) # kisse convert krna chata hun
units_to = st.selectbox("Convert to:", ["meters", "kilometers","grams", "kilograms"]) # kisme convert karna chata hun 

# button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, units_from, units_to) # Call the conversion function
    st.write(f"Convert value: {result}") # Display the result