#!/bin/sh

filelist=("/bin/ipktest_bin" 
 "/sbin/ipktest_sbin" 
 "/lib/ipktest_lib" 
 "/usr/bin/ipktest_usrbin" 
 "/usr/sbin/ipktest_usrsbin" 
 "/usr/lib/ipktest_usrlib" 
 "/etc/cdcs/conf/ipktest_etccdcsconf" 
 "/opt/ipktest_opt"
 ".")

echo "ipk installation finished..."
echo "checking installed files:"
for x in ${filelist[*]}
do
  printf "  %s: %s\n" $x $( (test -e $x >/dev/null) && { echo "Success"; } || { echo "Fail";} )
done


