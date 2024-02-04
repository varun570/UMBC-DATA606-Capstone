# Forecasting Liquor Distribution Demand:

# A Machine Learning Approach

Prepared for UMBC Data Science Master Degree Capstone by

Dr Chaojie (Jay) Wang

Varun Balle

[GitHub](https://github.com/varun570)

[LinkedIn](https://www.linkedin.com/in/varun-balle-b4153a1b8/)

[PowerPoint file](https://drive.google.com/drive/folders/1V4bJ71uebxW-QcZm_aat0Ts9MdII879C?usp=sharing)

# Table of Contents

[Introduction](#_Toc157847838)

[What is demand Forecasting?](#_Toc157847839)

[Why do we Forecast Demand?](#_Toc157847840)

[Factors Affecting Demand Forecasting](#_Toc157847841)

[Beverage Alcohol Industry](#_Toc157847842)

[Proposed Workflow](#_Toc157847843)

[Data Description](#_Toc157847844)

[Target](#_Toc157847845)

[Features and Machine Learning Models](#_Toc157847846)

[1. Time series model](#_Toc157847847)

[2. Regression Model](#_Toc157847848)

[3. Deep Learning](#_Toc157847849)

[Evaluation And Results](#_Toc157847850)

[Closing Note](#_Toc157847850)

[References](#_Toc157847851)

# Introduction

## What is demand Forecasting?

Demand forecasting is the process of using predictive analysis of historical data to estimate and predict customers' future demand for a product or service. It helps the business make better-informed supply decisions that estimate the total sales and revenue for a future time.

Demand forecasting allows businesses to optimize inventory by predicting future sales. By analyzing historical sales data, demand managers can make informed business decisions about everything from inventory planning and warehousing needs to running flash sales and meeting customer expectations.

## Why do we Forecast Demand?

We want to predict the future so we can act now. Without demand, there is no business. Without a thorough understanding of demand, businesses aren't capable of making the right decisions about marketing spend, production, staffing, and more.

Demand Forecasting directly affects and helps with profit margins, cash flow, capital expenditure, future capacity planning, and more. It allows companies to optimize their inventory, increase turnover rates, and reduce warehousing costs.

It provides insight into upcoming cash flow. You will create a more accurate budget regarding suppliers and other operational expenses. It also enables you to invest more in business growth.

It assists in identifying and resolving any issues in the sales pipeline and supply chain operations to ensure the business runs optimally.

## Factors Affecting Demand Forecasting

- Economy: When the economy falls into recession and fewer people work, the demand for luxury products will decline. But, at the same time, demand for affordable products will likely increase.
- Geography: Where your customers reside and where you manufacture, store, and fulfill orders from can have a huge impact on inventory forecasting
- Inventory Management: Operational challenges, such as managing obsolete inventory, limited storage space, and high inventory carrying costs, can significantly impact the effectiveness of supply chain forecasting. Accurate forecasts help businesses optimize their inventory levels and better define safety stock, minimizing the risk of holding excess or obsolete stock and reducing storage and carrying costs.
- Competition: Competition affects demand as there are more options for your customers to choose from and more companies vying for their attention.
- Data Quality: One of the most significant challenges in demand forecasting is ensuring the quality and quantity of data used for analysis. Inaccurate, incomplete, or outdated data can lead to misleading forecasts, rendering them less useful for decision-making.

# Beverage Alcohol Industry

The beverage alcohol industry sustains 4.4 million jobs and generates a combined $69 billion in tax revenue at the federal, state, and local levels

The beverage alcohol industry isn't a one-size-fits-all market. It's a blend of channels, each with its distinct nuances and requirements. There's little room for error in this industry. A forecasting misstep can lead to overproduction, tying up capital and risking product obsolescence.

Factors in the beverage industry:

- Dependency on the agriculture industry
- Distributors
- National Chains
- DTC(Direct-to-consumer)

# Proposed Workflow

![Shape5](RackMultipart20240203-1-18iyuy_html_e5710b4b6e0d896e.gif) ![Shape2](RackMultipart20240203-1-18iyuy_html_8020e3484751888.gif) ![Shape3](RackMultipart20240203-1-18iyuy_html_8020e3484751888.gif) ![Shape4](RackMultipart20240203-1-18iyuy_html_e6eb0ad86e9de004.gif) ![Shape1](RackMultipart20240203-1-18iyuy_html_1d8c384e5431b8e9.gif)

<img width="873" alt="image" src="https://github.com/varun570/UMBC-DATA606-Capstone/assets/71378746/4a838f33-7b67-4a30-bda2-2f54813584d4">


# Data Description

[Link to dataset](https://www.kaggle.com/datasets/anandaramg/liquor-sales)

The data at hand was obtained from free source Kaggle. It consists of liquor sales data from cities all over the US for the year 2014-2015.

The dataset consists of 15000 rows and 22 columns. The columns are as follows:

- date (object)
- convenience\_store(object)
- store (int64)
- name (object)
- address (object)
- city (object)
- zipcode (object)
- store\_location (object)
- county\_number(int64)
- county (object)
- category (float64)
- category\_name (object)
- vendor\_no (int64)
- vendor (object)
- item (int64)
- description (object)
- pack (int64)
- liter\_size (int64)
- state\_btl\_cost (float64)
- btl\_price (float64)
- bottle\_qty (int64)
- total (float64)

All of the columns are relating to the various items that are at sold at mentioned locations in cities across the US and the item price on that specific date.

The dataset also gives us details of the vendor so as to assess which beverage vendors have the upper hand in the market and how other vendors can improve their business.

# Target

Now coming to the target variable, as previously mentioned the goal of demand forecasting is to forecast how much of something needs to be at a future point in time to not incur any loss and maximize as profit as we can.

After assessing the data, it is obvious to choose "total" as the target variable. Because the total attribute gives us the insight of the total sales number for each store\_loaction and corresponding vendor.

Forecasting this total sales amount will give us the results that we need to determine the inventory the company has to maintain and the orders that it'll need to place with manufacturers to avoid any product backorder.

# Features and Machine Learning Models

I would like to take up a three-faceted approach toward reaching my final goal of forecasting. Which will be as follows.

1. Time series model: It is the technique for the prediction of events through a sequence of time. It predicts future events by analyzing the trends of the past, on the assumption that future trends will be similar to historical trends. Although this assumption might not be foolproof that's where considering affecting factors such as geography and seasonality will be taken into consideration.

SARIMA stands for Seasonal Autoregressive Integrated Moving Average. It is a statistical model that is used to forecast time series data that exhibits seasonality. Seasonality refers to the regular and predictable fluctuations in a time series that occur over a period of time, such as daily, weekly, or monthly cycles.

SARIMA is an extension of the ARIMA model, which is used to forecast time series data without seasonality. The SARIMA model adds three additional parameters to the ARIMA model to account for seasonality.

1. Regression Model: Numerous combination and ensemble techniques have been developed to improve forecasting accuracy. Among the different machine learning models, tree-based methods dominate in both accuracy and uncertainty handling.

Deploying Extra tree-based regression (ETR) which is an ensemble model seems promising due to its ability to learn faster with smaller inputs. This will also give us a forecasting which will be a bit more product-focused by considering attributes such as category, item, and vendor details.

1. Deep Learning: Finally coming to the deep learning model LSTM. LSTM (Long Short-Term Memory) is a type of recurrent neural network architecture specifically designed to address the vanishing gradient problem that can occur in traditional RNNs when dealing with long sequences of data.

After performing all necessary data preprocessing steps, taking up the step of feature engineering to create new features like rolling averages and including other price-related features will be able to help us get a much more nuanced final result.

# Evaluation And Results

All three model results will be evaluated and necessary finetuning will be done in order to bring out utmost accuracy and results will be validated. The best model out of the three will be chosen as the for forecasting the sales numbers for the next 6-month and 12-month horizon.

The proposed final outcome will also be an interactive dashboard in which users can pick the category and item number and visualize the demand for set upcoming time frames.

# Closing Note

I have contacted major wholesale liquor distributors Chesapeake Beverage, RNDC, Breakthru Beverage, and Southern Glazeer for more real-time sales data for the state of Maryland. I am currently in discussion with them regarding sharing data as majority of the data consists customer information which will be sensitive and access will be subjective. The availability of this real-time data will be confirmed to me by the end of next week i.e. 02/10/2024. 

If I gain access to real-time data from at least one of these companies I will replace the current proposed dataset with the received one. Necessary changes will be made to the data and new EDA will be done, but the underlying project objective shall remain the same. 

The goal behind obtaining data from companies will be to have a direct relationship with industry leaders which will be advantageous for me in both my academic and career goals.

# References

[1] Arora, T., Chandna, R., Conant, S., Sadler, B., & Slater, R. (2020). Demand Forecasting In Wholesale Alcohol Distribution: An Ensemble Approach. _SMU Data Science Review_, _3_(1), 7. [https://scholar.smu.edu/cgi/viewcontent.cgi?article=1137&context=datasciencereview](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1137&context=datasciencereview)

[2] Ludlow, M., & Sadler, B. (2020). Demand Forecasting for Alcoholic Beverage Distribution. _SMU Data Science Review_, _3_(1), 5. [https://scholar.smu.edu/cgi/viewcontent.cgi?article=1131&context=datasciencereview](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1131&context=datasciencereview)

[3] Nasseri, M., Taha Falatouri, Brandtner, P., & Farzaneh Darbanian. (2023). Applying Machine Learning in Retail Demand Prediction—A Comparison of Tree-Based Ensembles and Long Short-Term Memory-Based Deep Learning. _Applied Sciences_, _13_(19), 11112–11112. [https://doi.org/10.3390/app131911112](https://doi.org/10.3390/app131911112)

[4] _Liquor Sales_. (n.d.). Www.kaggle.com. Retrieved February 3, 2024, from [https://www.kaggle.com/datasets/anandaramg/liquor-sales/data](https://www.kaggle.com/datasets/anandaramg/liquor-sales/data)

[5] _The Alcohol Beverage Industry: An Economic Engine_. (n.d.). Fourloko.com. [https://fourloko.com/alcohol-beverage-economic-impact/](https://fourloko.com/alcohol-beverage-economic-impact/)

[6] _The art and science of forecasting in the beverage alcohol industry_. (n.d.). Claret.app. Retrieved February 3, 2024, from [https://claret.app/blog/the-art-and-science-of-forecasting-in-the-beverage-alcohol-industry](https://claret.app/blog/the-art-and-science-of-forecasting-in-the-beverage-alcohol-industry)

[7] Lab, T. F. (n.d.). _6 Types of Demand Forecasting and Projection Benefits_. Www.thefulfillmentlab.com. [https://www.thefulfillmentlab.com/blog/demand-forecasting#factors](https://www.thefulfillmentlab.com/blog/demand-forecasting#factors)

[8] _Demand Forecasting Methods To Add To Your Playbook_. (n.d.). Cogsy. [https://cogsy.com/demand-planning/demand-forecasting/](https://cogsy.com/demand-planning/demand-forecasting/)

[9] Owczarek, D. (2023, April 22). _What makes demand forecasting difficult? Navigating the supply chain forecasting challenges_. Nexocode. [https://nexocode.com/blog/posts/supply-chain-forecasting-challenges/](https://nexocode.com/blog/posts/supply-chain-forecasting-challenges/)

[10] Hand, R. (2022, October 28). _What is Demand Forecasting? Importance and Benefits of Forecasting Customer Demand_. ShipBob. [https://www.shipbob.com/blog/demand-forecasting/#what-is](https://www.shipbob.com/blog/demand-forecasting/#what-is)

‌
