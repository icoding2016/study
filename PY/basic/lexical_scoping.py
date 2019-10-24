'''
Lexical Scoping
A nested Python function can refer to variables defined in enclosing functions, but can not assign to them. 
Variable bindings are resolved using lexical scoping, that is, based on the static program text. 
Any assignment to a name in a block will cause Python to treat all references to that name as a local variable, 
even if the use precedes the assignment. If a global declaration occurs, the name is treated as a global variable.
'''



x = 10
def f1():
    print(x)

def f2():
    print(x)    # raise error.   x is considered a local variable
    x=0       

    
f1()    
f2()
