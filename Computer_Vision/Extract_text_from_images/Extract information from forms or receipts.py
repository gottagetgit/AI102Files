import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

key = "<enter your key here>"
endpoint = "<enter your endpoint URL here>"

form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

formUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai" \
          "-formrecognizer/tests/sample_forms/forms/Form_1.jpg "

print("--------Recognizing form--------")

poller = form_recognizer_client.begin_recognize_content_from_url(formUrl)
page = poller.result()

table = page[0].tables[0]  # page 1, table 1
print("Table found on page {}:".format(table.page_number))
for cell in table.cells:
    print("Cell text: {}".format(cell.text))
    print("Location: {}".format(cell.bounding_box))
    print("Confidence score: {}\n".format(cell.confidence))

receiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai" \
             "-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png "

print("--------Recognizing receipt--------")
poller = form_recognizer_client.begin_recognize_receipts_from_url(receiptUrl)
result = poller.result()

for receipt in result:
    for name, field in receipt.fields.items():
        if name == "Items":
            print()
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print()
                print("...Item #{}".format(idx + 1))
                for item_name, item in items.value.items():
                    print("......{}: {} has confidence {}".format(item_name, item.value, item.confidence))
        else:
            print()
            print("{}: {} has confidence {}".format(name, field.value, field.confidence))
