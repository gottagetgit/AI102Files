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
Recognize Printed Text with OCR - local
This example will extract, using OCR, printed text in an image, then print results line by line.
'''
print("===== Detect Printed Text with OCR - local =====")
print()
# Get an image with printed text
local_image_printed_text_path = "Images/printed_text.jpg"
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
print()
remote_printed_text_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files" \
                                "/master/ComputerVision/Images/printed_text.jpg "

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

'''
Batch Read File, recognize handwritten text - remote
This example will extract handwritten text in an image, then print results, line by line.
This API call can also recognize handwriting (not shown).
'''
print()
print("===== Detect Printed Text with the Read API - remote =====")
print()
# Get an image with handwritten text
remote_image_handw_text_url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive" \
                              "-services/Computer-vision/Images/readsample.jpg "

# Call API with URL and raw response (allows you to get the operation location)
recognize_handw_results = computervision_client.read(remote_image_handw_text_url,  raw=True)

# Get the operation location (URL with an ID at the end) from the response
operation_location_remote = recognize_handw_results.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = operation_location_remote.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results
while True:
    get_handw_text_results = computervision_client.get_read_result(operation_id)
    if get_handw_text_results.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if get_handw_text_results.status == OperationStatusCodes.succeeded:
    for text_result in get_handw_text_results.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)

'''
END - Detect Printed Text with the Read API - remote
'''