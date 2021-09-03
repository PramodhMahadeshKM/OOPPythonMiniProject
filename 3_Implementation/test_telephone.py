from telephone import Customer
from telephone import PrepaidCustomer
from telephone import PostpaidCustomer

object1=PrepaidCustomer()
object2=PostpaidCustomer()
obj1=PrepaidCustomer(1001,'Pramodh Mahadesh','pram123@gmail.com','9900112233',100 )
obj2=PrepaidCustomer(99999,'Pramodh','123@gmail.com','7902112233',-1000 )
obj3=PostpaidCustomer(1001,'Pramodh Mahadesh','pram123@gmail.com','8001122334',100 )
obj4=PostpaidCustomer(1001,'Pramodh','pram123@gmail.com','9900112233',-1000 )
l1=['1001','Pramodh','abc@gmail.com','9900112233','100']        #all pass
l2=['qwer','Pramodh','a12bc@gma12il.com','8900112233','100']    #id fail
l3=['1001','123','abc@gmail.com','7900112233','100']            #name fail
l4=['1001','Pramodh','a#bc@gmail.com','900112233','100']        #email fail
l5=['1001','Pramodh','abc@gmail.com','6900112233','100']        #phone no fail
l6=['1001','Pramodh','abc@gmail.com','9900112233','-102.234']   #balance/time fail

def test_make_call():
    assert obj1.make_call(10)==95
    assert obj2.make_call(10)==-1
    assert obj3.make_call(10)==44
    assert obj4.make_call(10) == -1

def test_add_balance():
    assert obj1.add_balance(100)==195
    assert obj2.add_balance(100)==-1
    assert obj1.add_balance(-10)==-1

def test_pay_bill():
    assert obj3.pay_bill(4)==40
    assert obj4.pay_bill(10)==-1
    assert obj3.pay_bill(-10)==-1

def test_get_data():
    assert object1.get_data(l1)==0
    assert object1.get_data(l2) == -1
    assert object1.get_data(l3) == -1
    assert object1.get_data(l4) == -1
    assert object1.get_data(l5) == -1
    assert object1.get_data(l6) == -1
    assert object2.get_data(l2) == -1
    assert object2.get_data(l3) == -1
    assert object2.get_data(l4) == -1
    assert object2.get_data(l5) == -1
    assert object2.get_data(l6) == -1
