'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project (Appointment Manager)
Course: CPRG 216-B
Date: 12/12/2024
'''


import os
from typing import List

class Appointment:

    def __init__(self,client_name=0, client_phone=0, appt_type=0, day_of_week, start_time_hour):
        self.__client_name = client_name  # Appointment property
        self.__client_phone = client_phone  # Appointment property
        self.__appt_type = appt_type  # Appointment property
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
        
        return self.get_appt_type_desc

    def get_end_time_hour(self):
        return self.__start_time_hour + 1

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def set_day_of_week(self, day_of_week):
        self.__day_of_week = day_of_week

    def set_start_time_hour(self, start_time_hour):
        self.__start_time_hour = start_time_hour

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.__client_name = 0
        self.__client_phone = 0
        self.__appt_type = 0

    def format_record(self):
        return f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}\n'

    def __str__(self):
        client_name = self.__client_name
        client_phone = self.__client_phone
        appt_type = self.__appt_type
        day_of_week = self.__day_of_week
        start_time_hour = self.__start_time_hour
        end_time_hour = start_time_hour + 1
        return (f'{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:<10}{end_time_hour:<10}{self.__appt_type:<10}')

appointment_list: List[Appointment] = []
start_time_hour_available = (9, 10, 11, 12, 13, 14, 15, 16)
day_of_week_available = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
appt_types = ('1', '2', '3', '4')

def create_weekly_calendar():
    appointment_list.clear()
    for day in day_of_week_available:
        for hour in start_time_hour_available:
            fin_appointment = Appointment(client_name=0, client_phone=0, appt_type=0, day_of_week=day, start_time_hour=hour)
            appointment_list.append(fin_appointment)
    print("Weekly calendar created.")

def save_scheduled_appointments():
    file_name = input("Enter a file name: ")
    if os.path.exists(file_name):
        option_select = input(f"A file with the name {file_name} already exists. Overwrite (O) or enter a new filename (N)? ").upper()
        if option_select == "O":
            with open(file_name, "w") as f:
                for appointment in appointment_list:
                    f.write(appointment.format_record())
            print(f"Appointments saved to {file_name}")
            return 'Yes'
        elif option_select == "N":
            new_file = input("Enter new file name: ")
            with open(new_file, "w") as f:
                for appointment in appointment_list:
                    f.write(appointment.format_record())
            print(f"A new file has been created using the name {new_file}")
            return 'Yes'
    else: 
        with open(file_name, "w") as f:
            for appointment in appointment_list:
                f.write(appointment.format_record())

def load_scheduled_appointments():
    file_load_name = input("Please enter the file name you want to load: ")
    if os.path.exists(file_load_name):
        with open(file_load_name, "r") as f:
            for line in f:
                print(line.rstrip())
    else:
        print("File not found")

def find_appointment_by_time():
    specific_appointments = []
    day = input("Enter the day you would like to search for: ").upper()
    time = int(input("Enter a time to search for appointments: "))
    for appointments in appointment_list:
        if appointments.get_start_time_hour() == time and appointments.get_day_of_week() == day:
            specific_appointments.append(appointments)
            print(f"{specific_appointments}")
            specific_appointments.clear


def show_appointments_by_name():
    entered_name = input("Please enter the name you would like to search: ")
    matching_appointments = []
    for appt in appointment_list:
        if entered_name.capitalize() in appt.get_client_name():
            matching_appointments.append(appt)
            print(matching_appointments)
        

def change_appointment_by_day_time():
   
    original_day = input("Enter the original day of the appointment: ").upper()
    original_time = input("Enter the original time of the appointment (24-hour clock): ")

    original_time = int(original_time)
    for appt in appointment_list:
       
        if original_day in appt.get_day_of_week() and appt.get_start_time_hour() == original_time:
            appointment_to_change = appt  

    new_day = input("Enter the new day for the appointment: ").upper()
    if new_day not in day_of_week_available:
        print(f"{new_day} is an invalid day or the salon is closed.")
        
    new_time = input("Enter the new time for the appointment (24-hour clock): ")
    if not new_time.isdigit():
        print("Invalid time format. Please enter a number.")
        return
    new_time = int(new_time)
    if new_time not in start_time_hour_available:
        print("That time is already booked")
        return
    for appt in appointment_list:
        if appt.get_day_of_week() == new_day and appt.get_start_time_hour() == new_time:
            print("Sorry, that time slot is already booked.")
            return
    appointment_to_change.set_day_of_week(new_day)
    appointment_to_change.set_start_time_hour(new_time)
    print("Appointment updated successfully!")





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
def print_menu():
    print('1) Create new weekly calendar')
    print('2) Find appointment by name')
    print('3) Find appointment by time')
    print('4) Cancel an appointment')
    print('5) Save scheduled appointments to file')
    print('6) Load scheduled appointments from file')
    print('7) Exit the system')

def main():
    create_weekly_calendar()
    print("Weekly calendar created")

    while True:
        print('=' * 40)
        print('Hair Salon Appointment Manager')
        print('=' * 40)

        print_menu()
        menu_choice = input('Enter your selection: ')

        if menu_choice == '1':
            create_weekly_calendar()
        elif menu_choice == '2':
            show_appointments_by_name()
        elif menu_choice == '3':
            find_appointment_by_time()
        elif menu_choice == '4':
            print('Cancel appointment functionality not implemented yet.')
        elif menu_choice == '5':
            save_scheduled_appointments()
        elif menu_choice == '6':
            load_scheduled_appointments()
        elif menu_choice == '7':
            print('Exiting system. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
