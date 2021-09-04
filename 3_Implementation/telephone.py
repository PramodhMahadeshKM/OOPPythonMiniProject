'''
This is the source file for the telephone project
'''
import re


class Customer:

    'Parent class'

    def __init__(self,idn=None,name=None,email=None,number=None):
        '''Parent class constructor'''
        self.idn=idn
        self.name=name
        self.email=email
        self.number=number

    def update_email(self,new_email):
        '''Function to update mail id'''
        self.email=new_email
        print('Updated successfully!\n')

    def display(self):
        '''Function to display info'''
        print(f'ID = {self.idn}\nName = {self.name}')
        print(f'Email = {self.email}\nPhone no. = {self.number}')

class PrepaidCustomer(Customer):

    '''Prepaid child class'''

    def __init__(self,idn=None,name=None,email=None,number=None,balance=None):
        '''Prepaid class constructor'''
        super().__init__(idn,name,email,number)
        self.balance=balance

    def read_data(self):
        '''Function to get data of the user from backend(.txt file here)'''
        file = open('Prepaid.txt', 'r')
        total_list = []
        for line in file:
            k = line.rstrip()
            total_list.append(k)
        file.close()
        return total_list

    def get_data(self,total_list):
        '''Function to check the list'''
        size = len(total_list)
        if size != 5:
            print('Incorrect no. of data in prepaid.txt\n')
            return -1
        for i in range(0, size):
            if total_list[i] == '':
                print('Data missing')
                break
        else:
            try:
                self.idn = int(total_list[0])
            except Exception as err:
                print(f'Error occured - {err}')
                print('Incorrect idn')
                return -1

            try:
                self.name = total_list[1]
                assert self.name.isalpha()
            except Exception:
                print('Error occured : ')
                print('Incorrect name')
                return -1

            try:
                self.email = total_list[2]
                assert re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)
            except Exception:
                print('Error occured : ')
                print('Incorrect email')
                return -1

            try:
                self.number = total_list[3]
                assert re.search(r'([789]\d{9}?)', self.number)
                assert len(self.number) == 10
            except Exception:
                print('Error occured : ')
                print('Incorrect phone no.')
                return -1

            try:
                self.balance = float(total_list[4])
                assert self.balance > -10
            except Exception as err:
                print(f'Error occured - {err}')
                print('Incorrect balance')
                return -1
            return 0

    def make_call(self,duration):
        '''Function to make call'''
        cost = duration * 0.5
        if self.balance<-10:
            print('Add balance to make a call\n')
            return -1
        if (self.balance-cost)<-10:
            print('Insufficient balance to make call\n')
            return -1
        else:
            self.balance-=cost
            return  self.balance

    def add_balance(self,money):
        '''Function to add balance'''
        if money<0:
            print('Please add money\n')
            return -1
        if self.balance<0:
            return -1
        else:
            self.balance += money
            print('Added successfully!\n')
            return self.balance


    def display_balance(self):
        '''Function to display balance'''
        print(f'The balance is {self.balance} Rs.\n')

    def prepaid_features(self):
        '''Function to display and implement features'''
        loop='Y'
        while loop in ('y','Y'):
            print(f'\nWelcome {self.name}\n')
            print('The features available are :')
            print('1. MAKE A CALL')
            print('2. ADD BALANCE')
            print('3. UPDATE EMAIL')
            print('4. CHECK BALANCE')
            print('5. DISPLAY INFO')
            key = input('Enter the no. of the the feature to use: ')
            if key == '1':
                try:
                    mins = float(input('Enter no. of mins of call: '))
                    assert mins > 0
                    PrepaidCustomer.make_call(self,mins)
                except Exception as err:
                    print(f'Error - {err}')
                    print('Please enter value appropriately')

            elif key == '2':
                try:
                    mon = float(input('Enter the amount you would like to add: '))
                    assert  mon > 0
                    PrepaidCustomer.add_balance(self,mon)
                except Exception as err:
                    print(f'Error - {err}')
                    print('Please enter value appropriately')

            elif key == '3':
                try:
                    mail=input('Enter the new email id: ')
                    assert re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', mail)
                    PrepaidCustomer.update_email(self,mail)
                except Exception:
                    print('Please enter valid email id\n')

            elif key == '4':
                PrepaidCustomer.display_balance(self)

            elif key == '5':
                PrepaidCustomer.display(self)

            else:
                print('Please enter the correct choice\n')
            loop=input('Would you like to go back to features page?(y/n): ')

    def display(self):
        '''Function to display info'''
        super().display()
        print(f'Balance = {self.balance} Rs.\n')


