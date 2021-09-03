from telephone import Customer
from telephone import PrepaidCustomer
from telephone import PostpaidCustomer

while True:
    print('*********  WELCOME *********')
    print('Press 1 for Prepaid services')
    print('Press 2 for Postpaid services')
    print('Press 0 to Exit')
    choice=input('Enter the choice: ')
    if choice=='1':
        li_1=[]
        obj_1=PrepaidCustomer()
        li_1=obj_1.read_data()
        obj_1.get_data(li_1)
        obj_1.prepaid_features()
    elif choice=='2':
        li_2=[]
        obj_2=PostpaidCustomer()
        li_2 = obj_2.read_data()
        obj_2.get_data(li_2)
        obj_2.postpaid_features()
    elif choice=='0':
        print('Thank You!!\n')
        break
    else:
        print('Enter the correct choice\n')
