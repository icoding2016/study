"""
generator send() method & yield

generator use
  - send() to receive an input
  - yield to generate an output and pend for next input (to trigger another generation)

When you use send and expression yield in a generator, you're treating it as a coroutine; 
a separate thread of execution that can run sequentially interleaved but not in parallel with its caller.

so when use 'yield x' in a generator, it output x and ransfers control back to the caller, waiting for an input on the input slot.
then if the caller use generator.send(s), 's' object is put into generator's input slot, that gives the control back to the generator,
which will continue the execution from the yield expression it stopped at.  
if here we use  i = yield, or i = yield x, then the input 's' is received by i

next(generator) is the same as generator.send(None)

"""
def gen_num():
    n = 0
    while True:
        i = yield n
        if i == 'stop':
            break
        n += 1

def test_gen_num():
    gen = gen_num()
    for i in range(10):
        n = next(gen)
        print(n)
        # if i >= 7:
        #     gen.send('stop')

def check_pwd(pwd="default_password"):
    while True:
        attempt = yield
        yield attempt==pwd

def test_check_pwd(pwd="default_password"):
    attempts = ["I", "am", "trying", "to", "hack", "the", "password"]
    checker = check_pwd(pwd)    # generator
    next(checker)
    for atmpt in attempts:
        if checker.send(atmpt):
            return "Got it"
    return "Failed to hack"
        

test_gen_num()
ck1 = test_check_pwd();  print(ck1)
ck2 = test_check_pwd('password');  print(ck2)

