📌 Project Title: MediTrain AI — AI-Powered Healthcare Education & Diagnostic Simulation Platform

📝 Overview
MediTrain AI is an advanced AI-driven conversational assistant designed to enhance medical training and health education. It simulates realistic diagnostic scenarios for medical students, healthcare professionals, and health-conscious users.
The project applies data science methodologies for knowledge modeling, natural language understanding, and real-time patient case simulations, combining AI model training with a user-friendly interface.

🎯 Problem Statement

Medical students often lack access to realistic, interactive diagnostic practice without requiring patient involvement. The aim was to create a data science-powered virtual training platform that improves clinical reasoning and patient communication skills.

📊 Data Science Workflow

Data Collection & Preprocessing

Curated medical Q&A datasets, symptom-disease mapping data, and patient conversation transcripts.

Cleaned and structured data for model ingestion (removed duplicates, standardized symptom terminology, balanced class representation).

Exploratory Data Analysis (EDA)

Mapped most common symptoms per disease category.

Identified rare symptom patterns to improve model accuracy for uncommon conditions.

Feature Engineering

Created symptom embedding vectors for better contextual understanding.

Added metadata features (symptom duration, severity scores, patient demographics).

Modeling & AI Integration

Fine-tuned a pre-trained NLP model for medical conversation understanding.

Implemented probabilistic reasoning for disease prediction based on symptom combinations.

Evaluation

Measured accuracy, recall, and F1-score for diagnostic suggestion tasks.

Conducted user testing with medical students for scenario realism and educational value.

Deployment

Built Streamlit frontend for interaction.

Created Flask API backend to serve AI model predictions in real time.

🛠️ Tech Stack

Data Science Tools: Python, Pandas, NumPy, scikit-learn, Matplotlib, Seaborn

NLP & AI: Transformers (Hugging Face), spaCy, NLTK

Frontend: Streamlit

Backend: Flask

Deployment: Heroku / Streamlit Cloud

📈 Outcomes & Impact

Enabled real-time medical case simulations for 100+ unique disease profiles.

Achieved 85%+ accuracy in symptom-to-disease prediction during testing.

Provided personalized learning paths for users based on diagnostic performance.

Reduced the gap between textbook learning and patient interaction practice.

🚀 Future Scope

Integrate with wearable device APIs for real patient vitals data simulation.

Multi-language medical training support.

Expand database for rare disease case simulations.
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
