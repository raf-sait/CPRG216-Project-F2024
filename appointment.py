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

    def __init__(self, day_of_week, start_time_hour, client_name = 0, client_phone = 0, appt_type = 0):
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = ''

        '''
        Function name: __init__
        Description: Initializes the objects, with __ added to keep them hidden
        Parameters: day of week, start time hour, client name, client phone, appt type
        Returns:
        '''

    def get_client_name(self):
        return self.__client_name
    
        '''
        Function name: get_client_name
        Description: gets the requested name from the schedule
        Parameters: self
        Returns: client_name
        '''

    def get_client_phone(self):
        return self.__client_phone
    
        '''
        Function name: get_client_phone
        Description: gets the requested client's phone number
        Parameters: self
        Returns: client_phone
        '''

    def get_appt_type(self):
        return self.__appt_type
        '''
        Function name: get_appt_type
        Description: gets the requested appointment type
        Parameters: self
        Returns: appt_type
        '''

    def get_day_of_week(self):
        return self.__day_of_week
        '''
        Function name: get_day_of_week
        Description: gets the requested day of the week of the client
        Parameters: self
        Returns: day_of_the_week
        '''

    def get_start_time_hour(self):
        return self.__start_time_hour
        '''
        Function name: start_time_hour
        Description: gets the starting hour of the client's appointment
        Parameters:self
        Returns: start_time_hour
        '''

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
        return self.__appt_type_desc
        
        '''
        Function name: get_appt_type_desc
        Description: Gets the requested appointment type
        Parameters: self
        Returns: Appointment type (1, 2, 3, or 4)
        '''

    def get_end_time_hour(self):
        return self.__start_time_hour + 1
        '''
        Function name: get_end_time_hour
        Description: gets the ending hour of the appointment
        Parameters: self
        Returns: end_time_hour
        '''

    def set_client_name(self, client_name):
        self.__client_name = client_name
        
        '''
        Function name: set_client_name
        Description: sets the client's name
        Parameters: self, client_name
        Returns: self.__client_name
        '''

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

        '''
        Function name: set_client_phone
        Description: sets the client's phone number
        Parameters: self, client_phone
        Returns: self.__client.phone
        '''

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

        '''
        Function name: set_appt_type
        Description: sets the appointment type of client
        Parameters:self, appt_type
        Returns: self.__appt_type
        '''

    def set_day_of_week(self, day_of_week):
        self.__day_of_week = day_of_week
        '''
        Function name: set_day_of_week
        Description: sets the client's appointment day of the week
        Parameters: self, day_of_week
        Returns: self.__day_of_week
        '''

    def set_start_time_hour(self, start_time_hour):
        self.__start_time_hour = start_time_hour
        '''
        Function name: set_start_time_hour
        Description: sets the starting hour of the client's appointment
        Parameters: self, start_time_hour
        Returns: self.__start.time_hour
        '''        

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)
        
        '''
        Function name: schedule
        Description: sets the schedule of the client with the required information
        Parameters: self, client_name, client_phone, appt_type
        Returns:
        '''

    def cancel(self):
        self.__client_name = 0
        self.__client_phone = 0
        self.__appt_type = 0
        
        '''
        Function name: cancel
        Description: cancel's the appoinment by replacing all values with 0
        Parameters: self
        Returns:
        '''

    def format_record(self):
        return f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}'
    
        '''
        Function name: format_record
        Description: outputs the record of the client with a specific format
        Parameters: self
        Returns: {self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}
        '''

    def __str__(self):
        client_name = self.__client_name
        client_phone = self.__client_phone
        appt_type = self.__appt_type
        day_of_week = self.__day_of_week
        start_time_hour = self.__start_time_hour
        end_time_hour = start_time_hour + 1
        return (f'{self.__client_name:<10}{self.__client_phone:<10}{self.__day_of_week:<10}{self.__start_time_hour}:00 - {end_time_hour}:00{self.__appt_type:<10}')
    
        '''
        Function name: __str__
        Description: Outputs the string of the class with all the information
        Parameters: self
        Returns: {self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:<10}{end_time_hour:<10}{self.__appt_type:<10}
        '''

appointment_list = []
start_time_hour_available = (9, 10, 11, 12, 13, 14, 15, 16)
day_of_week_available = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
appt_types = ['1', '2', '3', '4']

def create_weekly_calendar():
    appointment_list.clear()
    for day in day_of_week_available:
        for hour in start_time_hour_available:
            fin_appointment = Appointment(client_name = 0, client_phone = 0, appt_type = 0, day_of_week = day, start_time_hour = hour)
            appointment_list.append(fin_appointment)
    print("Weekly calendar created.")
    '''
    Function name: create_weekly_calendar
    Description: creates the weekly calendar needed for appointments
    Parameters: 
    Returns: cleared weekly calendar ready for input
    '''

