import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "YourKey", "YourRegion"


def translate_speech_to_speech():
    # Creates an instance of a speech translation config with specified subscription key and service region.
    # Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a speech synthesizer using the configured voice for audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Sets source and target languages. In this example, the service will translate a US English spoken input,
    # to French and Indonesian language spoken output Replace with the languages of your choice, from list found
    # here: https://aka.ms/speech/sttt-languages
    fromLanguage = 'en-US'
    translation_config.speech_recognition_language = fromLanguage

    # Add more than one language to the collection.
    # using the add_target_language() method
    translation_config.add_target_language("fr")
    translation_config.add_target_language("id-ID")

    # Creates a translation recognizer using and audio file as input.
    recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)

    # Starts translation, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognized text as well as the translation.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    print("Say something...")
    result = recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        # Output the text for the recognized speech input
        print("RECOGNIZED '{}': {}".format(fromLanguage, result.text))

        # Loop through the returned translation results
        for key in result.translations:

            # Using the Key and Value components of the returned dictionary for the translated results
            # The first portion gets the key (language code) while the second gets the Value
            # which is the translated text for the language specified
            # Output the language and then the translated text
            print("TRANSLATED into {}: {}".format(key, result.translations[key]))

            # If the language code is 'fr' for French, then use the French voice for Julie
            # If you change the languages in the 'AddTargetLanguage' above, ensure you modify this if statement as well
            if key == "fr":
                speech_config.speech_synthesis_voice_name = "fr-FR-Julie-Apollo"

                # Update the speech synthesizer to use the proper voice
                speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

                # Use the proper voice, from the speech synthesizer configuration, to narrate the translated result
                # in the native speaker voice.
                speech_synthesizer.speak_text_async(result.translations[key]).get()
            else:  # Otherwise, use the voice for the Indonesian translation
                speech_config.speech_synthesis_voice_name = "id-ID-Andika"

                # Update the speech synthesizer to use the proper voice
                speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

                # Use the proper voice, from the speech synthesizer configuration, to narrate the translated result
                # in the native speaker voice.
                speech_synthesizer.speak_text_async(result.translations[key]).get()

    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("RECOGNIZED: {} (text could not be translated)".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("NOMATCH: Speech could not be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("CANCELED: Reason={}".format(result.cancellation_details.reason))
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("CANCELED: ErrorDetails={}".format(result.cancellation_details.error_details))


translate_speech_to_speech()
