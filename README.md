# 🛍️ AI-Powered Independent Shopping System for the Visually Impaired

This project empowers visually impaired individuals by offering a smart, AI-based shopping assistant. It leverages deep learning (ANN), computer vision (Haar Cascades, Gaussian Feature Extractors), and voice-guided navigation (HMM) to provide personalized clothing recommendations and guide users through retail environments.

---

## ✨ Features
- 🎯 **Real-time Object Detection** with Haar Cascades
- 🧠 **Personalized Outfit Recommendations** using ANN
- 🌈 Detects **gender, size, and color**
- 🗣️ **Voice-based guidance** powered by Hidden Markov Models
- 👕 Tailored suggestions for clothing items
- 🧭 VR Integration for immersive shopping

---

## 🧪 Technologies Used
- Python
- OpenCV
- TensorFlow / Keras (for ANN)
- HMM Toolkit (like `hmmlearn`)
- VR: Unity3D or WebVR (optional enhancement)
- Hardware: Webcam or depth-sensing camera

---

## 📂 Project Structure
```bash
ai-shopping-assistant/
│
├── data/
│   └── sample_videos/           # Input test videos
├── src/
│   ├── video_acquisition.py     # Webcam input
│   ├── frame_conversion.py
│   ├── pre_processing.py
│   ├── feature_extraction.py
│   ├── ann_classifier.py
│   └── hmm_voice_guidance.py
├── assets/
│   └── haar_cascades/           # XML models for face/eye detection
├── README.md
├── requirements.txt
└── app.py                       # Main script
