import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os
import json


def config():
    print("Call Config")
    return subscription_key, face_api_url


image_path = os.path.join(r'/Computer_Vision/Extract_facial_information_from_images/CapFrame.jpg')
image_data = open(image_path, "rb")

subscription_key = "<enter your key>"
face_api_url = "<place the API URL here>"

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()
print(faces)
with open("faces.json", "w") as faces_file:
    json.dump(faces, faces_file, indent=4, sort_keys=True)
