
import streamlit as st
import pandas as pd
import numpy as np
import time
from sound import record, delete
import spot_keywords as sk
# import import_ipynb
# %run Spotting_keywords.ipynb


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
st.write("Now it works very easily... You just need to record yourself saying one of the keywords and then it's done!\nIt can be a little tricky though, so make sure you listen to the sound first. The timer is added for your benefit as it can be hard to tell when is it actually starting to record.\n ")
# st.write("Make sure you record first and then predict, else it is bound to show some error")
st.write("If you understood what I just said, then you can start by pressing the record button!")

if st.button("record"):
    # delete()
    with st.empty():
        for t in range(3):
            time.sleep(1)
            st.write("Recording will start in ", 2-t, "seconds")
        with st.spinner("recording..."):
            time.sleep(0.5)
            record(2)
        st.success("Done!")
    audio = open("output.wav", "rb")
    audio_byte = audio.read()
    st.audio(audio_byte, format='audio/wav')
    dp = sk.spotting_keywords()
    
    predicted_keyword = dp.predict("output.wav")
    st.balloons()
    # delete()
    st.write("The predicted keyword is: ", predicted_keyword)

        
