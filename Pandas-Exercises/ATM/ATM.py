#####################
##### ATM ###########
#####################
#The following program simulates an ATM,
#using a csv file as the data source
#and destination.
#####################
import csv
import pandas as pd


df = pd.read_csv('ATM.csv')   #Loads the csv data to a local database.


#Retrieval function for balance.
def checkBalance(userID):
    balance = df.loc[df['UserID'] == userID, 'Balance'].values[0]
    return balance

#The following functions verify the validity of responses,
#and return an appropriate response.

def isValidWithdraw(value, balance):
    if str(value).isdigit() == False:
        return False
    if (int(value)%10==0)== False:
        return False
    if (int(value) < balance) == False:
        print("Insufficient Balance")
        return False
    if (int(value) > 9) == False:
        return False
    return True

def isValidDeposit(value):
    if value.isnumeric() == False:
        return False
    if (float(value) > 0) == False:
        return False
    return True

def checkWithdraw(selection, balance):
    if selection == '1':
        value = 10
    elif selection == '2':
        value = 20
    elif selection == '3':
        value = 50
    elif selection == '4':
        value = 100
    elif selection == '5':
        value = str(input("Custom withdrawals must be multiples of 10. Minimum £10.\nEnter custom amount here: "))
    else:
        print("Invalid Selection. Returning to menu.")
        return False, 0
    if isValidWithdraw(value, balance):
        return True, int(value)
    else:
        print("Invalid withdrawal. Returning to menu.")
        return False, 0

                    

def checkCard(cardNumber):
    if cardNumber.isdigit()==False:
        return False, '000', '000'
    check = df.loc[df['CardNumber'] == int(cardNumber), ['UserID','PIN']]
    if not check.empty:
        flag = True
        userID = check.iloc[0]['UserID']
        PIN = check.iloc[0]['PIN']
    else:
        flag = False
        userID = PIN = '000'
    return flag, userID, PIN

#These next two functions embody the actions of the ATM,
#and use the above validity functions within them.

def deposit(userID, balance):
    value = str(input("Please enter a valid amount to deposit: "))
    if isValidDeposit(value):
        balance+=float(value)
        df.loc[df['UserID'] == userID, 'Balance'] = balance
        print("Deposit successful. Returning to menu.")
    else:
        print("Invalid entry value. Returning to menu.")
    return

def withdraw(userID, balance):
    print("Please choose an amount to withdraw:\n[1] - £10\n[2] - £20\n[3] - £50\n[4] - £100\n[5] - Custom Amount")
    selection = str(input("Enter key here: "))
    valid, value = checkWithdraw(selection, balance)
    if valid:
        balance-=value
        df.loc[df['UserID'] == userID, 'Balance'] = balance
        print("Withdrawal successful. Returning to menu.")
    return


#ATM Loops

print("Welcome to the ATM!")
validCard = False
while validCard == False:
    cardNumber = str(input("Please enter your card number: "))
    validCard, userID, PIN = checkCard(cardNumber)
    if validCard:
        for i in range(4):
            if i<3:
                message = "Please enter your PIN("+str(3-i)+" attempts remaining): "
                attPIN = str(input(message))
                if attPIN == str(PIN):
                    print("PIN Successful! Welcome user ",userID,"!!")
                    break
            else:
                print("No attempts remaining.\nThe authorities are on their way.")
                validCard = False

running = True                
while running:
    balance = checkBalance(userID)
    print("Your current balance is",balance,".")
    print("Please select an action:\n[1] - Deposit\n[2] - Withdraw\n[3] - Exit")
    select = str(input("Enter selection here: "))
    if select == '1':
        deposit(userID, balance)
    elif select == '2':
        withdraw(userID, balance)
    elif select == '3':
        print("Exiting. Thank you.")
        running = False
    else:
        print("Invalid selection.")


#Writes the data back to the CSV file
#df.to_csv('ATM.csv', index=False)






    
                    
        


    
