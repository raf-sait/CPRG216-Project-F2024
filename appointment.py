'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project (Appointment Class)
Course: CPRG 216-B
Date: 12/12/2024
'''

class Appointment:

    def __init__(self, client_name = 0, client_phone = 0, appt_type = 0, day_of_week, start_time_hour):
        self.__client_name = client_name #Appointment property
        self.__client_phone = client_phone #Appointment property
        self.__appt_type = appt_type #Appointment property
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name


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