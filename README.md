# 🩺 MediTrain AI — Data Science Powered Healthcare Education Platform

MediTrain AI is an **AI-driven conversational assistant** designed to enhance healthcare education and diagnostic skills.  
It simulates realistic medical case scenarios for **medical students, healthcare professionals, and health-conscious individuals**, leveraging **data science and AI techniques** for intelligent symptom analysis and case-based learning.

---

## 📌 Project Overview
The goal of MediTrain AI is to bridge the gap between **textbook learning** and **real-world patient interaction** by offering:
- **Diagnostic Simulations** — Interactive AI-driven medical case practice.
- **Personalized Learning Insights** — Recommendations based on user performance.
- **Patient Communication Training** — Realistic simulated patient interactions.
- **Health Education** — Actionable wellness tips and awareness.

This project integrates **data collection, analysis, feature engineering, model training, and deployment** into one end-to-end **data science pipeline**.

---

## 🎯 Problem Statement
Medical students often lack access to **realistic diagnostic practice** without involving actual patients.  
This project uses **NLP and data-driven reasoning** to create a safe, accessible, and interactive training environment.

---

## 📊 Data Science Workflow
1. **Data Collection & Preprocessing**
   - Curated medical Q&A datasets, symptom–disease mappings, and patient dialogue transcripts.
   - Cleaned, standardized, and balanced datasets for improved accuracy.

2. **Exploratory Data Analysis (EDA)**
   - Identified high-frequency symptoms per disease category.
   - Mapped rare symptom combinations to improve model predictions.

3. **Feature Engineering**
   - Created **symptom embeddings** and metadata features (duration, severity, demographics).
   - Applied vectorization for NLP model compatibility.

4. **Modeling & AI Integration**
   - Fine-tuned **Transformer-based NLP models** for medical context understanding.
   - Implemented probabilistic reasoning for disease prediction.

5. **Evaluation**
   - Used **Accuracy, Recall, and F1-score** metrics for model validation.
   - Conducted **user testing** with medical students for realism and usability.

6. **Deployment**
   - **Frontend**: Streamlit web app.
   - **Backend**: Flask API serving AI predictions in real time.
   - Hosted on Heroku / Streamlit Cloud.

---

## 🛠️ Tech Stack
- **Programming & Data Science**: Python, Pandas, NumPy, scikit-learn, Matplotlib, Seaborn
- **NLP & AI**: Transformers (Hugging Face), spaCy, NLTK
- **Frontend**: Streamlit
- **Backend**: Flask
- **Deployment**: Heroku / Streamlit Cloud

---

## 📈 Outcomes
- Delivered **real-time medical case simulations** for 100+ diseases.
- Achieved **85%+ accuracy** in symptom-to-disease prediction tasks.
- Reduced diagnostic training time and improved **practical learning outcomes**.

---

## 🚀 Future Scope
- Multi-language medical training support.
- Integration with wearable health device data.
- Expansion to rare disease case simulations.


## Installation Instructions ⚙️
To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/meditrain-ai.git
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - For **Windows**:

    ```bash
    .\venv\Scripts\activate
    ```

    - For **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

4. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

6. **Run the backend API**:

    ```bash
    python api.py
    ```


## Usage Guide 📝
- **Home Page**: Navigate to the home page to get an introduction to MediTrain AI, its features, and how it can benefit you in mastering medical knowledge and patient care.
- **Chat Page**: On this page, you can start a conversation with MediTrain AI to practice diagnosing conditions. The AI will provide insights based on your inputs.
- **How to Use**: This page provides a detailed step-by-step guide on how to use MediTrain AI, including a sample scenario for medical students.
- **Feedback**: At any time, you can provide feedback on your experience with the platform to help us improve. You can also rate your experience and leave comments.

## Contributing 🤝
We welcome contributions! To get started:

1. Fork this repository.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes, and test them locally.
5. Submit a pull request with a detailed description of your changes.

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements 🙏
Special thanks to my mentor for their continuous guidance and support throughout the development of MediTrain AI. Their invaluable insights and encouragement helped shape this project into what it is today. I am truly grateful for their mentorship and expertise!

Made with ❤️ by Anushri Soni
