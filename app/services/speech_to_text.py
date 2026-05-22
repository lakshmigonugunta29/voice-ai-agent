import speech_recognition as sr

def convert_voice_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Speak now...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("User Said:", text)

        return text

    except sr.UnknownValueError:

        return "Could not understand audio"

    except sr.RequestError:

        return "Speech service unavailable"