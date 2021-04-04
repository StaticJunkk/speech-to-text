# Speech-to-Text
[![Python Version](https://img.shields.io/badge/python-3.7.2-brightgreen.svg)](https://python.org)

## Table of Contents
* [Idea behind the Project](#idea-behind-the-project)
* [Dataset Used](#dataset-used)
* [Hierarchy](#hierarchy)
* [Preprocessing Data](#preprocessing-data)
* [Training and Testing](#training and testing)
* [Deploying Locally Using Flask](#deploying-locally-using-flask)

## Idea Behind the Project
The idea was to create a Speech-to-sign converter, which could in a way ease the conversation with people
having speaking and hearing impairments. Since direct conversion seemed a little doubtful, the idea was to
break the overall process into two parts
* Speech to Text
* Text to Sign

While creating Speech to Text seemed very easy with Pyaudio library and various applications available from 
tech giants such as google, what intruiged me here was to see how exactly are the signals being processed. So,
the project swiftly got diverted. I ended up using Google's Speech Command Dataset to predict 31 command keywords.

P.S. I do hope I'll get to implement the Speech-to-sign thing, although a dataset for sign language isn't available
yet. If you do find one... let me know (;_;)

## Dataset Used
The dataset used for this project was [Google's Speech Command Dataset](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html).
It had audio samples, mostly of 1 sec of lenght, for 31 command keywords and few noises. A total of 65,000 audio samples are there. 
(Sadly, the size is too large ;_;)

## Hierarchy 
Let's quickly go over on how you are supposed to run the above code and how exactly the flow takes place.
### Running the code solely for getting the output from the model
If this is your objective, then you can simply run the server.py and client.py file. Make sure to have all the package requirements preinstalled.
Also, make sure to have the audio file ready. I'd suggest trimming the audio file to a length which only contains the audio and no black spaces. 
Using the rest of the code should be easy, although you might need a little knowledge of how flask works. There's no front space for the webapp, 
so it might not seem very colorful, but rest assured, it works anyway.

## Preprocessing
The audio samples were taken into frequency domain, but we didn't use the classical fourier transform. Instead, to mimic the way human ear responds to
various frequencies, we used Mel-frequency-cepstral coefficients. You can read more about them [here](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum#:~:text=Mel-frequency%20cepstral%20coefficients%20%28%20MFCCs%29%20are%20coefficients%20that,representation%20of%20the%20audio%20clip%20%28a%20nonlinear%20%22spectrum-of-a-spectrum%22%29.)
The data_generation file does this job for us and we saved all the coefficients in json format.

## Training and Testing

## Deploying Locally Using Flask

