# twister example

import functools

# first examples
# def twist(function):
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         print "Shep Schwab shopped at Scott's Schnapps shop"
#         function(*args, **kwargs)
#     return wrapper

# more complicated examples
def twist(twister):
    print twister
#    print function - I can't print function and haven't explicity passed so how does it get into twist so decorator can access it?
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print twister
            function(*args, **kwargs)
        return wrapper
    return decorator

@twist("She sells sea shells on the sea shore") # the @ implicitly mmust pass in the spoon function or maybe not?
def spoon():
    print "A well-boiled icicle"


# @twist
# def spoon():
#     print "A well-boiled icicle"

#print "{}".format(spoon())

print spoon()