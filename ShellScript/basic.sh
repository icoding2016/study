#!/usr/bin/bash
#
# Basic shell operations
#

echo -x     # output all the shell command lines to std

# echo
# echo by itself displays a line of text. It will take any thing within the following "..." two quotation marks, literally, and just print out as it is. 
# However with echo -e you're making echo to enable interpret backslash escapes. So with this in mind here are some examples
# INPUT: echo "abc\n def \nghi" 
# OUTPUT:abc\n def \nghi
# 
# INPUT: echo -e "abc\n def \nghi"
# OUTPUT:abc
#  def 
# ghi


# output all odd numbers between [1,99]
for i in {1..99}; do if [ $(($i%2)) == 1 ]; then echo $i;fi; done

# get the name xxx input from user and output "Welcom xxx"
read var;echo "Welcome $var";

# Given two integers,  and , find their sum, difference, product, and quotient.
read x;read y;echo $(($x+$y)); echo $(($x-$y)); echo $(($x*$y)); echo $(($x/$y));


# Given two integers, x and y, identify whether x<y or x>y or x=y.
# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y
read x; read y;
if [[ $x > $y ]]
  then echo "X is greater than Y";
elif [[ $x < $y ]]
  then echo "X is less than Y";
else
  echo "X is equal to Y";
fi


# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.
# Input Format
# One character
# Constraints
# The character will be from the set .
read var;
if [[ ${var^^} == "Y" ]]
    then echo "YES";
elif [[ ${var^^} == "N" ]]
    then echo "NO";
fi


# Given three integers (x, y, and z) representing the three sides of a triangle,
#   identify whether the triangle is scalene, isosceles, or equilateral.
#   If all three sides are equal, output EQUILATERAL.
#   Otherwise, if any two sides are equal, output ISOSCELES.
#   Otherwise, output SCALENE.
# Input Format
#   Three integers, each on a new line.
# Constraints
#   The sum of any two sides will be greater than the third.
# Output Format
#   One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
read x;
read y;
read z;
if [[ $x == $y && $x == $z ]]
  then echo "EQUILATERAL";
elif [[ $x == $y || $x == $z || $y == $z ]]
  then echo "ISOSCELES";
else
  echo "SCALENE";
fi


# A mathematical expression containing +,-,*,^, / and parenthesis will be provided. 
# Read in the expression, then evaluate it. Display the result rounded to  decimal places.
# Constraints: 
#   All numeric values are <= 999.
# Sample Input 1:  5+50*3/20 + (19*2)/7
# Sample Input 2:  -105+50*3/20 + (19^2)/7
# Sample Input 3:  (-105.5*7+50*3)/20 + (19^2)/7
# Sample Output 1: 17.929
# Sample Output 2: -45.929
# Sample Output 3: 22.146
read exp; echo $exp | bc -l | xargs printf "%.3f"
  # bc -l   # --mathlib     Define the standard math library.



# input n, calculate sum([1:n])
read n;count=1;s=0;while [[ $count -le $n ]];do s=$((s+count)); echo "$count,$s";count=$((count+1));done;echo "sum=$s";



# Given N integers, compute their average, rounded to three decimal places.
# Input Format
#     The first line contains an integer, .
#     Each of the following  lines contains a single integer.
# Output Format
#     Display the average of the  integers, rounded off to three decimal places.
# Input Constraints
#     ( refers to elements of the list of integers for which the average is to be computed)

# read N;count=0;s=0;while [[ $count -lt $N ]];do read n;s=$((s+n)); count=$((count+1));done;
read N;
s=0
count=0
while [[ $count -lt $N ]];
  do
    read n;
    count=$((count+1));
    s=$((s+n));
  done
echo "scale=4;$s/$count" | bc -l | xargs printf "%.3f"



# https://www.hackerrank.com/challenges/fractal-trees-all/problem
# Creating a Fractal Tree from Y-shaped branches
# This challenge involves the construction of trees, in the form of ASCII Art.
# We have to deal with real world constraints, so we cannot keep repeating the pattern infinitely. 
# So, we will provide you a number of iterations, and you need to generate the ASCII version
# of the Fractal Tree for only those many iterations (or, levels of recursion)








# $() vs ${}
#
# $(command) is “command substitution”. it runs the command, captures its output, and inserts that into the command line that contains the $(…); e.g.,
# e.g.
#   $ ls -ld $(date +%B).txt
#   -rwxr-xr-x  1 Noob Noob    867 Jul  2 11:09 July.txt
#
# ${…} lets you get the value of a variable, it also support some str operation with specific flags 
# e.g.
#   $ animal=cat
#   $ echo ${animal}s
#   cats
# 
# ! in ${...} introduced a level of variable indirection
# e.g.
#  $ animal=cat
#  $ echo $animal
#  cat
#  $ cat=tabby
#  $ echo $cat
#  tabby
#  $ echo ${!animal}
#  tabby 
#
# ${#...}  -- count the len of the str
# e.g.
#   $ echo ${#animal}   # $animal = cat
#   3    
#
# ${var1#${var2}} -- to return the remaining part of var1 after removing the lead var2 in var1
# e.g.
#   $ version_prefix=ver_
#   $ version=ver_3.2.0
#   $ echo ${version#${version_prefix}}
#   3.2.0
#
# ${parameter…something_else} constructs
#

version_prefix=ver_
version=ver_3.2.0
echo ${version#${version_prefix}}




