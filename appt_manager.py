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

    def schedule(self, client_name, client_phone, appt_type): # done by Clayton
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)
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

import os

appointment_list = []
start_time_hour_available = (9, 10, 11, 12, 13, 14, 15, 16)
day_of_week_available = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
appt_types = ('1','2','3','4')

def create_weekly_calendar():
   appointment_list.clear()
   for day in day_of_week_available:
    for hour in start_time_hour_available:
     for type in appt_types:
        free_appointments = (day,hour,type) 
        appointment_list.append(free_appointments)    
    return 'Yes'

def save_scheduled_appointments():
    file_name = input("Enter a file name")
    if os.path.exists(file_name):
        option_select = input(f"there is already a file with the name {file_name}, please select O to overwrite or R to repeat the filename")
        if option_select == "O".upper:
            saved_appointments = open(f"{file_name},", "w")
            saved_appointments.write({appointment_list})
            saved_appointments.write()
        elif option_select == "R".upper:
             saved_appointments = open(f"{file_name},", "w")
             saved_appointments.write({appointment_list})
             saved_appointments.write()
             print(f"A new file has been created using the name {file_name}")
    else:
         saved_appointments = open(f"{file_name},", "w")
         saved_appointments.write({appointment_list})
         saved_appointments.write()
    return 'Yes'




def load_scheduled_appointments():
    file_load_name = input("Please enter the file name you want to load: ")
    if os.path.exists(file_load_name):
        with open(f"{file_load_name}", "r") as f:
            for line in f: 
                print(line.rstrip())
    else:
        print("File not found")
    return 'Yes'

def find_appointment_by_time():
    specific_appointments = []
    day = str(input(" Enter the day you would like to search for: ")).upper
    time = int(input("Enter a time to search for appointments"))
    for appointments in appointment_list:
        if appointment_list.start_time_hour == time and appointment_list.day_of_week == day:
            specific_appointments.append(appointments)
            print(f"{specific_appointments}")
            specific_appointments.clear

def show_appointments_by_name():
    matching_name=[]
    entered_name = input("Please enter the name you would like to search: ")
    return 'Yes'

    
def create_appointment():
    day_of_week = input('What day: ').upper()
    if day_of_week not in day_of_week_available:
        print(f'{day_of_week} is invalid day or the salon is closed')
        return 'Yes'
    start_time_hour = int(input('Enter start hour (24 hour clock) '))
    if start_time_hour not in start_time_hour_available:
        print('Sorry that time slot is not in the weekly calendar!')
        return 'Yes'
    end_time_hour = start_time_hour + 1
    client_name = input('Client name: ')
    client_phone = input('Client Phone: ')
    print('Appointment types')
    print('1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80')
    appt_type = input('Type of Appointment: ')
    if appt_type not in appt_types:
        return 'Yes'
    else:
        appointment = Appointment(day_of_week,start_time_hour)
        appointment.schedule(client_name,client_phone,appt_type)
        print(f'OK, {client_name}s appointment is scheduled!')
    return 'Yes'


def print_menu():
    print('1) Create new weekly calendar')
    print('2) Find appointment by name')
    print('3) Print calendar for a specific day')
    print('4) Cancel an appointment')
    print('5) Change an appointment')
    print('6) Calculate total fees for a day')
    print('7) Calculate total weekly fees')
    print('9) Exit the system')


#defchange_appointment_by_day_time():
#def calculate_fees_per_day():
#def calculate_weekly_fees():
#def save_scheduled_appointments():

print('Starting the Appointment Manager System')
print('Weekly calendar created')
    
previously_scheduled_appointment = input('Would you like to load previously scheduled appointments from a file (Y/N?)').upper()
if previously_scheduled_appointment == 'Y':
    load_scheduled_appointments()

def main():
    keep_running = 'Yes'
    while keep_running == 'Yes':
        print(f'='*40)
        print(f'Hair Salon Appointment Manager')
        print(f'='*40)

        print_menu()
        menu_choice = input('Enter your selection: ')
        
        if menu_choice == '1':
            print()
            print('** Schedule an appointment **')
            create_appointment()

        elif menu_choice == '2':
            print()
            print('** Find appointment by name **')
        elif menu_choice == '3':
            print()
            print('** Print calendar for a specific day **')

        elif menu_choice == '4':
            print()
            print('** Cancel an appointment **')
        elif menu_choice == '5':
            print()
            print('** Change an appointment **')
        elif menu_choice == '6':
            print()
            print('** Calculate total fees for a day **')
            #calculate_fees_per_day()
        elif menu_choice == '7':
            print()
            print('** Calculate total weekly fees **')
            #calculate_weekly_fees()
        elif menu_choice == '9':
            print()
            print('** Exit the System **')
            save_appointments_to_file = input('Would you like to save all scheduled appointments to a file (Y/N?)').upper()
            if save_appointments_to_file == 'Y':
                save_appointments_to_file()
                print('placeholder')
                print('Good Bye!')
                exit()
            else:
                print('placeholder 2')
                print('Good Bye!')
                exit()
        else:
            print('Invalid input')

if __name__ == '__main__':
    main()
