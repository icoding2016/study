#!/bin/sh


# Bash arrays have numbered indexes only, but they are sparse, ie you don't have to define all the indexes. 
# An entire array can be assigned by enclosing the array items in parenthesis:
#    arr=(Hello World)
# Individual items can be assigned with the familiar array syntax (unless you're used to Basic or Fortran):
#    arr[0]=Hello   arr[1]=World
# But it gets a bit ugly when you want to refer to an array item:
#    echo ${arr[0]} ${arr[1]}
# The braces are required to avoid conflicts with pathname expansion.

#
# Array function in shell script
# 
#   ${arr[*]}         # All of the items in the array
#   ${!arr[*]}        # All of the indexes in the array
#   ${#arr[*]}        # Number of items in the array
#   ${#arr[0]}        # Length of item zero
#

# examples:

filelist=(""/bin/ipktest_bin" \
 "/sbin/ipktest_sbin" \
 "/lib/ipktest_lib" \
 "/usr/bin/ipktest_usrbin" \
 "/usr/sbin/ipktest_usrsbin" \
 "/usr/lib/ipktest_usrlib" \
 "/etc/cdcs/conf/ipktest_etccdcsconf" \
 "/opt/ipktest_opt")

echo "Array size of filelist $(#{filelist[*]})"
echo "members:"
for x in ${filelist[*]}:
do
    printf "  %s\n" $x
done

 
