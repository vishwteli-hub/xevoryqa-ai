
import os
import requests
import time

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key missing.")
    raise SystemExit

model = "gemini-flash-lite-latest"

url = (
    f"https://generativelanguage.googleapis.com/"
    f"v1beta/models/{model}:generateContent"
)

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Reply with exactly: Gemini works."
                }
            ]
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 30,
        "temperature": 0.2
    }
}

try:
    print(f"Testing model: {model}", flush=True)

    start = time.time()

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=(10, 60)
    )

    print("HTTP Status:", response.status_code)
    print("Response time:", round(time.time() - start, 2), "seconds")

    if response.status_code == 200:
        data = response.json()
        answer = data["candidates"][0]["content"]["parts"][0]["text"]

        print("\nSUCCESS!")
        print("Gemini response:", answer)

    else:
        print("\nAPI ERROR:")
        print(response.text)

except requests.exceptions.Timeout:
    print("ERROR: Request timed out.")

except requests.exceptions.ConnectionError as error:
    print("ERROR: Connection failed:", error)

except Exception as error:
    print("ERROR:", type(error).__name__, error)
