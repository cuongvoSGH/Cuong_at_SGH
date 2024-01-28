# CUONG VO - 131116 
# VIRTUAL BANK

import bank
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

checking = True
B = bank.Bank()
T = bank.AccountTransactions()

while checking ==True:
    clear()
    print('======================== AUTO BANK ========================')
    print('1. Register for client')
    print('2. Create Account')
    print('3. Transaction')
    print('4. Find')
    print('5. Account Log')
    print('6. Quit')
    print('===========================================================')
    print('Please choose the option: ', end = '')
    n = int(input())
    try:
        match n:
            case 1:
                clear()
                print('======================== REGISTER ========================')
                print('Input First Name: ', end ='')
                first_name = input()
                print('Input Surname: ', end ='')
                last_name = input()
                print('Customer ID (ID, Passport): ', end = '')
                c_id = input()
                tmp = B.create_customer(cid=c_id, firstname=first_name, surname=last_name)
                print(tmp)
                print('Continue [Y/N]: ', end ='')
                cnt = input()
                if cnt == 'N': checking = False
            case 2:
                clear()
                print('======================== CREATE ACCOUNT ========================')
                print('Input Full Name: ', end ='')
                full_name = input()
                print('Input Customer ID (ID, Passport): ', end ='')
                c_id = input()
                tmp = B.create_account(cid=c_id, customer=full_name)
                print(tmp)
                trans_text = f'Create account No. {tmp.id}'
                transaction = [trans_text]
                trans_put = T.put_transaction(id=tmp.id, transaction=transaction)
                print('Continue [Y/N]: ', end = '')
                cnt = input()
                if cnt == 'N': checking = False
            case 3:
                clear()
                print('======================== TRANSACTION ========================')
                print('1. Deposit')
                print('2. Charge')
                print('3. Transaction')
                print('=============================================================')     
                print('Please choose the option: ', end = '')
                n1 = int(input())
                try:
                    match n1:
                        case 1:
                            clear()
                            print('======================== DEPOSIT ========================')
                            print('Input Account Number: ', end='')
                            acc_id = int(input())
                            print('Input amount: ', end = '')
                            amount = int(input())
                            tmp = B.deposit(id=acc_id, amount=amount)
                            print(tmp)
                            trans_text = f'Deposit to account {acc_id} amount {amount}'
                            transaction = [trans_text]
                            trans_put = T.put_transaction(id=acc_id, transaction=transaction)
                            print('Continue [Y/N]: ', end = '')
                            cnt = input()
                            if cnt == 'N': checking = False
                        case 2:
                            clear()
                            print('======================== CHARGE ========================')
                            print('Input Account Number: ', end='')
                            acc_id = int(input())
                            print('Input amount: ', end = '')
                            amount = int(input())
                            tmp = B.charge(id=acc_id, amount=amount)
                            print(tmp)
                            trans_text = f'Charge from account {acc_id} amount {amount}'
                            transaction = [trans_text]
                            trans_put = T.put_transaction(id=acc_id, transaction=transaction)
                            print('Continue [Y/N]: ', end = '')
                            cnt = input()
                            if cnt == 'N': checking = False
                        case 3:
                            clear()
                            print('======================== TRANSFER ========================')
                            print('Input Transfer Account Number: ', end='')
                            from_id = int(input())
                            print('Input Receive Account Number: ', end='')
                            to_id = int(input())
                            print('Input amount: ', end = '')
                            amount = int(input())
                            tmp = B.transfer(from_account_id=from_id, to_account_id=to_id, amount=amount)
                            print(tmp)
                            trans_text = f'Transfer to account {to_id} amount {amount}'
                            transaction = [trans_text]
                            trans_put = T.put_transaction(id=from_id, transaction=transaction)        
                            trans_text = f'Receive from account {from_id} amount {amount}'
                            transaction = [trans_text]
                            trans_put = T.put_transaction(id=to_id, transaction=transaction)                     
                            print('Continue [Y/N]: ', end = '')
                            cnt = input()
                            if cnt == 'N': checking = False
                except bank.BankException as ie:
                    print(f'{ie}')
                    print('Continue [Y/N]: ', end = '')
                    cnt = input()
                    if cnt == 'N': checking = False   
            case 4:
                clear()
                print('======================== FIND ========================')
                print('Input Account ID: ', end='')
                id = int(input())
                tmp = B.find_account(id=id)
                print(tmp)
                print('Continue [Y/N]: ', end = '')
                cnt = input()
                if cnt == 'N': checking = False
            case 5:
                clear()
                print('======================== ACCOUNT LOG ========================')
                print('Input Account ID: ', end='')
                id = int(input())
                tmp = T.get_transaction(id= id)
                for i in tmp:
                    print(i)
                print('Press any button to continue ....')
                input()
                print('Continue [Y/N]: ', end = '')
                cnt = input()
                if cnt == 'N': checking = False                
            case 6:
                print('6. Confirm quit [Y/N]: ', end = '')
                tmp = input()
                if tmp == 'Y': checking = False
    except bank.BankException as ie:
        print(f'{ie}')
        print('Continue [Y/N]: ', end = '')
        cnt = input()
        if cnt == 'N': checking = False
    if checking == False: 
        print(B)
        print('================= THANK YOU =================')