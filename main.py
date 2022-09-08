# Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
# Tasks:
# 1.   	Prompt user for a pin code
# 2.   	If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.
# 3.   	Set account balance to 100.
# 4.   	Now we need to simulate cash withdrawal
# 5.   	Accept the withdrawal amount
# 6.   	Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
# 7.   	However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.



user = {
    'pin': 1259,
'balance': 100}




def pin():
    count = 0
    while count < 3:
        try:
            upin = int(input("please type your pin: "))
        except ValueError:
            print("A pin is 4 digits , try again")
            count += 1
        else:
            if upin != user['pin']:
                print("Pin incorrect. Try again")
                count += 1
            else:
                withdraw()
    if count > 3:
        print("You have exceeded the number of tries")
        print("Your card is now blocked, please call you bank to unblock")
        exit(0)

def withdraw():
    try:
        amount = int(input("How much money do you want to withdraw?: "))
    except ValueError:
        print('Please try a correct amount')
    else:
        if amount > user['balance']:
            print('You dont have enough money in your account')
            exit(0)
        else:
            user['balance'] -= amount
            print(f'{amount} has been succesfully withdrawn, thank you.')
    return(amount)
pin()

##test units

class AtmTest(unittest.TestCase):

    def correct_amount(self):
        val = 30
        self.assertLessEqual(val,balance)

    def invalid(self):
        val = afhgsrt
        self.assertIsInstance(val, int)

    def more(self):
        val = 150
        self.assertGreater(val,balance)



if __name__ == '__main__':
    unittest.main()


    pass