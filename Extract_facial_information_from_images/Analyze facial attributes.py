import requests
import matplotlib.pyplot as plt
import simplejson
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os
import simplejson as json

def config():
    print("Call Config")
    return subscription_key, face_api_url

image_path = os.path.join(r'C:\Users\Jordi\PycharmProjects\AI102Files\Extract_facial_information_from_images\CapFrame.jpg')
image_data = open(image_path, "rb")

subscription_key = "7a27910ff6d04cb9bedb85cfbdacb184"
face_api_url = 'https://azcogsvc.cognitiveservices.azure.com/face/v1.0/detect'

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