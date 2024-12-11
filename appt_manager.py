'''
Author: Elizar Tagle, Clayton Ma, Rafael de Dios
Student IDs: 950160 (Rafael), 760796 (Clayton), 961496 (Elizar)
Assignment: Final Project (Appointment Manager)
Course: CPRG 216-B
Date: 12/12/2024
'''

def create_weekly_calendar():




    '''
    Function name:
    Description:
    Parameters:
    Returns:
    '''

def load_scheduled_appointments():




    '''
    Function name:
    Description:
    Parameters:
    Returns:
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
    Function name:
    Description:
    Parameters:
    Returns:
    '''

def main():
    previous_scheduled_appointment = ''
    
    print('Starting the Appointment Manager System')
    print('Weekly calendar created')
    
    previously_scheduled_appointment = input('Would you like to load previously scheduled appointments from a file (Y/N?)').upper()
    if previous_scheduled_appointment == 'y':
        print('placeholder')
    else:
        print('placeholder 2')
    
    print(f'='*40)
    print(f'Hair Salon Appointment Manager')
    print(f'='*40)

    print_menu()
    menu_choice = input('Enter your selection: ')
    
    if menu_choice == '1':
        print()
        print('** Schedule an appointment **')
    
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
            print('placeholder')
            print('Good Bye!')
        else:
            print('placeholder 2')
            print('Good Bye!')

    else:
        print('Invalid input')

if __name__ == '__main__':
    main()
