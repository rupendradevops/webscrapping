import numpy as np
class parentCls:
    array1 = np.array([[11, 13, 14, 15], [12, 13, 15, 16]])
    array2 = np.array([[21, 31, 41, 51], [21, 31, 51, 61]])
    array3 = np.array([[31, 41, 51, 61], [21, 31, 51, 61]])


    def myfunction1(self):
        print("default array1 details are :", self.array1)
        # myarray=self.array1*2
        # print("myarray value is:",myarray)

    def myfunction2(self):
        print("default array1 details are :", self.array2)
        # myarray1=self.array2+22
        # print("myarray1 value is:", myarray1)


    def myfunction3(self):
        print("default array1 details are :", self.array3)
        # myarray2 = self.array2 / 22
        # print("myarray2 value is:", myarray2)

class childcls(parentCls):
    def myfunction4(self):

        array1=np.array([["banana","apple"],
                         ["dog","cat"]])
        print("after changes my array1 details:",array1)
        print("default array2 value is:",self.array2)
        print("default array3 value is:", self.array3)

myobj=childcls()
myobj.myfunction1()
myobj.myfunction2()
myobj.myfunction3()
myobj.myfunction4()