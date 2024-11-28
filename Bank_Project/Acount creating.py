import pyfiglet as pfg
import pandas as pd
import pyinputplus as pin
import sys

def accountNo() :
    df = pd.read_csv("Bank_Project\Account_creating_Details.csv")
    Ac = df.tail(1)["AccountNo"][list(df.index.values)[-1]] +1
    return int(Ac)

def PinGenerater():
    check = True
    while check:
        pinNo = pin.inputPassword("Generate a PIN: ")
        confPin = pin.inputPassword("Confirm PIN: ")
        if pinNo == confPin:
            check = False
    return confPin
    # df = pd.read_csv("Bank_Project\Account_creating_Details.csv")
    # m = list(df.index.values)[-1]
    # df["AccountPin"][list(df.index.values)[-1]] = confPin

def createAccount():
    Details = []
    Enter = pin.inputStr("Enter your adhar number: ")
    Details.append(Enter)
    Enter = pin.inputStr("Enter your phone No. : ")
    Details.append(Enter)
    Enter = pin.inputStr("Enter your Full Name : ")
    Details.append(Enter)
    Enter = pin.inputDate("Enter D.O.B (MM/DD/YYYY): ")
    Details.append(Enter)
    AcNo = accountNo()
    print(f"------Your Account Number is: {AcNo}------",)
    AccPin = PinGenerater()

    Record = pd.DataFrame({
        "AdharNo":[Details[0],],
        "MobileNo":[ Details[1],],
        "Name": [Details[2],],
        "DOB": [Details[3],],
        "AccountNo" : [AcNo,],
        "AccountPin" : [AccPin,],
        "Balance" : [0,]
    })
    Record.to_csv("Bank_Project\Account_creating_Details.csv",mode='a',index=False,header=False)
    print("--------------Account Created Successfully :-) ---------------\n")


def ABCbank():
    welcm = pfg.figlet_format("ABC Bank")
    print(welcm)
    print("---------------------------Hare Krishna-------------------------\n")
    check = pin.inputYesNo("Do you want to create an Account (yes/no): ")       
    while check=="yes":
            createAccount()
            check = pin.inputYesNo("Do you want to create an Account (yes/no): ")

def BA():
    
    chk = True
    while chk:
        print("1) ATM")
        print("2) Bank")
        print("0) Exit")
        option = pin.inputNum("Which one you want to use: ")
        if option==1:
            ATM()
            # chk=False
        elif option==2:
            ABCbank()
            # chk=False
        elif option==0:
            SysOut()


def ATM():
    atmBanner = pfg.figlet_format("A T M")
    print(atmBanner)
    accno = pin.inputNum("Enter Account number: ")
    pn = pin.inputPassword("Enter PIN: ")
    # dic = {"AccNo":accno,"PIN" : pn}
    history = []
    while True:
        print("1) Deposit ")
        print("2) Withdrawl ")
        print("3) Transfer ")
        print("4) PIN Change ")
        print("5) Balance check ")
        print("6) History")
        print("7) Back ")
        print("0) Exit \n")
        query = pin.inputNum("Choose a number : ")
        df = pd.read_csv("Bank_Project\Account_creating_Details.csv")
        if query==1:
            #Deposit
            cash = pin.inputNum("Entre your amount: ")
            ac = df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"].values[0]
            df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"] = ac + cash
            df.to_csv("Bank_Project\Account_creating_Details.csv",index=False)
            print(f"-----Succesfully Deposited {cash} Rupee :-) -----\n")
            status = f"Deposited: {cash}\n"
            history.append(status)
        elif query==2:
            #Withdrawl
            cash = pin.inputNum("Entre your amount you want: ")
            ac = df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"].values[0]
            if cash <= ac:
                print(f"======Take your {cash} Rupee======\n")
                df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"] = ac - cash
                df.to_csv("Bank_Project\Account_creating_Details.csv",index=False)
                status = f"Withdrawl: {cash}\n"
                history.append(status)
            else:
                print("----You have Not that much amount to Withdraw :-( -----\n")
        elif query ==3:
            #Transfer
            cash = pin.inputNum("Entre The amount you want to Transfer: ")
            ac = df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"].values[0]
            if cash<= ac:
                frnAccno = pin.inputNum("Enter the Account No. to which you transfer: ")
                df.loc[df["AccountNo"]==frnAccno,"Balance"] = df.loc[df["AccountNo"]==frnAccno,"Balance"].values[0] + cash
                df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"] = ac - cash
                df.to_csv("Bank_Project\Account_creating_Details.csv",index=False)
                print("----Transfer Successfull :-) -----\n")
                status = f"Transfered: {cash} to AccNo: {frnAccno}\n"
                history.append(status)
            else:
                print("-----You have Not that much money to Transfer :-( -----\n")
        elif query==4:
            #PIN Change
            newPin = PinGenerater()
            df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"AccountPin"] = newPin
            pn = newPin
            df.to_csv("Bank_Project\Account_creating_Details.csv",index=False)
            print("-----PIN Successfully changed :-) -----\n")
            status = "PIN Changed\n"
            history.append(status)
        elif query==5:
            #Balance check
            ac = df.loc[(df["AccountNo"]==accno) & (df["AccountPin"]==pn),"Balance"].values[0]
            print(f"Current Balance: {ac}\n")
            status = "Balance Check\n"
            history.append(status)
        elif query==6:
            #History
            print("--------ATM History---------\n")
            print("".join(history))
        elif query == 7:
            return
        elif query == 0:
            SysOut()
            
def SysOut():
    print("\n        +_+ Program OVER -_-!     \n")
    sys.exit()

print("---------------------------Hare Krishna-------------------------\n")
# AcountDetails = ["AdharNo","MobileNo","PanNo","Name","DOB" ]
ABCbank()
print("\n---------------------------Hare Krishna-------------------------\n")
BA()






    






