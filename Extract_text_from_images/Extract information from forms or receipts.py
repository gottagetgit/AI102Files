import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://azcogsvc.cognitiveservices.azure.com/"
key = "7a27910ff6d04cb9bedb85cfbdacb184"

form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

receiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

print("--------Recognizing receipt--------")

poller = form_recognizer_client.begin_recognize_receipts_from_url(receiptUrl)
result = poller.result()

for receipt in result:
    for name, field in receipt.fields.items():
        if name == "Items":
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print("...Item #{}".format(idx + 1))
                for item_name, item in items.value.items():
                    print("......{}: {} has confidence {}".format(item_name, item.value, item.confidence))
        else:
            print("{}: {} has confidence {}".format(name, field.value, field.confidence))

bcUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/samples/sample_forms/business_cards/business-card-english.jpg"

poller = form_recognizer_client.begin_recognize_business_cards_from_url(bcUrl)
business_cards = poller.result()
print()

for idx, business_card in enumerate(business_cards):
    print("--------Recognizing business card #{}--------".format(idx+1))
    contact_names = business_card.fields.get("ContactNames")
    if contact_names:
        for contact_name in contact_names.value:
            print("Contact First Name: {} has confidence: {}".format(
                contact_name.value["FirstName"].value, contact_name.value["FirstName"].confidence
            ))
            print("Contact Last Name: {} has confidence: {}".format(
                contact_name.value["LastName"].value, contact_name.value["LastName"].confidence
            ))
    company_names = business_card.fields.get("CompanyNames")
    if company_names:
        for company_name in company_names.value:
            print("Company Name: {} has confidence: {}".format(company_name.value, company_name.confidence))
    departments = business_card.fields.get("Departments")
    if departments:
        for department in departments.value:
            print("Department: {} has confidence: {}".format(department.value, department.confidence))
    job_titles = business_card.fields.get("JobTitles")
    if job_titles:
        for job_title in job_titles.value:
            print("Job Title: {} has confidence: {}".format(job_title.value, job_title.confidence))
    emails = business_card.fields.get("Emails")
    if emails:
        for email in emails.value:
            print("Email: {} has confidence: {}".format(email.value, email.confidence))
    websites = business_card.fields.get("Websites")
    if websites:
        for website in websites.value:
            print("Website: {} has confidence: {}".format(website.value, website.confidence))
    addresses = business_card.fields.get("Addresses")
    if addresses:
        for address in addresses.value:
            print("Address: {} has confidence: {}".format(address.value, address.confidence))
    mobile_phones = business_card.fields.get("MobilePhones")
    if mobile_phones:
        for phone in mobile_phones.value:
            print("Mobile phone number: {} has confidence: {}".format(phone.value, phone.confidence))
    faxes = business_card.fields.get("Faxes")
    if faxes:
        for fax in faxes.value:
            print("Fax number: {} has confidence: {}".format(fax.value, fax.confidence))
    work_phones = business_card.fields.get("WorkPhones")
    if work_phones:
        for work_phone in work_phones.value:
            print("Work phone number: {} has confidence: {}".format(work_phone.value, work_phone.confidence))
    other_phones = business_card.fields.get("OtherPhones")
    if other_phones:
        for other_phone in other_phones.value:
            print("Other phone number: {} has confidence: {}".format(other_phone.value, other_phone.confidence))
print()

invoiceUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/simple-invoice.png"

poller = form_recognizer_client.begin_recognize_invoices_from_url(invoiceUrl)
invoices = poller.result()

for idx, invoice in enumerate(invoices):
    print("--------Recognizing invoice #{}--------".format(idx+1))
    vendor_name = invoice.fields.get("VendorName")
    if vendor_name:
        print("Vendor Name: {} has confidence: {}".format(vendor_name.value, vendor_name.confidence))
    vendor_address = invoice.fields.get("VendorAddress")
    if vendor_address:
        print("Vendor Address: {} has confidence: {}".format(vendor_address.value, vendor_address.confidence))
    customer_name = invoice.fields.get("CustomerName")
    if customer_name:
        print("Customer Name: {} has confidence: {}".format(customer_name.value, customer_name.confidence))
    customer_address = invoice.fields.get("CustomerAddress")
    if customer_address:
        print("Customer Address: {} has confidence: {}".format(customer_address.value, customer_address.confidence))
    customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
    if customer_address_recipient:
        print("Customer Address Recipient: {} has confidence: {}".format(customer_address_recipient.value, customer_address_recipient.confidence))
    invoice_id = invoice.fields.get("InvoiceId")
    if invoice_id:
        print("Invoice Id: {} has confidence: {}".format(invoice_id.value, invoice_id.confidence))
    invoice_date = invoice.fields.get("InvoiceDate")
    if invoice_date:
        print("Invoice Date: {} has confidence: {}".format(invoice_date.value, invoice_date.confidence))
    invoice_total = invoice.fields.get("InvoiceTotal")
    if invoice_total:
        print("Invoice Total: {} has confidence: {}".format(invoice_total.value, invoice_total.confidence))
    due_date = invoice.fields.get("DueDate")
    if due_date:
        print("Due Date: {} has confidence: {}".format(due_date.value, due_date.confidence))