def __myfunction(self):
    animal = "cat"
    print("in A class animal is:",animal)

def acessprivate(self):
    self.__myfunction()

class b(a):
    animal="dog"
    def myfunction(self):
        print("in b class animal is :",self.animal)

class c(b):
    def myfunction(self):
        a.acessprivate(self)
        super().myfunction()
a=c()
a.myfunction()
a.acessprivate()
a="rupendra"
def myname():
    global a
    print(a)
    a="raj"

    print(a)
myname()