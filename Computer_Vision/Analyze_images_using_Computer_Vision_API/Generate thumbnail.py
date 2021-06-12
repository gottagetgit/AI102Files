from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "<enter your key here>"
endpoint = "<enter your endpoint URL here>"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Generate Thumbnail
This example creates a thumbnail from both a local and URL image.
'''
print("===== Generate Thumbnails - local =====")

# Generate a thumbnail from a local image
local_image_path_thumb = "Images/Faces.jpg"
local_image_thumb = open(local_image_path_thumb, "rb")

print("Generating thumbnail from a local image...")
# Call the API with a local image, set the width/height if desired (pixels)
# Returns a Generator object, a thumbnail image binary (list).
thumb_local = computervision_client.generate_thumbnail_in_stream(100, 100, local_image_thumb, True)

# Write the image binary to file
with open("thumb_local.png", "wb") as f:
    for chunk in thumb_local:
        f.write(chunk)

# Uncomment/use this if you are writing many images as thumbnails from a list
# for i, image in enumerate(thumb_local, start=0):
#      with open('thumb_{0}.jpg'.format(i), 'wb') as f:
#         f.write(image)

print("Thumbnail saved to local folder.")
print()
print("===== Generate Thumbnails - remote =====")
# Generate a thumbnail from a URL image
# URL of faces
remote_image_url_thumb = "https://raw.githubusercontent.com/gottagetgit/AI102Files/main/Computer_Vision" \
                         "/Analyze_images_using_Computer_Vision_API/Images/Faces.jpg "

print("Generating thumbnail from a URL image...")
# Returns a Generator object, a thumbnail image binary (list).
thumb_remote = computervision_client.generate_thumbnail(
    100, 100, remote_image_url_thumb, True)

# Write the image binary to file
with open("thumb_remote.png", "wb") as f:
    for chunk in thumb_remote:
        f.write(chunk)

print("Thumbnail saved to local folder.")

# Uncomment/use this if you are writing many images as thumbnails from a list
# for i, image in enumerate(thumb_remote, start=0):
#      with open('thumb_{0}.jpg'.format(i), 'wb') as f:
#         f.write(image)

'''
END - Generate Thumbnail
'''