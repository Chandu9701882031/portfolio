# Bank Application using Dictionary

#Ditionary to store customer data

bank_accounts={}

def create_account():
  acc_number=input("Enter Account Number:")
  if acc_number in bank_accounts:
     print("Account already exists:")
  else:
    name=input("Enter account holder_name:")
    bank_accounts[acc_number]={"name":name,"balance":0}
    print(f"Account Created for {name} with account number {acc_number}")

def deposit():
  acc_number=input("Enter account Number:")
  if acc_number in bank_accounts:
   amount=float(input("Enter amount to deposite:"))
   if amount>0:
        bank_accounts[acc_number]["balance"]+=amount
        print(f"Deposited {amount}.Current Balance:{bank_accounts[acc_number]['balance']}")
   else:
      print("Invaild deposite amount")
  else:
   print("Account not found")

def withdraw():
  acc_number=input("Enter account Number:")
  if acc_number in bank_accounts:
   amount=float(input("Enter amount to withdraw:"))
   if 0<amount<=bank_accounts[acc_number]["balance"]:
        bank_accounts[acc_number]["balance"]-=amount
        print(f"Withdrawn {amount}.Current Balance:{bank_accounts[acc_number]['balance']}")
   else:
      print("Insuffient funds or Invalid amount")
  else:
   print("Account not found")


def checkbalance():
  acc_number=input("Enter account Number:")
  if acc_number in bank_accounts:
      print(f"Account Holder:{bank_accounts[acc_number]['name']}")
      print(f"Current Balance:{bank_accounts[acc_number]['balance']}")
  else:
   print("Account not found")





def menu():
 while True:
   print("\n---Bank Menu---")
   print("1.Create Account")
   print("2.Deposit Money")
   print("3.Withdraw money")
   print("4.Checkbalance")
   print("5.Exit")
   choice=input("Enter your choice(1-5):")
   if choice=='1':
     create_account()
   elif choice=='2':
      deposit()
   elif choice=='3':
      withdraw()
   elif choice=='4':
     checkbalance()
   elif choice=='5':
      print("Thankyou for using the applications")
      break
   else:
      print("Invalid choice")



menu()
   
