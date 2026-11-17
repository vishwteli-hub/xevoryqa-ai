
import joblib
import re

# Load trained machine-learning model
model = joblib.load("models/scam_detector.pkl")


def analyze_message(message):
    if not message or not message.strip():
        raise ValueError("Please enter a message.")

    # ML prediction
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]

    spam_index = list(model.classes_).index("spam")
    spam_probability = float(probabilities[spam_index])

    # Detect suspicious patterns
    indicators = []

    patterns = {
        "Urgent or threatening language": (
            r"\b(urgent|immediately|suspended|blocked|"
            r"expire|act now|today)\b"
        ),
        "Requests sensitive information": (
            r"\b(share|send|provide|enter|confirm|verify)\b"
            r".{0,40}\b(password|otp|pin|cvv|bank details|"
            r"account number)\b"
        ),
        "Prize or reward claims": (
            r"\b(winner|won|prize|lottery|free gift|claim reward)\b"
        ),
        "Suspicious links": r"https?://|www\."
    }

    for description, pattern in patterns.items():
        if re.search(pattern, message, re.IGNORECASE):
            indicators.append(description)

    # Combined risk assessment
    if "Requests sensitive information" in indicators:
        risk_level = "High Risk"

    elif len(indicators) >= 2:
        risk_level = "Potential Risk"

    elif prediction == "spam":
        risk_level = "Potential Risk"

    else:
        risk_level = "Low Risk"

    return {
        "prediction": prediction,
        "spam_probability": spam_probability,
        "indicators": indicators,
        "risk_level": risk_level
    }
