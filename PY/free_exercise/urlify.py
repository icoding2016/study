# Given an URL, replace the spaces with '%20' in place. 
# Assme the string has sufficient space at the end to hold the additional character, 
# and the true length of the URL is know (N) 
# e.g
# "Mr. John Smith!               "  (N=17) -> "Mr.%20John%20Smith!%20%20    "
#                  ^N

# note, the in-place replace in Python is impossible, python str is immutable
#  If the string is mutable, then count the number of space => calculate the length of new string.
#  re-fill the string from back to front


def urlify(url, len):
    new_url = url.replace(' ', '%20')
    return new_url



def test():
    new_url = urlify('Mr. John Smith!  ', 30)
    print(new_url)
    
test()


