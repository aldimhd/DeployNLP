import streamlit as st
import joblib
st.title("Sentiment Analyisis App")
st.subheader('Review anda tentang pelayanan hotel ini')
message = st.text_area(label="Enter the text of your hotel review")
pipe_lr = joblib.load(open('model_nlp.pkl','rb'))

if st.button('Analyze'):
  results = int(pipe_lr.predict([message]))
  sentiment_map = {0: "Respon Negatif", 1: "Respon Positif"}
  results = sentiment_map.get(results)
  st.success(results)