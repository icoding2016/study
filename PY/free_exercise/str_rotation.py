# String Rotation: Assume you have a method isSubString which checks if one word is a substring
# of another. 
# Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
# call to isSubString (e.g., "waterbottle" is a rotation of" erbottlewat").
#
#
# Idea: 
#   Use isSubString to find the start location, the check if the part before it match the part after in another string
#   [def]abc
#        ^
#        abc[def]
# 
# 
# Solution: simply do isSubstring(slsl, s2).           @_@
#
def isSubString(s1,s2):
    '''If s1 is a substring of s2'''


def isRotation(s1,s2):  
    offset=None
    if len(s1) != len(s2):
        return False
    if s1 == s2:      # same is not considered as 'rotation'
        return False
    i = 1
    while i < len(s1):
        if s1[:i] in s2:
            if i == len(s1) - 1:
                # same
                return False
            i += 1
            continue
        else:
            offset = i
            break
    
    part2 = s1[offset:]
    print(offset, part2)
    if part2 == s2[:len(part2)]:
        return True
    else:
        return False

def test():
    print(isRotation('abcdef', 'efabcd'))
    # print(isRotation('abcdef', 'abcdef'))    
    # print(isRotation('abcdef', 'efgabcd'))
    # print(isRotation('abcdef', 'efbacd'))

test()