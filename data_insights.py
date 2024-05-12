import streamlit as st
import numpy as np
import joblib

# Streamlit app
def main():
    st.title("Data Insights")

    # Display Images
    st.image("img/Total Liquor Sales in Iowa State (2019-2021).png", caption="Total Liquor Sales in Iowa State (2019-2021)", use_column_width=True)
    st.image("img/Top Selling Liquor Categories (2019-2021).png", caption="Top Selling Liquor Categories (2019-2021)", use_column_width=True)
    st.image("img/Top Selling Liquor Items (2019-2021).png", caption="Top Selling Liquor Items (2019-2021)", use_column_width=True)
    st.image("img/Average bottles sold per month.png", caption="Average bottles sold per month", use_column_width=True)
    st.image("img/Revenue (2019-2021).png", caption="Revenue (2019-2021)", use_column_width=True)
    st.image("img/Monthly Sales Trend by Year (2019-2021).png", caption="Monthly Sales Trend by Year (2019-2021)", use_column_width=True)
    st.image("img/Sales by Day of Week (2019-2021).png", caption="Sales by Day of Week (2019-2021)", use_column_width=True)
    st.image("img/Monthly Sales Trend (2019-2021).png", caption="Monthly Sales Trend (2019-2021)", use_column_width=True)
    st.image("img/Sales Impact of Holidays (2019-2021).png", caption="Sales Impact of Holidays (2019-2021)", use_column_width=True)
    st.image("img/Seasonal Consumption.png", caption="Seasonal Consumption", use_column_width=True)
    st.image("img/ARIMA Sales Forecast.png", caption="ARIMA Sales Forecast", use_column_width=True)

if __name__ == "__main__":
    main()

