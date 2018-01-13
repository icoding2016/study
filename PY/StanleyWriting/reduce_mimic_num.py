#  coding=utf-8

from __future__ import print_function



import os
import codecs
import sys

html_head=u'''
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Stanley Writing</title>
<style>
body,div,p,ul,li{ padding:0; margin:0; list-style:none;}
div{ width:938px; margin:0 auto;padding-left:2px; }
li{ float:left; width:80px; height:80px; font-family:"楷体","楷体_gb2312"; font-size:58px; text-align:center; line-height:85px; background:url(images/bg2.jpg); margin:4px 0px 5px -2px; color:#b8b8b8; }
li.f{color:#000;margin-left:-0px}
li.svg{line-height:72px;}
li svg{ magin:8px; vertical-align:middle;}
.afterpage{ page-break-after:always;}
</style>
</head>

<body>
<div>
<ul>
'''

html_tail=u'''
</ul>
</div>
<div style="display: none;">
	<script src="./temp_files/hm.js.download"></script><script>
	var _hmt = _hmt || [];
	(function() {
	  var hm = document.createElement("script");
	  hm.src = "//hm.baidu.com/hm.js?26806bf65928ca10b21fdd33824e109f";
	  var s = document.getElementsByTagName("script")[0];
	  s.parentNode.insertBefore(hm, s);
	})();
	</script>
</div>
'''

page_row_num = 13

input_sfile_writing_def = "StanleyWriting.txt"
output_filename_writing = "StandleyWriting.html"
input_sfile_story_def = "StanleyStory.txt"
output_filename_story = "StandleyStory.html"
input_list = u''

def gen_line_writing(word):
    li_str = '<li class="f">' + word + '</li>'
    for i in range(0,6):
        li_str += '<li>' + word + '</li>'
    for i in range(0,5):
        li_str += '<li></li>'
    print(li_str)
    return li_str

def gen_html(src='', outfn=output_filename_writing):
    if outfn is "":
        raise "NULL file name for output!"
        return
    if os.path.exists(outfn):
        r = ''
        print('File exit, overwrite it...')
        '''
        r = input('File exit, do you want to overwrite it?[y/n]: ')
        if r.lower() == 'n':
            print("Please choose a new name and try again...")
            return
        '''

    count_line=0
    buf = ''
    buf += html_head
    if src == '':         #default
        src = input_list
    for c in src:
        buf += gen_line_writing(c)
        count_line += 1
    buf += html_tail

    print('_'*40)
    print("Character#: %d" % len(src))
    print("line#: %d" % count_line)
    print("page#: %2f, lines on last page: %d" % (float(len(src)/page_row_num), len(src)%page_row_num))

    with codecs.open(outfn, mode="w+", encoding='utf-8') as of:
        #of.encoding("utf-8")
        of.write(buf)
        print("Written to file %s" % outfn)
        of.close()

def read_file_intobuf(filename=input_sfile_writing_def):
    global input_list
    if not os.path.exists(filename):
        print("File %s not exit..Abort." % filename)
        return False

    with codecs.open(filename, mode='r', encoding='utf-8') as f:
        input_list = f.read()
        #input_list.encode("utf-8")

    return input_list



if __name__ == "__main__":
    #gen_line_writing("cc".encode("utf-8"))
    #print("sys encoding %s" % ( sys.getdefaultencoding()))

    if read_file_intobuf():
        gen_html()