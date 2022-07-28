import numpy as np
import pandas as pd
import streamlit as st 
import joblib

classifier=joblib.load('modeln.pkl')


def welcome():
    return "Welcome All"


def predict_musicgenere(popularity,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,mode,speechiness,valence):

    prediction=classifier.predict(pd.DataFrame({'popularity':[popularity],'acousticness':[acousticness],"danceability":[danceability],"duration_ms":[duration_ms],'energy':[energy],'instrumentalness':[instrumentalness],'liveness':[liveness],"loudness":[loudness],"mode":[mode],"speechiness":[speechiness],"valence":[valence]}))

    return prediction
  
      
def main():
    st.title("Titanic")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit music_genere ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    popularity= st.text_input("popularity","Type Here")
    acousticness= st.text_input("acousticness","Type Here")
    danceability= st.text_input("danceability","Type Here")
    duration_ms = st.text_input("duration_ms","Type Here")
    energy= st.text_input("energy","Type Here")
    instrumentalness= st.text_input("instrumentalness","Type Here")
    liveness= st.text_input("liveness","Type Here")
    loudness= st.text_input("loudness","Type Here")
    mode= st.text_input("mode","Type Here")
    speechiness= st.text_input("speechiness","Type Here")
    valence= st.text_input("valence","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_musicgenere(popularity,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,mode,speechiness,valence)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()        
