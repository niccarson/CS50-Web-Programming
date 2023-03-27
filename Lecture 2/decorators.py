# decorators are functions that take functions as input and returns a modified version of that function
# functional programming is supported by python, where functions themselves are values and can be input and output

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

#add a decorator using @
@announce
def hello():
    print("SAMPLE DECORATOR")

hello()

# can be used a lot during web development, like using a decorator to check for login status 
# only allow certain functions to run when logged in 