import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def english_to_french(text):
    """This function does english to french translation"""

    authenticator = IAMAuthenticator(apikey)
    version = '2018-05-01'
    language_t = LanguageTranslatorV3(
        version=version, authenticator=authenticator)
    language_t.set_service_url(url)
    translation = language_t.translate(
        text=text, model_id="en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    if text == " ":
        return "Error: Enter a word"
    return french_text


def french_to_english(text):
    """This function does french to english translation"""
    authenticator = IAMAuthenticator(apikey)
    version = '2018-05-01'
    language_t = LanguageTranslatorV3(
        version=version, authenticator=authenticator)
    language_t.set_service_url(url)
    translation = language_t.translate(
        text=text, model_id="fr-en").get_result()
    english_text = translation['translations'][0]['translation']
    if text == " ":
        return "Error: Enter a word"
    return english_text


"""
print(english_to_french("this its a example"))
print(french_to_english("Comment allez vous?"))
print(english_to_french("Bonjour"))
print(french_to_english("Hello"))
"""
