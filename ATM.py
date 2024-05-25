pin = 0
bal = 0

def set_pin():
    global pin
    while True:
        pin1 = int(input('Enter a 4 digit pin: '))
        pin2 = int(input('Confirm your pin: '))
        if pin1 == pin2:
            print('Pin set successful...')
            pin = pin1
            break
        else:
            print("Pins don't match. Enter the correct pin.")

def deposit():
    global bal
    in_pin = int(input('Enter your 4 digit pin: '))
    if in_pin == pin:
        amt = int(input('Enter amount to deposit: '))
        bal += amt
        print(f'Amount of {amt} Rs. deposited')
    else:
        print('Incorrect pin')

def withdraw():
    global bal
    in_pin = int(input('Enter your 4 digit pin: '))
    if in_pin == pin:
        amt = int(input('Enter amount to withdraw: '))
        if amt <= bal:
            bal -= amt
            print(f'Amount of {amt} Rs. withdrawn')
        else:
            print('Insufficient balance')
    else:
        print('Incorrect pin')

def check_bal():
    in_pin = int(input('Enter your 4 digit pin: '))
    if in_pin == pin:
        print(f'Available balance in your A/C: {bal}')
    else:
        print('Incorrect pin')

while True:
    print('\nATM Menu:')
    print('1. Set PIN')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Check Balance')
    print('5. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        set_pin()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_bal()
    elif choice == 5:
        print('Thank you for using the ATM!')
        break
    else:
        print('Invalid choice. Please try again.')