def save_scheduled_appointments():
    file_name = input('Enter appointment filename: ')

    if os.path.exists(file_name):
        option_select = input(f'File already exists. Do you want to overwrite it (Y/N)? ').upper()
        if option_select == 'Y':
            with open(file_name, "w") as f:
                for appointment in appointment_list:
                    f.write(appointment.format_record())
            print(f"Appointments saved to {file_name}")
        if option_select == 'N':
            file_name = input('Enter appointment filename: ')
    
    with open(file_name, "w") as f:
        for appointment in appointment_list:
            f.write(appointment.format_record())
            line = file_name.readlines()
            count_appointments = len(line)
            print(f'{count_appointments} scheduled appointments have been successfully saved.')
    
    '''
    Function name: save_scheduled_appointments()
    Description: saves the scheduled appointments in a .txt file
    Parameters: file_name
    Returns: csv file with input appointment records
    '''

def load_scheduled_appointments():
    file_load_name = input('Please enter the file name you want to load: ')
    if os.path.exists(file_load_name):
        with open(file_load_name, 'r') as file_load_name:
            line = file_load_name.readlines()
            count_appointments = len(line)
            for line in file_load_name:
                client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                appointment = Appointment(client_name, client_phone, appt_type, day_of_week, start_time_hour)
                appointment_list.append(appointment)
    else:
        file_load_name = input('File not found. Re-enter appointment filename:')
    print(f'{count_appointments} previously scheduled appointments have been loaded.') 

    '''
    Function name: load_scheduled_appointments
    Description: Loads the scheduled appointments from an external files
    Parameters: name of csv file
    Returns: pre-filled appointment file, and number of appoinments
    '''

def find_appointment_by_time():
    specific_appointments = []
    day = input("Enter the day you would like to search for: ").upper()
    time = int(input("Enter a time to search for appointments: "))
    for appointments in appointment_list:
        if appointments.get_start_time_hour() == time and appointments.get_day_of_week() == day:
            specific_appointments.append(appointments)
            print(f"{specific_appointments}")
            specific_appointments.clear
    return 'Yes'

    '''
    Function name: find_appointment_by_time
    Description: finds a client's appointments via the time they booked
    Parameters: user input of day and time
    Returns: cleared appointment (if applicable)
    '''

def show_appointments_by_name():
    entered_name = input('Enter Client Name:')
    matching_appointments = []
    print(f'Appointments for {entered_name}')
    print(f'{'Client Name':>20} {'Phone':>20} {'Day':>20} {'Start':>20} {'End':>20} {'Type':>20}')
    print('-' * 150)
    for appointment in appointment_list:
        if entered_name.capitalize() in appointment.get_client_name():
            matching_appointments.append(appointment)
            print(matching_appointments)
    return 'Yes'
    '''
    Function name: show_appointments_by_name
    Description: shows the appointment of a client by their name
    Parameters: client name
    Returns: table showing appointments associated with a specific name
    '''
        
def show_appointments_by_day():
    search_day = input('Enter the day you would like to see the schedule for ').title()
    print(f'Appointments for {search_day}')
    print(f'{'Client Name':<20} {'Phone':<10} {'Day':<10} {'Start':<10} {'End':<10} {'Type':<10}')
    print('-' * 100)
    for appointment in appointment_list:
        if appointment.get_day_of_week() == search_day:
            print(appointment)
    '''
    Function name: show_appointments_by_day
    Description: shows the appointments associated with a day
    Parameters: day of the week
    Returns: table showing appointments associated with a day
    '''

def cancel_appointment():
    day_to_cancel = input('What day:  ').title()
    time_to_cancel = input('Enter start hour (24 hour clock): ')
    for appointment in appointment_list:
        if appointment.get_day_of_week() == day_to_cancel and appointment.get_start_time_hour() == time_to_cancel:
            print(f"{appointment.get_day_of_week()}, {appointment.get_start_time_hour}-{appointment.get_end_time_hour} for {appointment.get_client_name} has been cancelled!")
            appointment_list.remove(appointment)
        else:
            print("That time slot isn't booked and doesn't need to be changed")
    '''
    Function name: canceL_appointment
    Description: removes an appointment in appointment_list (if matching)
    Parameters: day and time to cancel
    Returns: appointment is removed from appointment_list
    '''

def change_appointment_by_day_time():
    original_day = input('What day: ').upper()
    original_time = input('Enter start hour (24 hour clock): ')
    original_time = int(original_time)
    for appointment in appointment_list:
        if original_day in appointment.get_day_of_week() and appointment.get_start_time_hour() == original_time:
            appointment_to_change = appointment  
        else:
            print("That time slot isn't booked and doesn't need to be changed")

    new_day = input("Enter the new day for the appointment: ").upper()
    if new_day not in day_of_week_available:
        print(f"{new_day} is invalid day or the salon is closed.")
        
    new_time = input("Enter the new time for the appointment (24-hour clock): ")
    if not new_time.isdigit():
        print("Invalid time format. Please enter a number.")
        return 'Yes'
    
    new_time = int(new_time)
    if new_time not in start_time_hour_available:
        print("That time is already booked")
        return 'Yes'
    for appointment in appointment_list:
        if appointment.get_day_of_week() == new_day and appointment.get_start_time_hour() == new_time:
            print("Sorry, that time slot is already booked.")
            return 'Yes'
        
    appointment_to_change.set_day_of_week(new_day)
    appointment_to_change.set_start_time_hour(new_time)
    print(f'Appointment for ____ has been changed to:')
    print(new_day)
    print(new_time)
    return 'Yes'
    '''
    Function name: change_appointment_by_day_time
    Description: changes appointment based on day and time inputted
    Parameters: day and time inputted
    Returns: changed day and time
    '''

