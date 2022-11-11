from numpy import random


class ParkingGarage:
    parking_spaces = {
        '00': False, '01': False, '02': False, '03': False, '04': False, '05': False, '06': False, '07': False, '08': False, '09': False,
        '10': False, '11': False, '12': False, '13': False, '14': False, '15': False, '16': False, '17': False, '18': False, '19': False,
        '20': False, '21': False, '22': False, '23': False, '24': False, '25': False, '26': False, '27': False, '28': False, '29': False,
    }

    current_ticket = {
        '00': {
            'is_full': False,
            'balance': 0,
        }
    }

    num = random.random()
    if num not in current_ticket.keys():
        current_ticket[num] = num

    def __init__(self, current_tickets):
        self.current_tickets = {}

    def take_ticket(self):
        # decrease tickets by 1
        # decrease parking_spaces by 1
        # assign user a spot
        # update their balance with cost of ticket
        pass

    def pay_for_parking(self):
        # update balance and paid flag

        # check if balance is paid
        # if no pay balance
        # update balance if they pay
        # else dont let them leave
        pass

    def leave_garage(self):
        # increase tickets by 1
        # increase parking_spaces by 1
        # in a while loop
        # if user has paid for parking:
        #   allow them to leave
        # else:
        #   continue begging them to pay
        pass


def main():

    park = ParkingGarage()

    app_running = True
    while app_running:

        entering = True
        while entering:
            user_choice = input(
                "Would you like to park?\n(Y)es | (N)o").lower()
            if user_choice == "y" or user_choice == "yes":
                entering = False
            elif user_choice == "n" or user_choice == "no":
                print('Have a good day.')
                entering, app_running = False, False
            else:
                continue

        park.take_ticket()

        exiting = True
        while exiting:
            user_choice = input(
                "Would you like to exit?\n(Y)es | (N)o").lower()
            if user_choice == "y" or user_choice == "yes":
                park.pay_for_parking()
                # if paid, leave
                park.leave_garage()
                exiting, app_running = False, False
            elif user_choice == "n" or user_choice == "no":
                continue
            else:
                print('Please select (Y)es | (N)o')


main()
