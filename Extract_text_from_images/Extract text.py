from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "46bd0636d83f4829ac745ff2c9ee2195"
endpoint = "https://azcogsvc.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Recognize Printed Text with OCR - local
This example will extract, using OCR, printed text in an image, then print results line by line.
'''
print("===== Detect Printed Text with OCR - local =====")
# Get an image with printed text
local_image_printed_text_path = "Images\\printed_text.jpg"
local_image_printed_text = open(local_image_printed_text_path, "rb")

ocr_result_local = computervision_client.recognize_printed_text_in_stream(local_image_printed_text)
for region in ocr_result_local.regions:
    for line in region.lines:
        print("Bounding box: {}".format(line.bounding_box))
        s = ""
        for word in line.words:
            s += word.text + " "
        print(s)
'''
END - Recognize Printed Text with OCR - local
'''
print()
'''
Recognize Printed Text with OCR - remote
This example will extract, using OCR, printed text in an image, then print results line by line.
'''
print("===== Detect Printed Text with OCR - remote =====")
remote_printed_text_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"

ocr_result_remote = computervision_client.recognize_printed_text(remote_printed_text_image_url)
for region in ocr_result_remote.regions:
    for line in region.lines:
        print("Bounding box: {}".format(line.bounding_box))
        s = ""
        for word in line.words:
            s += word.text + " "
        print(s)

'''
END - Recognize Printed Text with OCR - remote
'''