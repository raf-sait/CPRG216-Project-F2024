'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project (Appointment Class)
Course: CPRG 216-B
Date: 12/12/2024
'''

class Appointment:

    def __init__(self, day_of_week, start_time_hour, client_name = 0, client_phone = 0, appt_type = 0):
        self.__client_name = client_name #Appointment property
        self.__client_phone = client_phone #Appointment property
        self.__appt_type = appt_type #Appointment property
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self): 
        return self.__appt_type

    def get_day_of_week(self): 
        return self.__day_of_week

    def get_start_time_hour(self): 
        return self.__start_time_hour

    def get_appt_type_desc(self):
        appt_num = input("Please enter your appointment type from the following options for a description (0,1,2,3,4,): ")
        if appt_num == 0:
            print("Available")
        elif appt_num == 1:
            print("Mens Cut")
        elif appt_num == 2:
            print("Ladies Cut")
        elif appt_num == 3:
            print("Mens Colouring")
        elif appt_num == 4:
            print("Ladies Colouring")
        else:
            print("Not a valid input")
        
    def get_end_time_hour(self):
        return self.__start_time_hour + 1  
    
    def set_client_name (self, client_name):
        self.__client_name = client_name

    def set_client_phone (self, client_phone):
        self.__client_phone = client_phone
    
    def set_appt_type (self, appt_type):
        self.__appt_type = appt_type

    def set_day_of_week(self, day_of_week): 
        self.__day_of_week = day_of_week

    def set_start_time_hour(self, start_time_hour): 
        self.__start_time_hour = start_time_hour

    def schedule(self, name, phone, appt): # done by Clayton
        self.__client_name = name
        self.__client_phone = phone
        self.__appt_type = appt
        return 
    
    def cancel(self): # done by Clayton
        self.__client_name = 0
        self.__client_phone = 0
        self.__appt_type = 0
        return 

    def format_record(self): # done by Clayton
        return print(f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}')
        
    def __str__(self):
        client_name = self.__client_name
        client_phone = self.__client_phone
        appt_type = self.__appt_type
        day_of_week = self.__day_of_week
        start_time_hour = self.__start_time_hour
        end_time_hour = start_time_hour + 1
        return (f'{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:<10}{end_time_hour:<10}{self.__appt_type:<10}')