"""
Write a function (in pseudo-code) called dumpList that takes as its parameters a string 
and a reference to an arbitrarily complex nested list and prints the value of each list element on a separate line. 

The value of each line should be preceded by the string and numbers indicating the depth and index of the element in the list. 
Assume that the list contains only strings and other nested lists.

Let’s take a look at an example of what we want exactly in the dumpList function. 
Suppose that you are given the following nested list. 
A nested list is just a list that contains other lists as well – so in the list below you see that it also contains the lists [‘a’,’b’,’c’] and [‘eggs’] :

List = ['a string', ['a','b','c'], 'spam', ['eggs']] 

And, suppose that the string passed in to the dumpList function is called ‘Foo’, 
then the output of dumpList(‘Foo’, List) would look like this:

Foo.0:  a string
Foo.1.0: a
Foo.1.1 : b
Foo.1.2: c
Foo.2: spam
Foo.3.0: eggs

"""

# This function dumps the origenal reprentation of a nested list L
def dumpList(name:str, L:list) -> None:
    index = 0
    for v in L:
        if isinstance(v, list):
            dumpList(f'{name}.{index}', v)
        else:
            print(f'{name}.{index}: {v}')
        index += 1

# This function dumps the string reprentation of a nested list s
def dumpListStr(name:str, s:str) -> int:
    """Dump the input string representation of nested list
    Args:
        name: the name of the list
        s: the string representation of the nested list
        index: current index   
    """
    if not s or len(s)<2:
        return len(s)
    assert s[0]=='[', f'invalid list {s}'
    index = 0
    quote_counter = 0
    value = ''
    i = 1
    while i < len(s)-1:
        c = s[i]
        if c == "'":
            if quote_counter == 0:
                value = ''    # reset value
                quote_counter = 1
            else:    # quote_counter == 1:
                print(f"{name}.{index}: {value}")
                quote_counter = 0
        elif c == ',' and quote_counter == 0:
            index += 1
            value = ''
        elif c == '[' and quote_counter==0:
            reached = dumpListStr(f'{name}.{index}', s[i:])
            i += reached
            # bracket_counter += 1
        elif c == ']' and quote_counter==0:
            i += 1
            break
        else:
            value += c
        i += 1
    return i-1



def test():
    data = ['a string', ['a','b','c'], 'spam', ['eggs']]
    print('---- dumpList (for original list)----')
    dumpList('Foo', data)

    print('---- dumpListStr (for string expression of list)----')
    data = "['a string', ['a','b','c'], 'spam', ['eggs']]" 
    dumpListStr('Foo', data)


test()
