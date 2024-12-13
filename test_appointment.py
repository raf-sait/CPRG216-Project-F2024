#
# test_appointment - This program tests the majority of the methods in the Appointment class
#
# Author:
# Version/Date:
#
import appointment as ap

def main():
    # Here are the types of appointments:
    # 0 - Available, 1 = Mens cut $50, 2= Ladies cut $80, 3= Mens Colouring $50, 4= Ladies Colouring $120
    # create a list of 7 appointments for Saturday (between 9:00 and 15:00 start time)
    appt_list = []
    day = "Saturday"
    for time in range(9, 16):
        appt_list.append(ap.Appointment(day, time))

    # Book the first appointment slot (9 AM) for Harvey Wallbanger for a Men's Cut (appt_type = 1)
    current_appt = appt_list[0]
    current_appt.schedule("Harvey", "403-233-3944", 1)

    # Book the second appointment slot (10 AM) for Sara for a Ladies Colouring
    current_appt = appt_list[1]
    current_appt.schedule("Sara", "403-233-3945", 4)

    # Go through all the appointments and find the noon hour slot and book Jenny for a cut
    found = False
    index = 0
    while index < len(appt_list) and not found:
        current_appt = appt_list[index]
        # is this appointment the noon hour appointment for Saturday available?
        if current_appt.get_day_of_week() == "Saturday" and \
           current_appt.get_start_time_hour() == 12 and \
           current_appt.get_appt_type() == 0:
            found = True
        index += 1
    if found:
        # book it!
        current_appt.set_client_name("Jenny")
        current_appt.set_client_phone("403-867-5309")
        current_appt.set_appt_type(2)  # 2 - Ladies Cut
    else:
        print("Appointment entry not found")

    # Print only scheduled appointments using format_record()
    print("Scheduled appointment records:")
    for appt in appt_list:
        if appt.get_appt_type() != 0:
            print(appt.format_record())

    # Cancel Sara's appointment
    current_appt = appt_list[1]
    current_appt.cancel()

    # Print report of all appointment times using string method
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    for appt in appt_list:
        print(appt)
        
if __name__ == "__main__":
    main()