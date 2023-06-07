from deep_translator import MyMemoryTranslator #Import deep_translator


#Function to translate english text to french
def english_to_french(english_text):
    french_text = MyMemoryTranslator(
        source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

english_to_french('Hello')

#Function to translate french text to english
def french_to_english(french_text):
    english_text = MyMemoryTranslator(
        source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text


french_to_english('Bonjour')
