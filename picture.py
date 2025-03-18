# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI
import json
import webbrowser

# credential = DefaultAzureCredential()
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "<your-api-key>")

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://<your-endpoint-api>.openai.azure.com/",
    api_key=subscription_key
)

result = client.images.generate(
    model="dall-e-3", # the name of your DALL-E 3 deployment
    prompt="A couple driving on a Vespa scooter in Pixar style with white background",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url )

# open a browser to view the image
webbrowser.open(image_url)

