class CallDetail:
    def __init__(self,l1,l2,l3,l4):
        self.callingNumber = l1
        self.calledNumber = l2
        self.duration = l3
        self.callType = l4
    def print1(self):
        print('Calling Number-',self.callingNumber,'\nCalled Number-', self.calledNumber,'\nCall Duration-', self.duration,'\nCall Type-',self.callType,'\n')
    

class Util:
    def __init__(self):
        self.list_of_call_objects = None
    def parse_customer(self, list_of_call_string):
        list1 = []
        for i in range(len(list_of_call_string)):
            list1= list_of_call_string[i].split(",")
            callingNumber = list1[0]
            calledNumber = list1[1]
            duration = list1[2]
            callType = list1[3]
            c1 = CallDetail(callingNumber,calledNumber,duration,callType)
            c1.print1()

call1 ='9154637482,7458302943,15,STD'
call2 ='3509875098,5097325097,25,ISD'
call3 ='3522930875,2345982475,30,STD'

list_of_call_string=[call1, call2, call3]
Util().parse_customer(list_of_call_string)
