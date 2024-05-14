# 1. Liquor Sales Forecasting

- **Project Title:** Liquor Sales Forecasting
- **Prepared for** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author:** Varun Balle
- **GitHub:** https://github.com/varun570
- **LinkedIn:** http://www.linkedin.com/in/varun-balle
- **Portfolio:** https://varun570.github.io/
- **PowerPoint Presentation:** https://docs.google.com/presentation/d/1ho2J2YmaCzj9rmGVDYqgpGSyUjWuMiiu/edit?usp=sharing&ouid=106355446175748978087&rtpof=true&sd=true
- **Streamlitapp:** https://liquorsalesforecasting.streamlit.app/
- **YouTube Video:** https://youtu.be/z9P7tOCCOZ0

# 2. Background
The project leverages data-driven forecasting to predict future liquor sales trends. Analyzes factors like consumer preferences, economic conditions, and seasonality to refine forecasts. Empowers businesses to anticipate market demands and make data-backed strategic choices. Enables businesses to optimize inventory management, pricing strategies, and marketing efforts. Aims to provide valuable insights that contribute to improved overall business performance in the liquor industry.

**Research Questions:**
1. What historical sales data and market factors can be effectively utilized to develop an accurate forecasting model for future liquor sales trends?
2. How can a data-driven liquor sales forecast empower businesses to make strategic decisions regarding inventory management, and pricing strategies? 
3. To what extent can the implementation of a data-driven liquor sales forecasting model contribute to improved business performance metrics within the beverage industry?

# 3. Data

## Data Sources
- The dataset provided by https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy
- This is data collected directly by the State of Iowa.

## Data Size
- The dataset is approximately 2GB+.
- The dataset contains ~ 7M rows and 24 columns

## Period
- Data is from 2019-2021

## Data Dictionary
1. invoiceanditemnumber: concatenated invoice and line number associated with the liquor order. This provides a unique identifier for the individual liquor products included in the store order. 
2. date: date of order. 
3. storenumber: unique number assigned to the store that ordered the liquor.
4. storename: name of store that ordered the liquor. 
5. address: address of store that ordered the liquor. 
6. city: city where the store that ordered the liquor is located. 
7. zipcode: zip code where the store who ordered the liquor is located.
8. storelocation: location of store that ordered the liquor. The address, city, state, and zip code are geocoded to provide geographic coordinates.
9. countynumber: Iowa county number for the county where the store that ordered the liquor is located.
10. county: the county where the store that ordered the liquor is located.
11. category: category code associated with the liquor ordered.
12. categoryname: category of the liquor order. 
13. vendornumber: the vendor number of the company for the brand of liquor ordered.
14. vendorname: the vendor name of the company for the brand of liquor ordered. 
15. itemnumber: item number for the individual liquor product ordered.
16. itemdescription: description of the individual liquor product ordered. 
17. pack: the number of bottles in a case for the liquor ordered.
18. bottlevolumeml: volume of each liquor bottle ordered in milliliters.
19. statebottlecost: the amount that the alcoholic beverages division paid for each bottle of liquor ordered. 
20. statebottleretail: the amount the store paid for each bottle of liquor ordered. 
21. bottlessold: the number of bottles of liquor ordered by the store.
22. saledollars: total cost of liquor order (number of bottles multiplied by the state bottle retail). 
23. volumesoldliters: total volume of liquor ordered in liters. (i.e. (bottle volume (ml) x bottles sold)/1,000). 
24. volumesold_gallons: total volume of liquor ordered in gallons. (i.e. (bottle volume (ml) x bottles sold)/3785.411784).

## Features/Predictors
- Potential features for the ML models include:
  - Store Number
  - Category
  - Store Name
  - City
  - County
  - Bottle Volume(ml)
  - Vendor Number
  - Packs 
  - State Bottle Cost

# Model Training

## 1. Models for Predictive Analytics:
We will use regression-based, time series analysis and neural networks:
  - Linear Regression
  - KNN
  - SVM Regressor
  - ARIMA
  - LSTM

## 2. Training Procedure:
For Regression-based prediction, we are using Linear Regression, Support Vector Machine Regressor, KNN, and time series analysis utilizing ARIMA. And coming to neural network LSTM is utilized  

## 3. Python Packages:
We will primarily use the following Python packages for model training and evaluation:
- Data Manipulation and Cleaning:
  - pandas
- Data Exploration and Visualization:
  - NumPy
  - Matplotlib
  - Seaborn
- Machine Learning
 - Scikit-learn
 - SVR
 - KNeighborsRegressor
 - StandardScaler
 - LinearRegression

## 4. Development Environments:
We can develop and train our models in various environments:
- Local machine: Using Jupyter Notebook 
- Online platforms: Google Colab, Streamlit

## 5. Web App Development:
Developed a web application using Streamlit for users to interact with our trained forecasting models. 
- **Streamlitapp:** https://liquorsalesforecasting.streamlit.app/

# Conclusion

This liquor sales forecasting project leverages a 2GB+ dataset (2019-2021) to train various models (Linear Regression, ARIMA, LSTM) for predicting future trends. By analyzing factors like store location, category, and bottle volume, the project aims to empower businesses with data-driven insights to optimize inventory, pricing, and marketing strategies, ultimately contributing to improved overall business performance in the liquor industry.

