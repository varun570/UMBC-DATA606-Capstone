import streamlit as st
import numpy as np
import joblib

# Load trained models with absolute paths
svm_model = joblib.load('svm_regressor_model.pkl')
knn_model = joblib.load('knn_regressor_model.pkl')

# Define mappings for categorical features
category_mapping = {'AMERICAN VODKAS': 1, 'CANADIAN WHISKIES': 2, 'STRAIGHT BOURBON WHISKIES': 3, 'WHISKEY LIQUEUR': 4, 'AMERICAN FLAVORED VODKA': 5}
store_name_mapping = {'HY-VEE #3 / BDI / DES MOINES': 1, 'CENTRAL CITY 2': 2, 'CENTRAL CITY LIQUOR, INC.': 3, 'HY-VEE FOOD STORE / CEDAR FALLS': 4, 'HY-VEE WINE AND SPIRITS / BETTENDORF': 5}
city_mapping = {'DES MOINES': 1, 'CEDAR RAPIDS': 2, 'DAVENPORT': 3, 'WATERLOO': 4, 'WEST DES MOINES': 5}
county_mapping = {'POLK': 1, 'LINN': 2, 'SCOTT': 3, 'BLACK HAWK': 4, 'JOHNSON': 5}
bottle_volume_ml_mapping = {'50' : 1, '100' : 2, '200' : 3, '375' : 4, '750' : 5, '1750' : 6}

# Function to preprocess input data
def preprocess_input(store_number, store_name, city, county, category, vendor_number, pack, bottle_volume_ml, state_bottle_cost):
    # Convert categorical features to numerical using mappings
    category = category_mapping.get(category, 0)  # 0 is default if not found
    store_name = store_name_mapping.get(store_name, 0)
    city = city_mapping.get(city, 0)
    county = county_mapping.get(county, 0)

    return np.array([store_number, store_name, city, county, category, vendor_number, pack, bottle_volume_ml, state_bottle_cost]).reshape(1, -1)

# Function to predict sales
def predict_sales(input_data):
    svm_pred = svm_model.predict(input_data)
    knn_pred = knn_model.predict(input_data)
    return svm_pred[0], knn_pred[0]

# Streamlit app
def main():
    # User inputs
    st.sidebar.header('USER INPUT')
    store_number = st.sidebar.number_input("Store ID", placeholder="Enter Store ID")

    # Use dropdown menus for categorical features
    category = st.sidebar.selectbox("Category", list(category_mapping.keys()), index=None, placeholder="Select Category",)
    store_name = st.sidebar.selectbox("Store Name", list(store_name_mapping.keys()), index=None, placeholder="Select Store",)
    city = st.sidebar.selectbox("City", list(city_mapping.keys()), index=None, placeholder="Select City",)
    county = st.sidebar.selectbox("County", list(county_mapping.keys()), index=None, placeholder="Select County",)
    bottle_volume_ml = st.sidebar.selectbox("Bottle Volume (ml)", list(bottle_volume_ml_mapping.keys()), index=None, placeholder="Select Bottle Volume")
    
    vendor_number = st.sidebar.number_input("Vendor Number(1-20)", placeholder="Enter Vendor Number")
    pack = st.sidebar.number_input("Packs(Maximum 30)",  placeholder="Enter Number of Packs")
    state_bottle_cost = st.sidebar.number_input("State Bottle Cost",  placeholder="Enter Bottle Cost")
    
    # Prediction
    if st.sidebar.button("Predict"):
        # Show loading indicator while predicting
        with st.spinner('Predicting...'):
            input_data = preprocess_input(store_number, store_name, city, county, category, vendor_number, pack, bottle_volume_ml, state_bottle_cost)
            svm_pred, knn_pred = predict_sales(input_data)
        
        # Once prediction is done, display the results
        st.success('Prediction complete!')
        #st.write("Predicted Sales (SVM): $ {:.2f}".format(svm_pred))
        st.write("Predicted Sales : $ {:.2f}".format(knn_pred))

if __name__ == "__main__":
    main()

