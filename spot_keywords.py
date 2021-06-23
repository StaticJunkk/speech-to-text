from tensorflow import keras
import numpy as np
import librosa as lb


model_path = "model.h5"

NUM_SAMPLES = 22050


class _spotting_keywords:

    model = None

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

    _instance = None

    def predict(self, file_path):
        MFCCs = self.preprocess(file_path)

        MFCCs = MFCCs[np.newaxis, ..., np.newaxis]

        predictions = self.model.predict(MFCCs)
        predicted_index = np.argmax(predictions)

        predicted_keyword = self.mappings[predicted_index]

        _spotting_keywords._instance = None
        return predicted_keyword

    def preprocess(self, file_path, n_mfcc=13, n_fft=2048, hop_length=512):
        signal, sr = lb.load(file_path)
        if len(signal) > NUM_SAMPLES:
            signal = signal[:NUM_SAMPLES]

        MFCCs = lb.feature.mfcc(signal, n_mfcc=n_mfcc,
                                n_fft=n_fft, hop_length=hop_length)

        return MFCCs.T

def spotting_keywords():
    if _spotting_keywords._instance is None:
        _spotting_keywords._instance = _spotting_keywords()
        _spotting_keywords.model = keras.models.load_model(model_path)

    return _spotting_keywords._instance

# if __name__ == "__main__":
#     sp = spotting_keywords()
#     keyword1 = sp.predict("test/up.wav")

#     print(f"The audio file corresponds to : {keyword1}")
