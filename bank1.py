class Customer:
    last_id = 0
    def __init__(self, cid, firstname, surname):
        self.cid = cid
        self.firstname = firstname
        self.surname = surname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer created [{self.id}, {self.cid}, {self.firstname}, {self.surname}]'

class Account:
    last_id = 1000
    def __init__(self, cid, customer):
        self.cid = cid
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        
    def __repr__(self):
        return f'Account created [{self.id}, {self.cid}, {self.customer}, {self._balance}]'
    
class Bank:
    def __init__(self):
        self.customer_list = dict()
        self.account_list = dict()
    
    def create_customer(self, cid, firstname, surname):
        if cid in self.customer_list:
            raise ExistingCustomerException(f'Existing Customer with ID {cid}')
        c = Customer(cid, firstname, surname)
        self.customer_list[c.cid] = [c.id, c.cid, c.firstname, c.surname]
        return c

    def create_account(self, cid, customer):
        if cid not in self.customer_list:
            raise NonExistingCustomerException(f'Can not find the Customer {cid}')
        a = Account(cid, customer)
        self.account_list[a.id] = [a.id, a.cid, a.customer, a._balance]
        return a

    def find_account(self, id):
        if id not in self.account_list:
            raise NonExistingAccountException(f'Can not find Account with ID {id}')
        return f'Found Account {self.account_list[id]}'

    def transfer(self, from_account_id, to_account_id, amount):
        if (type(amount) != int) or (amount < 0):
            raise InvalidAmountException(f'Invalid amount {amount}')
        if from_account_id not in self.account_list:
            raise NonExistingAccountException(f'Transfer Account is not valid {from_account_id}')
        if to_account_id not in self.account_list:
            raise NonExistingAccountException(f'Receive Account is not valid {to_account_id}')
        tmp_balance = self.account_list[from_account_id][3]
        if amount > tmp_balance -5:
            raise InsufficientFundsException(f'Not enough funds {tmp_balance}')
        self.account_list[from_account_id][3] -= amount
        self.account_list[to_account_id][3] += amount
        return f'Successfully transfered from {from_account_id} to {to_account_id} amount {amount}'
    
    def deposit(self, id, amount):
        if (type(amount) != int) or (amount < 0):
            raise InvalidAmountException(f'Invalid amount {amount}')
        if id not in self.account_list:
            raise NonExistingAccountException(f'Can not find the Account {id}')
        self.account_list[id][3] += amount
        return f'Deposit done amount {amount} --> Account balance {self.account_list[id]}'
        
    def charge(self, id, amount):
        if (type(amount) != int) or (amount < 0):
            raise InvalidAmountException(f'Invalid amount {amount}')
        if id not in self.account_list:
            raise NonExistingAccountException(f'Can not find the Account {id}')
        tmp_balance = self.account_list[id][3]
        if amount > tmp_balance - 5:
            raise InsufficientFundsException(f'Not enough funds {tmp_balance}')
        self.account_list[id][3] -= amount
        return f'Charge done amount {amount} --> Account balance {self.account_list[id]}'
            
    def __repr__(self):
        return f'Bank contain Customer: {len(self.customer_list)} and Account: {len(self.account_list)}'
    
class AccountTransactions:
    def __init__(self):
        self.transations_list = dict()
    
    def put_transaction(self, id, transaction):
        self.id = id
        if id not in self.transations_list:
            self.transations_list[id] = transaction
        else: self.transations_list[id] += transaction
        return f'{transaction} put successfully to transaction list'
    
    def get_transaction(self, id):
        self.id = id
        if id not in self.transations_list:
            raise EmptyTransactionException(f'Do not have any transaction for account {id}')
        return self.transations_list[id]

    def __repr__(self):
        return f'{len(self.transations_list)} accounts have transaction.'
    
class BankException(Exception):
    pass

class ExistingCustomerException(BankException):
    pass

class InvalidAmountException(BankException):
    pass

class InsufficientFundsException(BankException):
    pass

class NonExistingCustomerException(BankException):
    pass

class NonExistingAccountException(BankException):
    pass    

class EmptyTransactionException(BankException):
    pass

import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

checking = True
B = Bank()
T = AccountTransactions()

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
                            print('Continue [Y/N]: ', end = '')
                            cnt = input()
                            if cnt == 'N': checking = False
                except BankException as ie:
                    print(f'{ie}')
                    print('Continue [Y/N]: ', end = '')
                    cnt = input()
                    if cnt == 'N': checking = False     
            case 4:
                4
            case 6:
                print('6. Confirm quit [Y/N]: ', end = '')
                tmp = input()
                if tmp == 'Y': checking = False
    except BankException as ie:
        print(f'Something went wrong {ie}')
        print('Continue [Y/N]: ', end = '')
        cnt = input()
        if cnt == 'N': checking = False