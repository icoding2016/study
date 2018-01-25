#!/bin/sh

file1="/bin/ipktest-bin" 
file2="/sbin/ipktest-sbin" 
file3="/lib/ipktest-lib" 
file4="/usr/bin/ipktest-usrbin" 
file5="/usr/sbin/ipktest-usrsbin" 
file6="/usr/lib/ipktest-usrlib" 
file7="/etc/cdcs/conf/ipktest-etccdcsconf" 
file8="/opt/ipktest-opt" 

FILECOUNT=8

echo "Installation finished, checking files:"
echo "--------------------------------------"

ret=0

#for ((i=1; i<=$FILECOUNT; i++))
#for filename in "file$(seq 1 $FILECOUNT)";
i=1
while [ $i -le $FILECOUNT ];
do
  filename=$(eval echo \$file${i})
  if [ -e $filename ]; 
  then 
    str="Yes";
  else
    str="No";
    ret=1
  fi
  printf "  %s:  -- %s\n" $filename $str 
  i=$(($i+1))
done

echo "--------------------------------------"
printf "Result: "; 
if [ $ret -eq 0 ]; then echo "Pass"; else echo "Fail"; fi

exit $ret

