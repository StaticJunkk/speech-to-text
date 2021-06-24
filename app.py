
import streamlit as st
import os

import spot_keywords as sk

fs = 44100
mappings = ["bed",
            "bird",
            "cat",
            "dog",
            "down",
            "eight",
            "five",
            "four",
            "go",
            "happy",
            "house",
            "left",
            "marvin",
            "nine",
            "no",
            "off",
            "on",
            "one",
            "right",
            "seven",
            "sheila",
            "six",
            "stop",
            "three",
            "tree",
            "two",
            "up",
            "wow",
            "yes",
            "zero",
            "_background_noise_"]

st.title("Keyword Detector")
st.write("\n")
st.subheader("Hola! I hope you are doing well!")
st.write("This is the deployment of a basic keyword spotter based on the [Google Speech Command Dataset.](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html)\nYou can find the entire codebase on [my GitHub repo.](https://github.com/StaticJunkk/speech-to-text)")
st.write("\nHere's the list of all the supported keywords")
with st.beta_expander("Supported Keywords"):
    st.write(mappings)
st.write("Now it works very easily... You just need to record yourself saying one of the keywords, preferably for one or two second, upload the file and then it's done!\nIt can be a little tricky though, so make sure you listen to the sound first. ")
# st.write("Make sure you record first and then predict, else it is bound to show some error")
st.write("If you understood what I just said, then you can start by pressing the upload button!")
st.write("You can use this file for trial purpose as well [demo file](https://github.com/StaticJunkk/speech-to-text/blob/master/up.ogg)")

uploaded_file = st.file_uploader("Pick an audio file", type=['ogg', 'wav', 'mp3'])
if uploaded_file is not None:
    upb = st.audio(uploaded_file, format='audio/wav')
    with open(os.path.join(os.getcwd(),"output.wav"),"wb") as f:
         f.write(uploaded_file.getbuffer())
    dp = sk.spotting_keywords()
    
    predicted_keyword = dp.predict("output.wav")
    st.balloons()
    # delete()
    st.write("The predicted keyword is: ", predicted_keyword)

        