class PostpaidCustomer(Customer):

    '''Postpaid child class'''

    def __init__(self,idn=None,name=None,email=None,number=None,time=None):
        '''Postpaid class constructor'''
        super().__init__(idn, name, email, number)
        self.time=time


    def read_data(self):
        '''Function to get data of the user from backend(.txt file here)'''
        file = open('Postpaid.txt', 'r')
        total_list = []
        for line in file:
            k = line.rstrip()
            total_list.append(k)
        file.close()
        return total_list

    def get_data(self,total_list):
        '''Function to pass data'''
        size = len(total_list)
        if size != 5:
            print('Incorrect no. of data in prepaid.txt\n')
            return -1
        for i in range(0, size):
            if total_list[i] == '':
                print('Data missing')
                break
        else:
            try:
                self.idn = int(total_list[0])
            except Exception as err:
                print(f'Error occured - {err}')
                print('Incorrect idn')
                return -1

            try:
                self.name = total_list[1]
                assert self.name.isalpha()
            except Exception:
                print('Error occured : ')
                print('Incorrect name')
                return -1

            try:
                self.email = total_list[2]
                assert re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)
            except Exception:
                print('Error occured : ')
                print('Incorrect email')
                return -1

            try:
                self.number = total_list[3]
                assert re.search(r'([789]\d{9}?)', self.number)
                assert len(self.number) == 10
            except Exception:
                print('Error occured : ')
                print('Incorrect phone no.')
                return -1

            try:
                self.time = float(total_list[4])
                assert self.time >=0
                self.bill = self.time*0.4
            except Exception as err:
                print(f'Error occured - {err}')
                print('Incorrect time')
                return -1
            return 0

    def make_call(self,duration):
        '''Function to make call'''
        if duration<0:
            print('Enter correct value')
            return -1
        if self.time<0:
            return -1
        else:
            self.bill = self.time * 0.4
            self.time+=duration
            self.bill+=(duration*0.4)
            return self.bill

    def pay_bill(self,money):
        '''Function to pay bill'''
        self.bill=self.time*0.4
        if money<=self.bill and money>0:
            self.bill-= money
            self.time-= (money/0.4)
            print('Paid successfully\n')
            return self.bill
        if self.bill<-10:
            return -1
        else:
            print('Pay the bill as shown\n')
            return -1

    def display_bill(self):
        '''Function to diplay bill'''
        print(f'The remaining bill is {self.bill} Rs.')

    def postpaid_features(self):
        '''Function to display and implement features'''
        loop='Y'
        while loop in ('y','Y'):
            print(f'\nWelcome {self.name}\n')
            print('The features available are :')
            print('1. MAKE A CALL')
            print('2. PAY BILL')
            print('3. UPDATE EMAIL')
            print('4. CHECK BILL')
            print('5. DISPLAY INFO')
            key = input('Enter the no. of the the feature to use: ')
            if key == '1':
                try:
                    mins = float(input('Enter no. of mins of call: '))
                    assert mins > 0
                    PostpaidCustomer.make_call(self,mins)
                except Exception as err:
                    print(f'Error - {err}')
                    print('Please enter value appropriately')

            elif key == '2':
                try:
                    PostpaidCustomer.display_bill(self)
                    mon = float(input('Enter the amount you would like to pay: '))
                    assert  mon > 0
                    PostpaidCustomer.pay_bill(self,mon)
                except Exception as err:
                    print(f'Error - {err}')
                    print('Please enter value appropriately')

            elif key == '3':
                try:
                    mail=input('Enter the new email id: ')
                    assert re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', mail)
                    PostpaidCustomer.update_email(self,mail)
                except Exception:
                    print('Please enter valid email id\n')

            elif key == '4':
                PostpaidCustomer.display_bill(self)

            elif key == '5':
                PostpaidCustomer.display(self)

            else:
                print('Please enter the correct choice\n')
            loop=input('Would you like to go back to features page?(y/n): ')

    def display(self):
        '''Function to display info'''
        super().display()
        print(f'Time conversed = {self.time} mins\nRemaining Bill = {self.bill} Rs.')