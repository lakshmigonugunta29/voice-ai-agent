from langdetect import detect

def analyze_message(user_voice):

    user_voice = user_voice.lower()

    # Language Detection
    try:
        lang = detect(user_voice)

        if lang == "hi":
            language = "Hindi"

        elif lang == "ta":
            language = "Tamil"

        else:
            language = "English"

    except:
        language = "English"

    # Intent Detection
    if "book" in user_voice or "appointment" in user_voice:

        intent = "Book Appointment"

        status = "Appointment Confirmed"

        ai_response = "Your appointment has been booked successfully."

    elif "cancel" in user_voice:

        intent = "Cancel Appointment"

        status = "Appointment Cancelled"

        ai_response = "Your appointment has been cancelled successfully."

    elif "reschedule" in user_voice:

        intent = "Reschedule Appointment"

        status = "Appointment Rescheduled"

        ai_response = "Your appointment has been rescheduled."

    else:

        intent = "General Conversation"

        status = "No Appointment Action"

        ai_response = "Sorry, I could not understand."

    return {
        "language": language,
        "intent": intent,
        "status": status,
        "ai_response": ai_response
    }