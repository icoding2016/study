

longstr1 = ('This is an example of a long string '
           'which is devided into multiple lines in the code '
           'and use bracket to group into one string (which is required to avoid compiler error)'
           'but actually should display in one line.\n')

longstr_in_obj = ('a tuple', 1, 'a long string in a tuple '
    'while is splitted into multiple lines in the code, but'
    ' should display as one line. '
    'In this case, the bracket is not required.\n'
)


mlstr = """This is an example of
a multi line string.
  This line has 2 space in the lead.
The last line.\n"""

mlstr2 = ('This is another example of a multi line string.\n'
          'Which does\'t use triple-quatation,but the \'\\n\' '
          'expression to change lines.\n'
          '  This line has 2 space in the lead.\n'
          'The last line.\n')

s='abcd'
# str  join
l = [x for x in s]
print(l)
s1=''
print(s1.join(l))

print(s+'x')          # >> abcx
print(s.join('x'))    # >>  x ,   that's a wrong way to use join
print(''.join(l))     # >> abc,   that's a right way to use join,   
print('-'.join(l))    # >> a-b-c, that's a right way to use join,   
ipsection = ['10','20','1','1']
print('.'.join(ipsection))

# cut a piece off the str
s1 = s[:3] + s[4:]    # >> abce
print(s1)


# str format
for i in range(1,11):
    for j in range(1,11):
        print("{:<6}".format(i*j), end='')
    print('')

print('{:b}'.format(10))

for i in range(1,10, 2):
    print(i)


# sub string  -- in
def subString(s1,s2):
    if s1 in s2:
        return True
    return False    
print(subString('abc', 'fullabcd'))
print(subString('abc', 'fullabd'))

s = 'abcdefghijk'
if 'a' in s:
    print('a in ',s)
    

# sub string  --  find
def findSubString(s1,s2):
    return s2.find(s1)

print(findSubString('abc', 'fullabcd'))


# remove substring from a string
s1='ababcab'
s2='ab'
print('remove ',s2, ' from ',s1, ': ', s1.replace(s2,''))

# convert str to int
s = '123'
print('int for for {} is {}'.format(s, int(s)))

# The better way to format a str
# f'python 3 f format has the best performance'
# e.g.
#   var1 = 'v1'
#   var2 = 10
#   f' some vars: {var1}, {var2} ' 
#   
# >>> import timeit
# >>> timeit.timeit("""name = "Eric"
# ... age = 74
# ... '%s is %s.' % (name, age)""", number = 10000)
# 0.003324444866599663
 
# >>> timeit.timeit("""name = "Eric"
# ... age = 74
# ... '{} is {}.'.format(name, age)""", number = 10000)
# 0.004242089427570761
 
# >>> timeit.timeit("""name = "Eric"
# ... age = 74
# ... f'{name} is {age}.'""", number = 10000)
# 0.0024820892040722242

print(longstr1)
print(longstr_in_obj[2])
print(mlstr)
print(mlstr2)
print()