import json
import os

from dotenv import load_dotenv
import requests

load_dotenv()

LANGUAGE_KEY = os.getenv("LANGUAGE_KEY")
LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")

payload = {
	"kind": "SentimentAnalysis",
	"parameters": {
		"modelVersion": "latest"
	},
	"analysisInput":{
		"documents":[
			{
				"id":"1",
				"language":"en",
				"text": "The sun shone brightly, making the park a perfect place for a picnic."
			},
            {
				"id":"2",
				"language":"en",
				"text": "The traffic was unbearable, causing everyone to arrive late to the event."
			}
		]
	}
}

response = requests.post(
    f"{LANGUAGE_ENDPOINT}/language/:analyze-text?api-version=2023-04-15-preview",
    json=payload,
    headers={
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": LANGUAGE_KEY
    }
)

print(json.dumps(response.json(), indent=2))