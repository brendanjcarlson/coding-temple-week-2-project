import math

# ask user if they are ready to leave, if yes, leave and delete current spot, balance, and duration
# if no, enter while loop


# BC(layed out format and ticket/spot assign)
# JH(updated parking_spaces, removed current_ticket)


class ParkingGarage:
    parking_spaces = {
        'A1': {'occupied': False},
        'A2': {'occupied': False},
        'A3': {'occupied': False},
        'A4': {'occupied': False},
        'A5': {'occupied': False},
        'A6': {'occupied': False},
        'A7': {'occupied': False},
        'A8': {'occupied': False},
        'A9': {'occupied': False},
        'A10': {'occupied': False},
        'B1': {'occupied': False},
        'B2': {'occupied': False},
        'B3': {'occupied': False},
        'B4': {'occupied': False},
        'B5': {'occupied': False},
        'B6': {'occupied': False},
        'B7': {'occupied': False},
        'B8': {'occupied': False},
        'B9': {'occupied': False},
        'B10': {'occupied': False},
        'C1': {'occupied': False},
        'C2': {'occupied': False},
        'C3': {'occupied': False},
        'C4': {'occupied': False},
        'C5': {'occupied': False},
        'C6': {'occupied': False},
        'C7': {'occupied': False},
        'C8': {'occupied': False},
        'C9': {'occupied': False},
        'C10': {'occupied': False},
    }
    # JA(created prices dict and fee variable)
    prices = {
        'tier_1': 5,
        'tier_2': 8,
        'tier_3': 10,
    }
    fee = 2
    # JH(created text dict)
    text = {
        'spot_assign': "\nYou've been assigned spot {spot} and your balance is {balance}.",
        'garage_full': "\nIt appears all spots are currently taken. Apologies for the inconvenience.",
        'pay_balance': "\nAre you going to pay your balance?\n(Y)es | (N)o\n",
        'current_balance': "\nYou have a balance of {balance} remaining. How much would you like to pay towards it?",
        'no_leave': "\nYou can't leave until you pay your full balance.",
        'show_balance': "\nYour balance is still {balance}. Please pay your balance before leaving.",
        'park_query': "\nWould you like to park?\n(Y)es | (N)o\n",
        'exit_query': "\nWould you like to exit?\n(Y)es | (N)o\n",
        'query_error': "\nInvalid selection, please select:\n(Y)es | (N)o\n",
        'payment_success': "\nYour payment was received and your balance is {balance}. You have 15 minutes to leave the garage. Thank you!",
        'good_day': "\nHave a good day!",
        'duration_query': "\nHow long do you want to park? (4, 8, or 12) hours\n",
        'payment_duration': "\nHow many long did you park for (in hours)? eg. 4 or 5.3",
        'fee_applied': "\nA fee of {fee} per hour has been added to your balance for going over your allotted duration.\nYour new balance is {balance}",
        'pay_full': "You have a balance of {balance}. Would you like to pay the full balance or just a portion? (F)ull | (P)ortion",
    }
    # JH(made options dict)
    options = {
        'yes': ['y', 'yes', 'ye', 'yeah', 'yea', 'yeh', 'ya', 'yah', '(y)es', '(y)'],
        'no': ['n', 'no', 'nah', 'na', 'nay', '(n)o', '(n)'],
        'full': ['f', 'full', 'all'],
        'portion': ['p', 'portion', 'some'],
    }

    # BC(layed out logic)

    # JA(worked on pay_for_parking, updated take_ticket)

    def __init__(self, current_spot=""):
        self.current_spot = current_spot

    # JH(worked on take_ticket, leave_garage)
    # BC(added spot assignment and counter loop and parking duration)
    # JA(added logic for parking duration fee)
    def take_ticket(self, parking_duration):
        # assign user a spot
        # update their balance with cost of ticket

        # Loops over dict for occupied spots each time a ticket is taken
        count = 0
        for spot in self.parking_spaces:
            if self.parking_spaces[spot]['occupied']:
                count += 1

        # Assigning a user first avail. spot unless full, sets spot to occupied, sets balance to price
        for spot in self.parking_spaces:
            if not self.parking_spaces[spot]['occupied']:
                self.parking_spaces[spot]['occupied'] = True
                self.parking_spaces[spot]['duration'] = parking_duration
                self.current_spot = spot
                if self.parking_spaces[spot]['duration'] <= 4:
                    # parking_duration is less than 4, price will change the balance for tier_1
                    self.parking_spaces[spot]['balance'] = self.prices['tier_1']
                    print(self.text['spot_assign'].format(
                        spot=spot, balance=self.parking_spaces[spot]['balance']))
                    break
                elif self.parking_spaces[spot]['duration'] > 4 or self.parking_spaces[spot]['duration'] <= 8:
                    # parking_duration between 4 and 8, price will change the balance for tier_2
                    self.parking_spaces[spot]['balance'] = self.prices['tier_2']
                    print(self.text['spot_assign'].format(
                        spot=spot, balance=self.parking_spaces[spot]['balance']))
                    break
                else:
                    # parking_duration greater than 8 hours, price will change the balance for tier_3
                    self.parking_spaces[spot]['balance'] = self.prices['tier_3']
                    print(self.text['spot_assign'].format(
                        spot=spot, balance=self.parking_spaces[spot]['balance']))
                    break
            elif count == 30:
                print(self.text['garage_full'])

    # BC(added input/logic for adding fee if user over time)
    def pay_for_parking(self):
        user_duration = float(
            input(self.text['payment_duration']))
        if user_duration > self.parking_spaces[self.current_spot]['duration']:
            time_over = user_duration - \
                self.parking_spaces[self.current_spot]['duration']
            self.parking_spaces[self.current_spot]['balance'] += self.fee * \
                math.ceil(time_over)
            print(self.text['fee_applied'].format(
                fee=self.fee, balance=self.parking_spaces[self.current_spot]['balance']))

        user_input = input(self.text['pay_full'].format(
            balance=self.parking_spaces[self.current_spot]['balance'])).lower()
        if user_input in self.options['full']:
            self.parking_spaces[self.current_spot]['balance'] = 0
            print(self.text['payment_success'].format(
                balance=self.parking_spaces[self.current_spot]['balance']))
        elif user_input in self.options['portion']:
            while self.parking_spaces[self.current_spot]['balance'] > 0:
                payment_input = float(input(self.text['current_balance'].format(
                    balance=self.parking_spaces[self.current_spot]['balance'])))
                if payment_input >= self.parking_spaces[self.current_spot]['balance']:
                    self.parking_spaces[self.current_spot]['balance'] = 0
                    print(self.text['payment_success'].format(
                        balance=self.parking_spaces[self.current_spot]['balance']))
                elif payment_input < self.parking_spaces[self.current_spot]['balance']:
                    self.parking_spaces[self.current_spot]['balance'] -= payment_input
                    print(self.text['no_leave'])

    def leave_garage(self):
        # set spot back to unoccupied
        # removes current_spot, duration value from the instance of the class

        # ask user if they are ready to leave
        self.parking_spaces[self.current_spot]['occupied'] = False
        del self.parking_spaces[self.current_spot]['balance']
        del self.parking_spaces[self.current_spot]['duration']
        self.current_spot = ''
        print(self.text['good_day'])


# BC(set up control flow)
def main():
    park = ParkingGarage()

    app_running = True
    while app_running:
        entering = True
        while entering:
            user_choice = input(park.text['park_query']).lower()
            if user_choice in park.options['yes']:
                parking_duration = int(
                    input(park.text['duration_query']))
                entering = False
                park.take_ticket(parking_duration)

                exiting = True
                while exiting:
                    user_choice = input(park.text['exit_query']).lower()
                    if user_choice in park.options['yes']:
                        park.pay_for_parking()
                        park.leave_garage()
                        exiting, app_running = False, False
                    elif user_choice in park.options['no']:
                        continue
                    else:
                        print(park.text['query_error'])
            elif user_choice in park.options['no']:
                print(park.text['good_day'])
                entering, app_running = False, False


main()
