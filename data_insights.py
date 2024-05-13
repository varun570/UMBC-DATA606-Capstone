import streamlit as st
import numpy as np
import joblib

# Streamlit app
def main():
    st.title("Data Insights")

    # Display Images
    st.image("img/Total Liquor Sales in Iowa State (2019-2021).png", caption="Total Liquor Sales in Iowa State (2019-2021): By analyzing the line plot, you can identify patterns in sales overtime there is an evident upward trend signifies that the liquor sales business is potentially growing and generating more revenue over time Growth from 2019-2020 was pretty linear where as it took a sudden bump in 2020 this could be accredited to the COVID-19 pandemic which hindered buyers' ability to purchase and steady incline was seen from 2020 to 2021s.", use_column_width=True)
    st.image("img/Top Selling Liquor Categories (2019-2021).png", caption="Top Selling Liquor Categories (2019-2021): From the plot, we can see that American Vodkas were the best selling category with Whiskey Liqueur and Canadian Whiskey Coming in second and third place", use_column_width=True)
    st.image("img/Top Selling Liquor Items (2019-2021).png", caption="Top Selling Liquor Items (2019-2021): From the plot, we can see that Titos Vodkas were the best-selling category with Black Velvet and Crown Royal coming in second and third place", use_column_width=True)
    st.image("img/Average bottles sold per month.png", caption="Average bottles sold per month: Considering the specific dates from January 2019 to January 2020 we can see a rise in sales numbers around holiday seasons such as Christmas and New years", use_column_width=True)
    st.image("img/Revenue (2019-2021).png", caption="Revenue (2019-2021): The product with the most revenue is AMERICAN VODKAS with a total revenue of 171,330,323 USD", use_column_width=True)
    st.image("img/Monthly Sales Trend by Year (2019-2021).png", caption="Monthly Sales Trend by Year (2019-2021)", use_column_width=True)
    st.image("img/Sales by Day of Week (2019-2021).png", caption="Sales by Day of Week (2019-2021)", use_column_width=True)
    st.image("img/Monthly Sales Trend (2019-2021).png", caption="Monthly Sales Trend (2019-2021)", use_column_width=True)
    st.image("img/Sales Impact of Holidays (2019-2021).png", caption="Sales Impact of Holidays (2019-2021)", use_column_width=True)
    st.image("img/Seasonal Consumption.png", caption="Seasonal Consumption", use_column_width=True)
    st.image("img/ARIMA Sales Forecast.png", caption="ARIMA Sales Forecast", use_column_width=True)

if __name__ == "__main__":
    main()

