from fastapi import APIRouter
import time

from app.services.language_detector import detect_language
from app.services.slot_checker import (
    check_slot,
    book_slot,
    get_available_slots
)

from app.memory.redis_memory import (
    save_memory,
    get_memory
)

router = APIRouter()


@router.get("/voice")
def voice_ai(message: str):

    # -----------------------------
    # START LATENCY TIMER
    # -----------------------------
    start = time.time()

    user = "mahesh"

    # -----------------------------
    # LANGUAGE DETECTION
    # -----------------------------
    language = detect_language(message)

    # -----------------------------
    # INTENT DETECTION
    # -----------------------------
    # -----------------------------

    if (
       "book" in message.lower()
        or "appointment" in message.lower()
        or "बुक" in message
        or "பதிவு" in message
    ):

        intent = "book_appointment"

    elif (
        "cancel" in message.lower()
         or "रद्द" in message
    ):

         intent = "cancel_appointment"

    else:

         intent = "general_query"

    # -----------------------------
    # DOCTOR + SLOT
    # -----------------------------
    doctor = "dr_smith"
    slot = "10:00 AM"

    # -----------------------------
    # SLOT CHECK
    # -----------------------------
    slot_result = check_slot(doctor, slot)

    # -----------------------------
    # BOOK APPOINTMENT
    # -----------------------------
    if slot_result["available"]:

        booking = book_slot(
            user,
            doctor,
            slot
        )

        status = "success"

    else:

        booking = {
            "message": slot_result["message"]
        }

        status = "failed"

    # -----------------------------
    # SAVE MEMORY
    # -----------------------------
    save_memory(
        user,
        {
            "language": language,
            "message": message,
            "intent": intent,
            "doctor": doctor,
            "slot": slot,
            "status": status
        }
    )

    # -----------------------------
    # GET MEMORY
    # -----------------------------
    memory = get_memory(user)

    # -----------------------------
    # MULTILINGUAL RESPONSE
    # -----------------------------
    if language == "hi":

        response_message = "आपकी appointment सफलतापूर्वक बुक हो गई"

    elif language == "ta":

        response_message = "உங்கள் appointment வெற்றிகரமாக பதிவு செய்யப்பட்டது"

    else:

        response_message = "Your appointment booked successfully"

    # -----------------------------
    # LATENCY END
    # -----------------------------
    end = time.time()

    latency = round((end - start) * 1000, 2)

    # -----------------------------
    # FINAL RESPONSE
    # -----------------------------
    return {

        "user_message": message,

        "language": language,

        "intent": intent,

        "doctor": doctor,

        "slot": slot,

        "booking_status": status,

        "response_message": response_message,

        "booking_details": booking,

        "memory": memory,

        "latency_ms": latency
    }