#!/bin/sh

filelist=(
 "/bin/ipktest_bin" 
 "/sbin/ipktest_sbin" 
 "/lib/ipktest_lib" 
 "/usr/bin/ipktest_usrbin" 
 "/usr/sbin/ipktest_usrsbin" 
 "/usr/lib/ipktest_usrlib" 
 "/etc/cdcs/conf/ipktest_etccdcsconf" 
 "/opt/ipktest_opt"
 )
#filelist=('.' '..')

echo "Installation finished, checking files:"
echo "--------------------------------------"

ret=0

for x in ${filelist[*]}
do
  if [ -e $x ]; 
  then 
    str="Yes";
  else
    str="No";
    ret=1
  fi
  printf "  %s:  -- %s\n" $x $str 
done

echo "--------------------------------------"
printf "Result: "; 
if [ $ret -eq 0 ]; then echo "Pass"; else echo "Fail"; fi

exit $ret

