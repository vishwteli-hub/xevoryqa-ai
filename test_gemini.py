
import os
import time
from google import genai

print("STEP 1: Checking API key...", flush=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key is missing.")
    raise SystemExit

print("STEP 2: API key found.", flush=True)

print("STEP 3: Connecting to Gemini...", flush=True)

try:
    client = genai.Client(
        api_key=api_key,
        http_options={"timeout": 120000}
    )

    print("STEP 4: Sending test request...", flush=True)

    start_time = time.time()

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input="Reply with exactly: Gemini connection works."
    )

    elapsed = time.time() - start_time

    print("\nSUCCESS!", flush=True)
    print("Gemini response:", response.output_text, flush=True)
    print(f"Response time: {elapsed:.2f} seconds", flush=True)

except Exception as error:
    print("\nGEMINI ERROR:", flush=True)
    print(type(error).__name__, flush=True)
    print(str(error), flush=True)
