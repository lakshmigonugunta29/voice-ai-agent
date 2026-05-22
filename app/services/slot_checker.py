# backend/app/services/slot_checker.py

available_slots = {

    "dr_smith": [
        "10:00 AM",
        "11:00 AM",
        "2:00 PM"
    ],

    "dr_kumar": [
        "9:00 AM",
        "1:00 PM",
        "4:00 PM"
    ],

    "dr_rajesh": [
        "8:00 AM",
        "12:00 PM",
        "5:00 PM"
    ]
}


booked_slots = []


# -----------------------------------
# CHECK SLOT
# -----------------------------------

def check_slot(doctor, time_slot):

    doctor = doctor.lower()

    # doctor exists or not
    if doctor not in available_slots:

        return {
            "available": False,
            "message": "Doctor not found"
        }

    # slot exists or not
    if time_slot not in available_slots[doctor]:

        return {
            "available": False,
            "message": "Requested slot not available"
        }

    # already booked or not
    for booking in booked_slots:

        if (
            booking["doctor"] == doctor
            and booking["time_slot"] == time_slot
        ):

            return {
                "available": False,
                "message": "Slot already booked",
                "alternative_slots": get_available_slots(doctor)["available_slots"]
            }

    return {
        "available": True,
        "message": "Slot available"
    }


# -----------------------------------
# BOOK SLOT
# -----------------------------------

def book_slot(user, doctor, time_slot):

    slot_result = check_slot(doctor, time_slot)

    # booking failed
    if slot_result["available"] is False:

        return {
            "status": "failed",
            "message": slot_result["message"],
            "alternative_slots": slot_result.get(
                "alternative_slots",
                []
            )
        }

    # booking success
    booking = {
        "user": user,
        "doctor": doctor,
        "time_slot": time_slot
    }

    booked_slots.append(booking)

    return {
        "status": "success",
        "message": "Appointment booked successfully",
        "booking": booking
    }


# -----------------------------------
# CANCEL BOOKING
# -----------------------------------

def cancel_booking(user, doctor, time_slot):

    for booking in booked_slots:

        if (
            booking["user"] == user
            and booking["doctor"] == doctor
            and booking["time_slot"] == time_slot
        ):

            booked_slots.remove(booking)

            return {
                "status": "success",
                "message": "Appointment cancelled successfully"
            }

    return {
        "status": "failed",
        "message": "Booking not found"
    }


# -----------------------------------
# GET AVAILABLE SLOTS
# -----------------------------------

def get_available_slots(doctor):

    doctor = doctor.lower()

    if doctor not in available_slots:

        return {
            "status": "failed",
            "message": "Doctor not found"
        }

    free_slots = []

    for slot in available_slots[doctor]:

        booked = False

        for booking in booked_slots:

            if (
                booking["doctor"] == doctor
                and booking["time_slot"] == slot
            ):

                booked = True

        if booked is False:

            free_slots.append(slot)

    return {
        "status": "success",
        "doctor": doctor,
        "available_slots": free_slots
    }


# -----------------------------------
# GET ALL BOOKINGS
# -----------------------------------

def get_all_bookings():

    return {
        "total_bookings": len(booked_slots),
        "bookings": booked_slots
    }