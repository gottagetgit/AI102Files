from pip._vendor import requests
# pprint is used to format the JSON response
from pprint import pprint

# variables to store subscription key and root URL for the Cognitive Service resource
subscription_key = "YourKey"
endpoint = "YourEndpoint"

# append the Text Analytics endpoint information to the URL
entities_url = endpoint + "/text/analytics/v2.1/entities"

# variable to store a JSON formatted document that contains two entries in a JSON array.
documents = {"documents": [
    {"id": "1", "language": "en",
     "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell "
             "BASIC interpreters for the Altair 8800."},
    {"id": "2", "language": "es",
     "text": "La sede principal de Microsoft se encuentra en la ciudad de Redmond, a 21 kilómetros de "
             "Seattle."}
]}

# Setup the header information for the REST request passing in the subscription key
headers = {"Ocp-Apim-Subscription-Key": subscription_key}

# Build the REST request by passing in the complete URL, header information for authentication, and the JSON document
response = requests.post(entities_url, headers=headers, json=documents)

# Create a variable to store the results that are returned from the REST request
entities = response.json()

# Output the result using pprint.
pprint(entities)
