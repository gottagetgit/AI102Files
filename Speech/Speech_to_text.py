import azure.cognitiveservices.speech as speechsdk

'''
In this exercise you will see an example of a speech to text translations from a local file.
'''

speech_key, service_region = "YourKey", "YourRegion"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

audio_input = speechsdk.AudioConfig(filename="C:\\Users\\Jordi\\PycharmProjects\\AI102Files\\Speech\\Media\\narration"
                                             ".wav")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
print("Recognizing first result...")

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

'''
In this exercise you will see an example of listening for speech from a microphone and translating it to text output.
'''

speech_key, service_region = "820f0a6b22524842acae9c5d176bd843", "westeurope"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Begin speaking...")

result = speech_recognizer.recognize_once()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
