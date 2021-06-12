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
Detect Brands - remote
This example detects common brands like logos and puts a bounding box around them.
'''
print("===== Detect Brands - remote =====")
# Get a URL with a brand logo
remote_image_url = "https://raw.githubusercontent.com/gottagetgit/AI102Files/main/Computer_Vision" \
                   "/Analyze_images_using_Computer_Vision_API/Images/gray-shirt-logo.jpg "
# Select the visual feature(s) you want
remote_image_features = ["brands"]
# Call API with URL and features
detect_brands_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)

print("Detecting brands in remote image: \n")
if len(detect_brands_results_remote.brands) == 0:
    print("No brands detected.")
else:
    for brand in detect_brands_results_remote.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format(
            brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w,
            brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))
print()
'''
Detect Brands - local
This example detects common brands like logos and puts a bounding box around them.
'''
print("===== Detect Brands - local =====")
# Open image file
local_image_path_shirt = "Images/gray-shirt-logo.jpg"
local_image_shirt = open(local_image_path_shirt, "rb")
# Select the visual feature(s) you want
local_image_features = ["brands"]
# Call API with image and features
detect_brands_results_local = computervision_client.analyze_image_in_stream(local_image_shirt, local_image_features)

# Print detection results with bounding box and confidence score
print("Detecting brands in local image: \n")
if len(detect_brands_results_local.brands) == 0:
    print("No brands detected.")
else:
    for brand in detect_brands_results_local.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format(
            brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w,
            brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))
print()
'''
END - Detect brands - local
'''