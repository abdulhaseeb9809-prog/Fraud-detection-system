# 🔍 AI Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## 🌐 Live Demo

https://fraud-detection-system-csgzrfksxgogwjcixkmyau.streamlit.app/

---

## 📌 Overview

This project is an AI-based fraud detection system designed to identify impersonation and fraudulent activities in digital environments.

The system focuses on:
- Detecting deepfake images used in identity fraud  
- Identifying spam or fraudulent messages (SMS/Email)  

It provides a practical solution for improving security in applications such as banking, onboarding, and digital communication.

---

## 🚀 Key Features

### 📸 Deepfake Image Detection
- Uses **Transfer Learning (MobileNetV2)**
- Classifies images as:
  - Real
  - Fake
- Helps detect impersonation attempts

---

### 📩 Text Fraud Detection
- Uses **TF-IDF + Logistic Regression**
- Detects:
  - Spam messages
  - Safe messages
- Useful for SMS and email filtering

---

### ⚠️ Fraud Risk Scoring
- Assigns risk levels:
  - 🟢 Low Risk  
  - 🟡 Medium Risk  
  - 🔴 High Risk  
- Makes the system more actionable

---

### 🌐 Web Application
- Built using **Streamlit**
- Simple and interactive UI
- Real-time predictions

---

## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Scikit-learn**
- **Streamlit**
- **Natural Language Processing (TF-IDF)**


---

## ▶️ Getting Started

### 1. Install Dependencies


pip install -r requirements.txt


### 2. Run the application


streamlit run app.py


---

## 🎯 Use Cases

- Banking fraud detection  
- Customer onboarding verification  
- Identity impersonation prevention  
- Spam detection systems  

---

## ⚠️ Note

- Full datasets are not included due to size constraints.
- The project focuses on demonstrating core functionality and working prototype.

---

## 🔮 Future Improvements

- Video-based deepfake detection  
- Voice fraud detection  
- Real-time API integration  
- Improved model accuracy with larger datasets  

---

## 👨‍💻 Author

**Abdul Haseeb**

