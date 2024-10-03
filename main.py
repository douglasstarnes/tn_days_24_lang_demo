import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

LANGUAGE_KEY = os.getenv("LANGUAGE_KEY")
LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")

credential = AzureKeyCredential(LANGUAGE_KEY)
client = TextAnalyticsClient(
    endpoint=LANGUAGE_ENDPOINT,
    credential=credential
)

documents = [
    "The sun shone brightly, making the park a perfect place for a picnic.", # positive
    "The traffic was unbearable, causing everyone to arrive late to the event.", # negative
    "The meeting was scheduled for 10 AM and lasted about an hour.", # neutral
    "She opened the door to find a surprise party waiting for her, but she wasn’t sure if she was excited or overwhelmed." # ambiguous
]

results = client.analyze_sentiment(documents)
for idx, document in enumerate(results):
    print(f"{idx + 1}) {'-' * 40}")
    print(f"  {' '.join([sentence.text for sentence in document.sentences])}")
    print(f"  Overall sentiment: {document.sentiment}")
    print(f"  Confidence scores:")
    print(f"    positive: {document.confidence_scores.positive}")
    print(f"    negative: {document.confidence_scores.negative}")
    print(f"    neutral: {document.confidence_scores.neutral}")