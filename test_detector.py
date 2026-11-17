
from detector import analyze_message

# Test messages and their expected risk levels
test_cases = [
    (
        "Hey, are we meeting tomorrow at 10 AM?",
        "Low Risk"
    ),
    (
        "Your bank account will be blocked. Share your OTP immediately.",
        "High Risk"
    ),
    (
        "Congratulations! You are a winner. Click here to claim your prize.",
        "Potential Risk"
    ),
    (
        "Your package delivery failed. Track it at http://example.com",
        "Potential Risk"
    ),
    (
        "Your account statement is ready. Thank you for banking with us.",
        "Low Risk"
    )
]

passed = 0
failed = 0

print("\n========== SCAMSHIELD TEST REPORT ==========\n")

for number, (message, expected) in enumerate(test_cases, start=1):

    result = analyze_message(message)
    actual = result["risk_level"]

    if actual == expected:
        print(f"TEST {number}: PASS")
        passed += 1
    else:
        print(f"TEST {number}: FAIL")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")

    print(f"Message: {message}")
    print(f"Risk: {actual}")
    print("-" * 45)

print("\n========== FINAL RESULTS ==========")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total: {len(test_cases)}")

if failed == 0:
    print("\nAll automated tests passed!")
else:
    print("\nSome tests failed. Review the detector.")
