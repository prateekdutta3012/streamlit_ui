import numpy as np
import pickle
import pandas as pd
import base64
import time

from gtts import gTTS
import os

import streamlit as st 

from PIL import Image

image = Image.open('Klogo.png')
st.image(image)

st.write("""
#  AI Generated Spokesperson
""")
st.write('Create videos from plain text in minutes with AI video creation platform.')

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('mask_group.jpg')


def main():
    txt = st.text_area('Enter your text')
    st.write('The content of transcript is: ', (txt))
    
    
    if st.button("Start processing"):
        with st.spinner('Wait for it...'):
            time.sleep(4)
            st.success('Now click on "Run Audio"')
        #"""English US _ speed slow"""
        mytext = txt
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=True)
        myobj.save("My_Audio.mp3")
        
        #Playing the converted file
        #os.system("My_Audio.mp3")


    # Audio bar
    st.write("""
    #  Audio generated from Transcript
    """)

    if st.button("Run Audio"):
        audio_file = open('My_Audio.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/ogg')
    
    #Video display
    st.write("""
    # Model Generated video
    """)

    if st.button("Show Result"):

        video_file = open('result_voice (1).mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

if __name__=='__main__':
    main()