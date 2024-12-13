'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project (Appointment Manager)
Course: CPRG 216-B
Date: 12/12/2024
'''
import os 
appointment_list = []
available_timeslots = (9,10, 11, 12, 13, 14, 15, 16)
available_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
appointment_types = [1,2,3,4]

def create_weekly_calendar():
   appointment_list.clear()
   for day in available_days:
    for hour in available_timeslots:
     for type in appointment_types:
        free_appointments = (day,hour,type) 
        appointment_list.append(free_appointments)    

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


def load_scheduled_appointments():
    file_load_name = input("Please enter the file name you want to load: ")
    if os.path.exists(file_load_name):
        with open(f"{file_load_name}", "r") as f:
            for line in f: 
                print(line.rstrip())
    else:
        print("File not found")

def find_appointment_by_time():
    specific_appointments = []
    day = str(input(" Enter the day you would like to search for: ")).upper
    time = int(input("Enter a time to search for appointments"))
    for appointments in appointment:
        if appointment.start_time_hour == time and appoinment.day_of_week == day:
            specific_appointments.append(appointments)
            print(f"{specific_appointments}")
            specific_appointments.clear

def show_appointments_by_name():
    matching_name=[]
    entered_name = input("Please enter the name you would like to search: ")
    







def print_menu():
    print('1) Create new weekly calendar')
    print('2) Find appointment by name')
    print('3) Print calendar for a specific day')
    print('4) Cancel an appointment')
    print('5) Change an appointment')
    print('6) Calculate total fees for a day')
    print('7) Calculate total weekly fees')
    print('9) Exit the system')

    '''
    Function name:
    Description:
    Parameters:
    Returns:
    '''

def main():
    
    
    print('Starting the Appointment Manager System')
    print('Weekly calendar created')
    
    previously_scheduled_appointment = input('Would you like to load previously scheduled appointments from a file (Y/N?)').upper()
    if previously_scheduled_appointment == 'y':
        load_scheduled_appointments()
    else:
        print('placeholder 2')
    
    print(f'='*40)
    print(f'Hair Salon Appointment Manager')
    print(f'='*40)

    print_menu()
    menu_choice = input('Enter your selection: ')
    
    if menu_choice == '1':
       create_weekly_calendar()
    
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
    
    elif menu_choice == '7':
        print()
        print('** Calculate total weekly fees **')
    
    elif menu_choice == '9':
        print()
        print('** Exit the System **')

        save_appointments_to_file = input('Would you like to save all scheduled appointments to a file (Y/N?)').upper()
        if save_appointments_to_file == 'y':
            save_appointments_to_file()
            print('placeholder')
            print('Good Bye!')
        else:
            print('placeholder 2')
            print('Good Bye!')

    else:
        print('Invalid input')

if __name__ == '__main__':
    main()
