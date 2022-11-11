from numpy import random

# BC(layed out format and ticket/spot assign) JH(updated parking_spaces, removed current_ticket)
class ParkingGarage:
    parking_spaces = {
        'A1': {'occupied': True}, 
        'A2': {'occupied': True}, 
        'A3': {'occupied': False}, 
        'A4': {'occupied': True}, 
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
    price = 5

    # BC(layed out logic) JH(worked on take_ticket, leave_garage)
    def __init__(self):
        pass

    def take_ticket(self):
        # assign user a spot
        # update their balance with cost of ticket

        # for k, v in self.parking_spaces.items():
        #     if not v:
        #         current_ticket[k] = 


        #     if num not in current_ticket and parking_spaces[]:
        #         current_ticket[num] = num

        count = 0
        for spot in self.parking_spaces:
            if not self.parking_spaces[spot]['occupied']:
                self.parking_spaces[spot]['occupied'] = True
                self.parking_spaces[spot]['balance'] = self.price
                print(f"You've been assigned spot {spot} and your balance is {self.price}.")
                break
            
            else: 
                count += 1
                if count == 30:
                    print("It appears all spots are taken. Sorry for the inconvenience.")




    def pay_for_parking(self):
        # update balance and paid flag
        # check if balance is paid
        # if no pay balance
        # update balance if they pay
        # else dont let them leave
        pass

    def leave_garage(self, spot):
        # in a while loop
        # if user has paid for parking:
        #   allow them to leave
        # else:
        #   continue begging them to pay

        while self.parking_spaces[spot]['balance'] != 0:
            print(f"Your balance is still {self.parking_spaces[spot]['balance']}. Please pay your balance before leaving.")         

        self.parking_spaces[key]['occupied'] = False

        for key in self.parking_spaces[spot]:
            if key != 'occupied':
                del self.parking_spaces[spot][key]


def main():

    park = ParkingGarage()

    app_running = True
    while app_running:
        # BC(set up control flow)
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
        # BC(set up control flow)
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


# main()

building = ParkingGarage()
building.take_ticket()
building.take_ticket()
building.take_ticket()
building.take_ticket()