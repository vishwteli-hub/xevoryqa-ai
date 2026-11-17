
from ai_explainer import explain_message

print("Testing ScamShield AI Gemini integration...\n")

result = explain_message(
    message="URGENT! Your bank account will be blocked. Share your OTP immediately to verify your account.",
    prediction="spam",
    spam_probability=0.98,
    indicators=[
        "Urgent or threatening language",
        "Requests sensitive information"
    ],
    risk_level="High Risk"
)

print("GEMINI RESULT:\n")
print(result)
