from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    """This function does english to french translation"""
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.english_to_french(textToTranslate)
    return translatedText


@app.route("/frenchToEnglish")
def frenchToEnglish():
    """This function does french to english translation"""
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.french_to_english(textToTranslate)
    return translatedText


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
