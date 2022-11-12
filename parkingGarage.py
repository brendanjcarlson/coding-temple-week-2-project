from numpy import random

# JH(created text and options dictionaries and implemented throughout code)
text = {
    'spot_assign': "\nYou've been assigned spot {spot} and your balance is {price}.",
    'garage_full': "\nIt appears all spots are currently taken. Apologies for the inconvenience.",
    'pay_balance': "\nAre you going to pay your balance?\n(Y)es | (N)o\n",
    'no_leave': "\nYou can't leave until you pay your balance.",
    'show_balance': "\nYour balance is still {balance}. Please pay your balance before leaving.",
    'park_query': "\nWould you like to park?\n(Y)es | (N)o\n",
    'exit_query': "\nWould you like to exit?\n(Y)es | (N)o\n",
    'query_error': "\nInvalid selection, please select:\n(Y)es | (N)o\n",
    'payment_success': "\nYour payment was received and your balance is {balance}. You have 15 minutes to leave the garage. Thank you!",
    'good_day': "\nHave a good day!"
}

options = {
    'yes': ['y', 'yes', 'ye', 'yeah', 'yea', 'yeh', 'ya', 'yah', '(y)es', '(y)'],
    'no': ['n', 'no', 'nah', 'na', 'nay', '(n)o', '(n)']
}


# BC(layed out format and ticket/spot assign) 
# JH(updated parking_spaces, removed current_ticket)
class ParkingGarage:
    parking_spaces = {
        'A1': {'occupied': True}, 
        'A2': {'occupied': True}, 
        'A3': {'occupied': False}, 
        'A4': {'occupied': True}, 
        'A5': {'occupied': False}, 
        'A6': {'occupied': True}, 
        'A7': {'occupied': True}, 
        'A8': {'occupied': True}, 
        'A9': {'occupied': False}, 
        'A10': {'occupied': True}, 
        'B1': {'occupied': False}, 
        'B2': {'occupied': False}, 
        'B3': {'occupied': False}, 
        'B4': {'occupied': True}, 
        'B5': {'occupied': False}, 
        'B6': {'occupied': True}, 
        'B7': {'occupied': False}, 
        'B8': {'occupied': False}, 
        'B9': {'occupied': False}, 
        'B10': {'occupied': False}, 
        'C1': {'occupied': False}, 
        'C2': {'occupied': False}, 
        'C3': {'occupied': False}, 
        'C4': {'occupied': True}, 
        'C5': {'occupied': False}, 
        'C6': {'occupied': False}, 
        'C7': {'occupied': False}, 
        'C8': {'occupied': False}, 
        'C9': {'occupied': True}, 
        'C10': {'occupied': True}, 
    }
    price = 5


    # BC(layed out logic) 
    # JH(worked on take_ticket, leave_garage) 
    # JA(worked on pay_for_parking, updated take_ticket)
    def __init__(self, current_spot=""):
        self.current_spot= current_spot
        

    def take_ticket(self):
        # assign user a spot
        # update their balance with cost of ticket

        # Loops over dict for occupied spots each time a ticket is taken
        count = 0
        for spot in self.parking_spaces:
            if self.parking_spaces[spot]['occupied']:
                count +=1
        
        # Assigning a user first avail. spot unless full, sets spot to occupied, sets balance to price
        for spot in self.parking_spaces:
            if not self.parking_spaces[spot]['occupied']:
                self.parking_spaces[spot]['occupied'] = True
                self.current_spot = spot
                self.parking_spaces[spot]['balance'] = self.price
                print(text['spot_assign'].format(spot=spot, price=self.price))
                break
            
            elif count == 30:
                print(text['garage_full'])

    
    def pay_for_parking(self):
        # update balance and paid flag
        # check if balance is paid
        # if no pay balance
        # update balance if they pay
        # else dont let them leave
        
        # Checks for balance and asks user to pay.
        # If balance is 0, let them leave. If not, ask them to pay again.
        while self.parking_spaces[self.current_spot]['balance'] > 0:
            user_input= input(text['pay_balance']).lower()
            if user_input in options['yes']:
                self.parking_spaces [self.current_spot]['balance'] = 0
                print(text['payment_success'].format(balance=self.parking_spaces[self.current_spot]['balance']))
            else : 
                print(text['no_leave'])
                
    # Sets spot back to not occupied when leaving garage
    def leave_garage(self):
        # in a while loop
        # if user has paid for parking:
        #   allow them to leave
        # else:
        #   continue begging them to pay

        self.parking_spaces[self.current_spot]['occupied'] = False


# BC(set up control flow)
def main():
    park = ParkingGarage()

    app_running = True
    while app_running:
        entering = True
        while entering:
            user_choice = input(text['park_query']).lower()
            if user_choice in options['yes']:
                entering = False
                park.take_ticket()
            elif user_choice in options['no']:
                print(text['good_day'])
                entering, app_running = False, False
            else:
                continue

        exiting = True
        while exiting:
            user_choice = input(text['exit_query']).lower()
            if user_choice in options['yes']:
                park.pay_for_parking()
                # if paid, leave
                park.leave_garage()
                exiting, app_running = False, False
            elif user_choice in options['no']:
                continue
            else:
                print(text['query_error'])


main()

