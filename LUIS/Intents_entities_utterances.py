from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from msrest.authentication import CognitiveServicesCredentials

import datetime, json, os, time

authoring_key = 'YourAuthoringKey'
authoring_endpoint = 'YourAuthoringEndpoint'

# Instantiate a LUIS client
client = LUISAuthoringClient(authoring_endpoint, CognitiveServicesCredentials(authoring_key))


def create_app():
    # Create a new LUIS app
    app_name = "PictureBotLUIS"
    app_desc = "Picture Bot app built with LUIS Python SDK."
    app_version = "0.1"
    app_locale = "en-us"

    app_id = client.apps.add(dict(name=app_name,
                                  initial_version_id=app_version,
                                  description=app_desc,
                                  culture=app_locale))

    print("Created LUIS app {}\n    with ID {}".format(app_name, app_id))
    add_intents(app_id, app_version)
    add_entities(app_id, app_version)
    return app_id, app_version


def add_intents(app_id, app_version):
    intents = ["Greeting", "SearchPics", "OrderPic", "SharePic"]
    for intent in intents:
        intentId = client.model.add_intent(app_id, app_version, intent)
        print("Intent {} {} added.".format(intent, intentId))


def add_entities(app_id, app_version):
    facetEntityId = client.model.add_entity(app_id, app_version, name="facet")
    print("facetEntityId {} added.".format(facetEntityId))


# Helper function for creating the utterance data structure.
def create_utterance(intent, utterance, *labels):
    text = utterance.lower()

    def label(name, value):
        value = value.lower()
        start = text.index(value)
        return dict(entity_name=name, start_char_index=start,
                    end_char_index=start + len(value))

    return dict(text=text, intent_name=intent,
                entity_labels=[label(n, v) for (n, v) in labels])


def add_utterances(app_id, app_version):
    # Now define the utterances
    utterances = [create_utterance("SearchPic", "find outdoor pics",
                                   ("facet", "outdoor")),

                  create_utterance("SearchPic", "are there pictures of a train?",
                                   ("facet", "train")),

                  create_utterance("SearchPic", "find pictures of food",
                                   ("facet", "food")),

                  create_utterance("SearchPic", "search for photos of boys playing",
                                   ("facet", "boys playing")),

                  create_utterance("SearchPic", "give me colorful pictures",
                                   ("facet", "colorful")),

                  create_utterance("SearchPic", "show me beach pics",
                                   ("facet", "beach")),

                  create_utterance("SearchPic", "I want to find dog photos",
                                   ("facet", "dog")),

                  create_utterance("SearchPic", "find pictures of German shepherds",
                                   ("facet", "German shepherds")),

                  create_utterance("SearchPic", "search for pictures of men indoors",
                                   ("facet", "men indoors")),

                  create_utterance("SearchPic", "show me pictures of men wearing glasses",
                                   ("facet", "men wearing glasses")),

                  create_utterance("SearchPic", "I want to see pics of smiling people",
                                   ("facet", "smiling people")),

                  create_utterance("SearchPic", "show me baby pics",
                                   ("facet", "baby"))]

    # Add the utterances in batch. You may add any number of example utterances
    # for any number of intents in one call.
    client.examples.batch(app_id, app_version, utterances)
    print("{} example utterance(s) added.".format(len(utterances)))


create_app()
