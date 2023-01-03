def f1(f):
    def wrapper(*args, **kwargs):
        print('Wrapper called')
        f(*args, **kwargs)
        print('Wrapper ended')
        
    return wrapper

@f1
#def function():
def function(p = None):
    print('I am a function')
    print('with parameter', p)

function(2)
