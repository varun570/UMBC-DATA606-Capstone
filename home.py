import streamlit as st

st.set_page_config(page_title="Liquor Sales Forecasting")
# Define session state variable (optional)
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Page layout and buttons
st.title("Liquor Sales Forecasting")

st.image("img/Home Page.jpeg", use_column_width=True)

col1, col2, col3, col4 = st.columns([1, 2, 2, 2])  # Adjust width ratios as needed

with col1:
    st.write("")  # Empty column for spacing

with col2:
    if st.button("HOME"):
        st.session_state["page"] = "home"  # Empty column for spacing

with col3:
    if st.button("INSIGHTS"):
        st.session_state["page"] = "data_insights"

with col4:
    if st.button("FORECASTER"):
        st.session_state["page"] = "forecaster"

    
# Conditional rendering based on session state
if st.session_state["page"] == "home":
    st.write("This application employs a multi-faceted approach, integrating Machine Learning (ML) techniques, to analyze and forecast the demand for liquor distribution.")
    st.write("The beverage alcohol industry isn't a one-size-fits-all market.")
    st.write("A forecasting misstep can lead to overproduction, tying up capital and risking product obsolescence.")
    st.write("Factors in the beverage industry:")
    with st.expander("1. Dependency on the Agriculture Industry:"):
        st.write("Fluctuations in crop yields due to weather, pests, or disease can disrupt the supply of raw materials, impacting production and potentially leading to shortages or price hikes.")
        st.write("ML models can integrate historical agricultural data to predict potential yield issues and their influence on liquor supply.")
    with st.expander("2. Distributors:"):
        st.write("Distributors act as the middlemen between producers and retailers. Their buying decisions significantly impact demand.")
        st.write("Including historical sales data from distributors in the ML models can help predict their future purchasing behavior.")
    with st.expander("3. National Chains:"):
        st.write("Large national grocery store chains and retailers have significant buying power and can influence consumer trends.")
        st.write("Analyzing sales data from these chains and incorporating it into the forecast can provide insights into consumer buying patterns and upcoming promotions.")
    with st.expander("4. DTC (Direct-to-Consumer):"):
        st.write("The growing trend of Direct-to-Consumer sales allows producers to sell directly to customers, bypassing traditional distribution channels.")
        st.write("Including sales data from DTC platforms in the ML models helps account for this growing market segment and its impact on overall demand.")
elif st.session_state["page"] == "data_insights":
    # Import and run data_insights.py content
    exec(open("data_insights.py").read())
elif st.session_state["page"] == "forecaster":
    # Import and run forecaster.py content
    exec(open("forecaster.py").read())
else:
    # Handle unexpected page state
    st.error("Invalid page state!")
