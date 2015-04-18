@addfive
def sum(a,b):
    return a + b

def addfive(func):
    
    def inner(a,b):
        newvalue = func(a,b) + 5
        return newvalue
        
    return inner
    
print sum(2,3)

@addthml
def greetSam()