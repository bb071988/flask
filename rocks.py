

def youRock(func):
    def inner(name):
        rock_value =  "{} you rock".format(func(name))
        return rock_value
    return inner

@youRock
def greet(name):
    return "Hello {}".format(name)

print "{}".format(greet("Sam"))
#print "{}".format(greet(test_name))

# if __name__ == "__main__":  This code block does not work - test_name undefined in print statement above.
#     print __name__
#     test_name = "Sam"
    
    
    