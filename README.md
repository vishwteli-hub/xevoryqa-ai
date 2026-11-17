
# 🛡️ ScamShield AI

### AI-Powered Suspicious Message Analyzer

ScamShield AI is a machine-learning-based application that analyzes SMS messages to identify potential spam and suspicious patterns.

It combines machine learning, rule-based detection and a locally running Qwen LLM to provide an initial risk assessment and practical safety advice.

## ✨ Features

- SMS spam classification using Machine Learning
- TF-IDF text vectorization
- Logistic Regression classifier
- Suspicious pattern detection
- Combined risk assessment
- Local Qwen AI explanations using LM Studio
- Streamlit web interface
- Model performance visualization

## 🧰 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib
- Joblib
- LM Studio
- Qwen LLM

## ⚙️ How It Works

1. User enters an SMS message.
2. Machine learning model analyzes the message.
3. Rule-based detection checks suspicious indicators.
4. The application assigns an initial risk level.
5. Local Qwen AI generates an explanation.
6. The application displays results and safety advice.

## 📊 Model Performance

Dataset: UCI SMS Spam Collection

| Metric | Result |
|---|---:|
| Accuracy | 97.67% |
| Spam Precision | 90% |
| Spam Recall | 93% |
| Spam F1-score | 91% |

Evaluation was performed on a stratified held-out test split.

## 🖥️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd project-degrade
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

For AI explanations, start LM Studio, load a compatible Qwen model and enable its local server.

## 📁 Project Structure

```text
project-degrade/
│
├── app.py
├── detector.py
├── ai_explainer.py
├── train_model.py
├── evaluate_model.py
├── visualize_model.py
├── test_detector.py
├── requirements.txt
│
├── data/
├── models/
└── model_performance.png
```

## ⚠️ Limitations

- The training dataset is limited to the SMS Spam Collection.
- Model performance on this dataset does not guarantee real-world scam detection accuracy.
- Rule-based indicators may miss unfamiliar scam techniques.
- AI-generated explanations may contain errors.
- A low-risk result does not guarantee that a message is safe.

## 🚀 Future Improvements

- Support more Indian languages.
- Improve detection of modern phishing messages.
- Expand the training dataset.
- Add URL analysis.
- Improve model evaluation using external datasets.
- Deploy the application online.

## 👨‍💻 Project Status

Developed as a Machine Learning and AI portfolio project.
