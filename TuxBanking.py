# bank simulator with credit and debit credential generators that use authentication
# through hashing and hash comparisons.

# programmed by Benjamin Saravia on February 21, 2025.

# needed imports
import time # used 33 times
import random # used 16 times
import os # used 9 times
import hashlib # used 4 times
import getpass # used 1 time

# needed lists and variables
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
user_balance = 0 # it is $0 by default
# card type 1 = CREDIT
# card type 2 = DEBIT

# creating function that creates the random credit/debit credentials
def credential_generate(desired_card):
    
    # creating four variables that will each hold 4 different combinations of digits for the card credentials to be created
    first_four_numbers = str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1))
    second_four_numbers = str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1))
    third_four_numbers = str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1))
    fourth_four_numbers = str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1)) + str(random.sample(numbers, 1))
    
    card_digits_list = [first_four_numbers, second_four_numbers, third_four_numbers, fourth_four_numbers]

    # if the user chose a CREDIT card
    if desired_card == "credit" or "c":
        
        global user_card_type # globally declaring the user_card_type variale
        user_card_type = 1
        
        print("Generating card credentials...")
        time.sleep(1.5)
        
        credit_card_credentials = [digit.replace('[', '').replace(']', '') for digit in card_digits_list]
        credit_card_credentials = "-".join(credit_card_credentials)
        credit_card_credentials = str(credit_card_credentials)
        
        global last_four_digits
        last_four_digits = credit_card_credentials[15:19] # slicing the last 4 digits of the 16-digit credential
        last_four_digits = str(last_four_digits)
        
        # getting the hash of last_four_digits for authentication into SHA 256
        global last_four_digits_hash
        last_four_digits_hash = hashlib.sha256(last_four_digits.encode()).hexdigest()
        last_four_digits_hash = str(last_four_digits_hash)
        
        print(f"\nYour credit card credentials are: {credit_card_credentials}")
        time.sleep(2)
        print(f"Card type: {user_card_type}")
        
    # if the user chose a DEBIT card
    elif desired_card == "debit" or "d":
        
        user_card_type = 2
        
        print("Generating card credentials...")
        time.sleep(1.5)
        
        debit_card_credentials = [digit.replace('[', '').replace(']', '') for digit in card_digits_list]
        debit_card_credentials = "-".join(debit_card_credentials)
        debit_card_credentials = str(debit_card_credentials)
        print(f"\nYour debit card credentials are: {debit_card_credentials}")
        time.sleep(2)
        print(f"Card type: {user_card_type}")
        
# creating the variable that prompts the user to create a 4-digit PIN to proect their CREDIT/DEBIT card
def pin_creation():
    
    # try loop for error handling
    try:
        
        while True:
        
            time.sleep(2)
            if user_card_type == 1:
            
                print("\nPlease choose your 4-digit PIN for your CREDIT card: ")
            
            elif user_card_type == 2:
            
                print("\nPlease choose your 4-digit PIN for your DEBIT card: ")
            
            global user_PIN # declaring user_PIN as a global variable
            user_PIN = int(input('> '))
            user_PIN = str(user_PIN)
        
            if len(user_PIN) != 4:
            
                time.sleep(1)
                print("\nSYSTEM ERROR: Your PIN must be 4 digits long. Please try again.")
            
                continue

            while True:
            
                # creating a SHA 256 hash for the user's PIN for authentication
                global user_PIN_hash
                user_PIN_hash = hashlib.sha256(user_PIN.encode()).hexdigest()
                user_PIN_hash = str(user_PIN_hash)
                
                time.sleep(1.2)
                print("SYSTEM: PIN created.")
                print("\nPIN: ****")
                time.sleep(1)
            
                # setting the balance for the account
                deposit_decision = input("\nWould you like to make an initial deposit? (y / n): ")
                
                if deposit_decision.lower() == "y":
                    
                    user_deposit = int(input('Deposit amount: >$'))
                    global user_balance
                    user_balance += user_deposit
                    time.sleep(1)
                    print(f"SYSTEM: {user_deposit} has been deposited to {username}'s account.")
                    time.sleep(1)
                    
                    break
                    
                else:
                
                    print("\nSYSTEM: No initial deposit was made.")
                    time.sleep(1)
                    break
            
    # if the user inputs something invalid        
    except ValueError:
        
        print("Please enter a valid input.")
        
        pin_creation()  
        
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n")
        print("SYSTEM: CTRL + C detected.")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing the simulation...")
            
        else:
            
            print("\nRe-opening the simulation...")
            print("\n")
            time.sleep(1.5)
            os.system('clear')
            
            pin_creation()
        
