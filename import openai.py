import openai

openai.api_key = "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"

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Say hello.",
        max_tokens=10
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"API Test Error: {e}")
