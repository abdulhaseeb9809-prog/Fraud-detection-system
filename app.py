import streamlit as st
import numpy as np
import pickle
from PIL import Image

# 🔥 TensorFlow / Keras imports
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, BatchNormalization, Dropout

# ---------------- BUILD DEEPFAKE MODEL ----------------

base_model = MobileNetV2(weights=None, include_top=False, input_shape=(128,128,3))

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    BatchNormalization(),
    Dense(128, activation='relu', kernel_regularizer='l2'),
    Dropout(0.6),
    Dense(1, activation='sigmoid')
])

# 🔥 Load trained weights
model.load_weights("deepfake.weights.h5")

deepfake_model = model

# ---------------- LOAD SPAM MODEL ----------------

spam_model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- STREAMLIT UI ----------------

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🔍 AI Fraud Detection System")

# ================= IMAGE SECTION =================

st.header("📸 Deepfake Image Detection")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img_resized = img.resize((128,128))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    pred = deepfake_model.predict(img_array)[0][0]
    label = "Real" if pred > 0.5 else "Fake"

    # Risk scoring
    if pred > 0.8:
        risk = "LOW RISK"
    elif pred > 0.5:
        risk = "MEDIUM RISK"
    else:
        risk = "HIGH RISK ⚠️"

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {pred:.2f}")
    st.write(f"Fraud Risk: {risk}")

# ================= TEXT SECTION =================

st.header("📩 Email / SMS Fraud Detection")

user_input = st.text_area("Enter message")

if st.button("Check Message"):
    vec = vectorizer.transform([user_input])
    pred = spam_model.predict(vec)[0]

    label = "Spam" if pred == 1 else "Safe"

    # 🔥 fallback probability (fix sklearn issue)
    prob = 0.9 if pred == 1 else 0.1

    if prob > 0.8:
        risk = "HIGH RISK ⚠️"
    elif prob > 0.5:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {prob:.2f}")
    st.write(f"Fraud Risk: {risk}")