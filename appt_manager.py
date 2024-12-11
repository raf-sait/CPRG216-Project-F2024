'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project
Course: CPRG 216-B
Date: 12/12/2024
'''





print('1) Schedule an appointment')
print('2) Find appointment by name')
print('3) Print calendar for a specific day')
print('4) Cancel an appointment')
print('5) Change an appointment')
print('6) Calculate total fees for a day')
print('7) Calculate total fees for a day')
print('9) Exit the system')

class Appointment:

    def __init__(self, client_name = 0, client_phone = 0, appt_type = 0, day_of_week, start_time_hour):
        self.__client_name = client_name #Appointment property
        self.__client_phone = client_phone #Appointment property
        self.__appt_type = appt_type #Appointment property
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    #def get client_name
    #def get client_phone
    #def get appt_type
    #def get_appt_type_desc()
    #def get_end_time_hour()
    #def set client_name
    #def set client_phone
    #def set appt_type
    #def schedule()
    #def cancel()
    #def format_record()
    #def __str__()