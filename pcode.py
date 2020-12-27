'''def f1(**n):
    for k,v in n.items():
        print(k,v,sep="......")
f1(name='rahul',cls=12)
print()
print()
print()
f1(name="rahul",title="kumar",dept='cse')
#******************************************



GARBAGE COLLECTOR
___RESPONSIBLE FOR DESTROYING OBJECT----------

gc modcule
import gc



gc.inenabled()--->returns True or False
gc.enable()
gc.desable()







#DEstructors concept_______________________________

syntax---  __del__(self):
    -----responsible for cleanup activities to an object before destruction



  
import time
class Test1:
    def __init__(self):
        print("initialisation......")
    def __del__(self):
        print("cleanup activity going on....")
T=Test1()
T=None
time.sleep(10)
print("Object destroyed by gc")
#**************************************************

import time
class Test1:
    def __init__(self):
        print("initialisation......")
    def __del__(self):
        print("cleanup activity going on....")
T=Test1()
S=T
R=S
del T
print("T destroyed")
time.sleep(5)
del S
print("S destroyed")
time.sleep(5)
print("R to be destroyed and now no reference to object left")
del R
print("R destroyed and now no reference to object left")
time.sleep(10)
print("Object destroyed by gc")

#*****************************************************************
NOTE---

This example illustrates that After the end of every program garbage collector is automatically called to collect the garbage
and gc calls the constructor for cleanup activities.


import time
class Test1:
    def __init__(self):
        print("initialisation......")
    def __del__(self):
        print("cleanup activity going on....")
l=[Test1(),Test1(),Test1()]
print("End of program")
time.sleep(5)


output----
 
initialisation......
initialisation......
initialisation......
End of program
cleanup activity going on....
cleanup activity going on....
cleanup activity going on....

'''
print("Subbranch1")







