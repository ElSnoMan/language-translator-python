"""
Python Google Translate API Docs:
    https://py-googletrans.readthedocs.io/en/latest/

Supported Languages
    https://cloud.google.com/translate/docs/languages
"""
from googletrans import Translator


text = '''  Pour souvent, quand sur mon canapé je mens
D'humeur vacante ou songeuse,
Ils clignotent sur cet œil intérieur
Quel est le bonheur de la solitude;
Et puis mon cœur se remplit de plaisir,
Et danse avec les jonquilles. '''


translator = Translator()
lang = translator.detect(text)
print(lang)  # Detected(lang=fr, confidence=0.9857986)


res = translator.translate(text, dest='en')
print(res)
