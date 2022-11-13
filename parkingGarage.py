import math

# ask user if they are ready to leave, if yes, leave and delete current spot, balance, and duration
# if no, enter while loop


# BC(layed out format and ticket/spot assign. moved dictionaries to inside class)
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
    # BC(added k/v pairs to dict)
    # JH(created text dict)
    text = {
        'invalid_selection': "Invalid selection, please enter a valid number.",
        'spot_assign': "\nYou've been assigned spot {spot} and your balance is ${balance:.2f}.",
        'garage_full': "\nIt appears all spots are currently taken. Apologies for the inconvenience.",
        'pay_balance': "\nAre you going to pay your balance?\n(Y)es | (N)o\n",
        'current_balance': "\nYou have a balance of ${balance:.2f} remaining. How much would you like to pay towards it?\n",
        'no_leave': "\nYou can't leave until you pay your full balance.",
        'show_balance': "\nYour balance is still ${balance:.2f}. Please pay your balance before leaving.",
        'park_query': "\nWould you like to park?\n(Y)es | (N)o\n",
        'leave_query': "\nAre you ready to leave?\n(Y)es | (N)o\n",
        'exit_query': "\nWould you like to exit?\n(Y)es | (N)o\n",
        'query_error': "\nInvalid selection, please select:\n(Y)es | (N)o\n",
        'payment_success': "\nYour payment was received and your balance is ${balance:.2f}. You have 15 minutes to leave the garage. Thank you!",
        'good_day': "\nHave a good day!",
        'duration_query': "\nHow long do you want to park? (4, 8, or 12)hours\n",
        'payment_duration': "\nHow long did you park for (in hours)? eg. 4 or 5.3\n",
        'fee_applied': "\nA fee of ${fee:.2f} per hour has been added to your balance for going over your allotted duration.\nYour new balance is ${balance:.2f}",
        'pay_full': "You have a balance of ${balance:.2f}. Would you like to pay the full balance or just a portion? (F)ull | (P)ortion\n",
        'show_timer': "You have {timer} more minutes until the authorities are called. Stay at your own risk.",
        'call_popo': "\U0001F6A8 \U0001F693 \U0001F6A8 \U0001F693 \U0001F6A8 TIME'S UP SUCKA. WOOP WOOP THAT'S THE SOUND OF THE POLICE. \U0001F6A8 \U0001F693 \U0001F6A8 \U0001F693 \U0001F6A8",
    }
    # BC(added k/v pairs to dict)
    # JH(made options dict)
    options = {
        'yes': ['y', 'yes', 'ye', 'yeah', 'yea', 'yeh', 'ya', 'yah', '(y)es', '(y)'],
        'no': ['n', 'no', 'nah', 'na', 'nay', '(n)o', '(n)'],
        'full': ['f', 'full', 'all'],
        'portion': ['p', 'portion', 'some'],
    }

    # BC(layed out logic)

    # JA(worked on pay_for_parking, updated take_ticket)

    def __init__(self, current_spot="", timer=15):
        self.current_spot = current_spot
        self.timer = timer

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
    # JH(added try/except)
    def pay_for_parking(self):
        pay_durationing = True
        while pay_durationing:
            user_duration = input(self.text['payment_duration'])
            try:
                user_duration = abs(float(user_duration))
                pay_durationing = False
            except:
                print(self.text['invalid_selection'])

        if user_duration > self.parking_spaces[self.current_spot]['duration']:
            time_over = user_duration - \
                self.parking_spaces[self.current_spot]['duration']
            self.parking_spaces[self.current_spot]['balance'] += self.fee * \
                math.ceil(time_over)
            print(self.text['fee_applied'].format(
                fee=self.fee, balance=self.parking_spaces[self.current_spot]['balance']))

    # BC(worked on payment processing functionality)
    # JH(added try/except)
        user_input = input(self.text['pay_full'].format(
            balance=self.parking_spaces[self.current_spot]['balance'])).lower()
        if user_input in self.options['full']:
            self.parking_spaces[self.current_spot]['balance'] = 0
            print(self.text['payment_success'].format(
                balance=self.parking_spaces[self.current_spot]['balance']))
        elif user_input in self.options['portion']:
            while self.parking_spaces[self.current_spot]['balance'] > 0:
                pay_amounting = True
                while pay_amounting:
                    payment_input = input(self.text['current_balance'].format(
                        balance=self.parking_spaces[self.current_spot]['balance']))

                    try:
                        payment_input = abs(float(payment_input))
                        pay_amounting = False
                    except:
                        print(self.text['invalid_selection'])

                if payment_input >= self.parking_spaces[self.current_spot]['balance']:
                    self.parking_spaces[self.current_spot]['balance'] = 0
                    print(self.text['payment_success'].format(
                        balance=self.parking_spaces[self.current_spot]['balance']))
                elif payment_input < self.parking_spaces[self.current_spot]['balance']:
                    self.parking_spaces[self.current_spot]['balance'] -= payment_input
                    print(self.text['no_leave'])

    # BC(re-write leave_garage for timer functionality)
    # JH(started leave_garage)
    def leave_garage(self):
        # set spot back to unoccupied
        # removes current_spot, duration value from the instance of the class

        # ask user if they are ready to leave

        leaving = True
        while leaving:
            choice = input(self.text['exit_query']).lower()

            if choice in self.options['yes']:
                self.parking_spaces[self.current_spot]['occupied'] = False
                del self.parking_spaces[self.current_spot]['balance']
                del self.parking_spaces[self.current_spot]['duration']
                self.current_spot = ''
                print(self.text['good_day'])
                leaving = False

            elif choice in self.options['no']:
                if self.timer > 0:
                    print(self.text['show_timer'].format(timer=self.timer))
                    self.timer -= 1
                else:
                    print(self.text['call_popo'])
                    leaving = False



# BC(set up control flow, set up try/except)
def main():
    park = ParkingGarage()

    app_running = True
    while app_running:
        entering = True
        while entering:
            user_choice = input(park.text['park_query']).lower()
            if user_choice in park.options['yes']:
                durationing = True
                while durationing:
                    parking_duration = input(park.text['duration_query'])
                    try:
                        park.take_ticket(abs(float(parking_duration)))
                        entering, durationing = False, False
                    except:
                        print(park.text['invalid_selection'])
                        
                exiting = True
                while exiting:
                    user_choice = input(park.text['leave_query']).lower()
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
