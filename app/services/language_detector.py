from langdetect import detect

def detect_language(text):

    try:

        lang = detect(text)

        if lang == "en":
            return "English"

        elif lang == "hi":
            return "Hindi"

        elif lang == "ta":
            return "Tamil"

        else:
            return "Unknown"

    except:

        return "Unknown"