def calculate_fees_per_day():
    day_for_total_fees = input('What day: ').title()
    if day_for_total_fees not in day_of_week_available:
        print(f'{day_for_total_fees} is invalid day or the salon is closed')
        return 'Yes'
    for appointment in appointment_list:
        if appointment.get_day_of_week() == day_for_total_fees: 
            appointment_type = appointment.get_appt_type()
            if appointment_type == 1 or 3:
                fee = 40
            elif appointment_type == 2:
                fee = 60
            elif appointment_type == 4:
                fee = 80
            total_fees = 0
            total_fees += fee
    print(f'Total fees for {day_for_total_fees} is ${total_fees}')
    return 'Yes'
    '''
    Function name: calculate_fees_per_day
    Description: calculates the total fees of a day
    Parameters: 
    Returns: fees for given day based on appointment list
    '''

def calculate_fees_per_week():
    for appointment in appointment_list:
        appointment_type = appointment.get_appt_type
        if appointment_type == 1 or 3:
            fee = 40
        elif appointment_type == 2:
            fee = 60
        elif appointment_type == 4:
            fee = 80
        total_weekly_fees = 0
        total_weekly_fees += fee
    print(f'Total weekly fees is ${total_weekly_fees}')
    return 'Yes'
    '''
    Function name: calculate_fees_per_week
    Description: calculates the total fees of that whole week
    Parameters: 
    Returns: fees for given week based on appointment list
    '''

def create_appointment():
    day_of_week = input('What day: ').title()
    if day_of_week not in day_of_week_available:
        print(f'{day_of_week} is invalid day or the salon is closed')
        return 'Yes'
    start_time_hour = int(input('Enter start hour (24 hour clock) '))
    if start_time_hour not in start_time_hour_available:
        print('Sorry that time slot is not in the weekly calendar!')
        return 'Yes'
    client_name = input('Client name: ')
    client_phone = input('Client Phone: ')
    print('Appointment types')
    print('1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80')
    appt_type = input('Type of Appointment: ')
    if appt_type not in appt_types:
        return
    else:
        appointment = Appointment(day_of_week,start_time_hour)
        appointment.schedule(client_name,client_phone,appt_type)
        appointment_list.append(appointment)
        print(f'OK, {client_name}s appointment is scheduled!')
    '''
    Function name: create_appointment()
    Description: shows the appointments associated with a day
    Parameters: day of the week, start time hour, client name, client phone, appointment type
    Returns: appointment added with listed parameters
    '''

def print_menu():
    print('1) Schedule an appointment')
    print('2) Find appointment by name')
    print('3) Print calendar for a specific day')
    print('4) Cancel an appointment')
    print('5) Change an appointment')
    print('6) Calculate total fees for a day')
    print('7) Calculate total weekly fees')
    print('9) Exit the system')

    '''
    Function name: print_menu
    Description: shows menu inputs for main()
    Parameters:
    Returns:
    ''' 

def main():
    create_weekly_calendar()
    previously_scheduled_appointment = input('Would you like to load previously scheduled appointments from a file (Y/N?)').upper()
    if previously_scheduled_appointment == 'Y':
        load_scheduled_appointments()

    keep_checking = 'Yes'
    while keep_checking == 'Yes':

        print('=' * 40)
        print('Hair Salon Appointment Manager')
        print('=' * 40)

        print_menu()
        menu_choice = input('Enter your selection: ')

        if menu_choice == '1':
            print()
            print('** Schedule an appointment **')
            create_appointment()

        elif menu_choice == '2':
            print()
            print('** Find appointment by name **')
            show_appointments_by_name()

        elif menu_choice == '3':
            print()
            print('** Print calendar for a specific day **')
            show_appointments_by_day()
            
        elif menu_choice == '4':
            print()
            print('** Cancel an appointment **')
            cancel_appointment()

        elif menu_choice == '5':
            print()
            print('** Change an appointment **')
            change_appointment_by_day_time()

        elif menu_choice == '6':
            print()
            print('** Calculate total fees for a day **')
            calculate_fees_per_day()

        elif menu_choice == '7':
            print()
            print('** Calculate weekly fees **')
            calculate_fees_per_week()
            
        elif menu_choice == '9':
            print()
            print('** Exit the System **')
            save_appointments_to_file = input('Would you like to save all scheduled appointments to a file (Y/N?)').upper()
            if save_appointments_to_file == 'Y':
                save_scheduled_appointments()
                print('Good Bye!')
                exit()
            if save_appointments_to_file == 'N':
                print('Good Bye!')
                exit()
        else:
            print()
            print('Invalid option')

    '''
    Function name: main
    Description: The main function where the application is ran
    Parameters: user input (1-9)
    Returns: runs the program based on user input
    '''
    
if __name__ == '__main__':
    main()
