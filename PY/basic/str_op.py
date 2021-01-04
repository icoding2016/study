
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