def verification():
    
    # declare variables for retry counts
    x = 0  # Retry count for card digits
    y = 0  # Retry count for PIN
    z = 0  # Retry count for username

    try:
        
        # username verification + retry loop
        while z < 2:
            
            os.system('clear')
            time.sleep(1.5)
            print("We will now have you log in again to confirm your bank identity.")

            # Username verification
            username_verification = input("Please enter your account's USERNAME: ")
            username_verification = str(username_verification)

            if username_verification != username:
                
                time.sleep(1.2)
                print("\nSYSTEM: That username does not exist in our system.")
                time.sleep(1.2)
                print("Please input a real username.")
                time.sleep(1.2)
                z += 1
                
                continue
            
            else:
                
                # once username is confirmed, proceed to card digits verification
                while x < 2:
                    
                    time.sleep(1)
                    if user_card_type == 1:
                        
                        print("\nBelow, please enter the last 4 digits of your CREDIT card:")
                        
                    elif user_card_type == 2:
                        
                        print("\nBelow, please enter the last 4 digits of your DEBIT card: ")

                    credential_confirmation = input('>')
                    credential_confirmation_hash = hashlib.sha256(credential_confirmation.encode()).hexdigest()

                    if credential_confirmation_hash != last_four_digits_hash:
                        
                        time.sleep(1.2)
                        print(f"\nSYSTEM: ERROR. The last 4 digits do not match with the last 4 on {username_verification}'s CARD.")
                          
                        time.sleep(1.5)
                        print("The verification has failed. Please try again.")
                        time.sleep(1.5)
                        
                        x += 1
                        continue
                    
                    else:
                        
                        # card digits are correct, proceed to PIN verification
                        while y < 2:
                            
                            time.sleep(1.2)
                            
                            if user_card_type == 1:
                                
                                print("\nSYSTEM: The last 4 digits of your CREDIT card have been identified.")
                                
                            elif user_card_type == 2:
                                
                                print("\nSYSTEM: The last 4 digits of your DEBIT card have been identified.")

                            print("Please confirm the 4-digit PIN for the account below: ")
                            print("NOTE: your input will not show [for security].")
                            PIN_confirmation = getpass.getpass('>')
                            PIN_confirmation_hash = hashlib.sha256(PIN_confirmation.encode()).hexdigest()

                            if PIN_confirmation_hash != user_PIN_hash and y < 2:
                                
                                time.sleep(1.2)
                                print("SYSTEM: ERROR. We could not confirm your PIN. Please try again.")
                                y += 1
                                time.sleep(1)
                                
                                continue
                            
                            else:
                                
                                # PIN is correct, verification successful
                                time.sleep(1.5)
                                print("\nSYSTEM: PIN CONFIRMED!")
                                time.sleep(1)
                                os.system('clear')

                                print(f"\nWelcome, {username}!")
                                print(f"Account: ****-****-****-{last_four_digits}")
                                print(f"Balance: ${user_balance}")
                                print("\n🐧")
                                
                                return  # exit the function after successful verification

                        # if PIN verification fails twice
                        if y == 2:
                            
                            os.system('clear')
                            time.sleep(1.5)
                            print("\nSYSTEM: You have failed 2 verification attempts.")
                            print("The simulation will now be terminated. Thank you for banking with TUX.")
                            print("\n🐧")
                            
                            return

                # if card digits verification fails twice
                if x == 2:
                    
                    os.system('clear')
                    time.sleep(1.5)
                    print("\nSYSTEM: You have failed 2 verification attempts and will now be locked out.")
                    print("The simulation will now be terminated. Thank you for banking with TUX.")
                    print("\n🐧")
                    
                    return

        # if username verification fails twice
        if z == 2:
            
            os.system('clear')
            time.sleep(1.5)
            print("\nSYSTEM: You have failed 2 verification attempts.")
            print("The simulation will now be terminated. Thank you for banking with TUX.")
            print("\n🐧")
            
            return

    except ValueError:
        
        print("Please enter a valid input.")
        verification()

    except KeyboardInterrupt:
        
        print("\nSYSTEM: CTRL + C detected.")
        error_resolve = input("Was this intentional? (Y / N): >")

        if error_resolve.upper() == "Y":
            
            print("\nClosing the simulation...")
            
        else:
            
            print("\nRe-opening the simulation...")
            time.sleep(1.5)
            os.system('clear')
            
            verification()   
                 
# defining the main function
def main():
    
    # try loop for error handling
    try:
        
        os.system('clear')
        print("\n")
        print("🐧                TUX BANKING                  🐧")
        time.sleep(2)
    
        # declaring the user's bank name as a global variable
        global username
        username = input("\nPlease choose a USERNAME for your new bank account: ")
        time.sleep(2)
        print(f"Hello, {username}.")
        time.sleep(1.2)
    
        card_decision = input("\nDo you want a CREDIT (c) or DEBIT (d) card?: ")
        card_decision = card_decision.lower()
    
        credential_generate(card_decision)
        
    # if the user inputs something invalid        
    except ValueError:
        
        print("Please enter a valid input.")
        
        main()  
        
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n")
        print("SYSTEM: CTRL + C detected.")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing the simulation...")
            
        else:
            
            print("\nRe-opening the simulation...")
            print("\n")
            time.sleep(1.5)
            os.system('clear')
            
            main()
    
# calling all of the functions made
main()
pin_creation()
verification()
