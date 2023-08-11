import base64
import streamlit as st
import requests
import numpy as np
from PIL import Image
from model.generate_caption import *
import os
import gtts
from playsound import playsound
import webbrowser



# Custom CSS
STYLE = """
h1 {
   color: #0c7489;
   font-size: 42px;
}

h2 {
   
   font-size: 32px;
}

p {
  color: #ffffff;
  font-size: 22px;
}
"""

st.markdown(f'<style>{STYLE}</style>', unsafe_allow_html=True)


# Add project title and details  
st.title("Visual AID for the Visually Impaired 👀")

st.header("About this Project 📋")
st.write("""
This project utilizes image captioning 🖼️ and text-to-speech technology 🗣️ to provide a visual aid for blind or visually impaired individuals. It is designed to help describe photos or live environments to give users better situational awareness. 

The model is trained 🧠 to generate descriptive captions for images, which are then read aloud using text-to-speech 🎤. This allows visually impaired users to get quick audio descriptions of their surroundings.

This project is part of the Intel OneAPI Hackathon 2023, using Intel OneDNN library & OneDAL library 💻 and software tools.
""")

# Existing code to run image captioning model  

st.header("Project Demo 🎥")
st.write("Here you can try out the visual assistant by uploading an image:")

uploaded_files = st.file_uploader("Upload some file", accept_multiple_files=True)



for uploaded_file in uploaded_files:
  bytes_data = uploaded_file.read()
  st.write("filename:", uploaded_file.name)

  print('Name of the file upload is: ',uploaded_file.name)
  location = f'Upload/{uploaded_file.name}'
  with open(os.path.join("Upload",uploaded_file.name),"wb") as f: 
    f.write(uploaded_file.getbuffer())
  
  pred_caption = generate_caption(location)
  
  st.image(location)
  st.write(pred_caption)

  # Convert predicted caption to speech
  tts = gtts.gTTS(pred_caption)
  audio_file = 'audio_'+uploaded_file.name+'.mp3'
  tts.save(audio_file)

  # Convert audio to base64
  audio_bytes = open(audio_file, "rb").read()
  audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
  # Embed audio in HTML
  html_audio = f"<audio controls><source src='data:audio/mp3;base64,{audio_b64}' type='audio/mp3'></audio>" 


  
  
  
  st.write('______________________________________________________________')

url = 'https://github.com/viveklistenus'

st.button('View on GitHub', on_click=webbrowser.open_new_tab, args=(url,))



for i in range(0,len(uploaded_files),2):
  cols = st.columns(2)
  try:
    cols[0].image(f'Upload/{uploaded_files[i].name}', use_column_width=True)
    cols[0].text(generate_caption(f'Upload/{uploaded_files[i].name}'))
    
    cols[1].image(f'Upload/{uploaded_files[i+1].name}', use_column_width=True) 
    cols[1].text(generate_caption(f'Upload/{uploaded_files[i].name}'))
  except KeyError:
    pass
