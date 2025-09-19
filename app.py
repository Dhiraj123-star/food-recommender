import streamlit as st
from utils.recommender import recommend_food

st.title("🥗 Food Recommendation System")

query = st.text_input("What kind of food are you craving today?")

if query:
    recommendations = recommend_food(query)
    st.subheader("Recommended Dishes:")
    for item in recommendations:
        st.markdown(f"**{item['name']}**: {item['description']}")