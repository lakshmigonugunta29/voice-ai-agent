from app.database.models import appointments

def save_appointment(data):

    appointments.append(data)

    return data

def get_appointments():

    return appointments