from groq import Groq
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)
def sentment_analysis_of_review(text):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Do sentiment analysis of the following text and give output in the form of JSON {\n       \"positive\": score,\n       \"negative\": score,\n       \"neutral\": score\n     }"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    return completion.choices[0].message.content
