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

remote_image_url = "https://raw.githubusercontent.com/gottagetgit/AI102Files/main/Computer_Vision" \
                   "/Analyze_images_using_Computer_Vision_API/Images/Landmark.jpg "

'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an image - remote =====")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

# Print results with confidence score
print("Tags in the remote image: \n")
if len(tags_result_remote.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
Tag an Image - local
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an Image - local =====")
# Open local image file
local_image_path = "Images/Landmark.jpg"
local_image = open(local_image_path, "rb")
# Call API local image
tags_result_local = computervision_client.tag_image_in_stream(local_image)

# Print results with confidence score
print("Tags in the local image: \n")
if len(tags_result_local.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
END - Tag an Image - local
'''