# Developed by:
# Harrison Stahl https://github.com/Harryman
# The Everything Corp
#
# Liscense: CC Attribution

# .cpp file must use explicit {}
# All references in the library should look like the file name YOURLIB.cpp
# YOURLIB will be used to parse the file and find functions etc.
# include your YOURLIB.h before anyother includes

def sbtwn(str,idx,a,b):#this finds the instance of b first then rfinds a keep in mind
	end = str.find(b,idx)
	start = str.rfind(a,idx,end)+len(a)
	ret = str[start:end],start,end
	return ret

def getFunc(str,start):
	if(str.find(libName+"::",start)>0):
		funcType = sbtwn(str,start,'\n',libName+"::")
		func = sbtwn(str,funcType[2],'::','{')
		keyword = sbtwn(str,funcType[2],'::','(')
		tpnt = str.find('}',func[2])
		ret = funcType[0]+func[0],keyword[0],tpnt
		return ret
	else:
		ret = '','',-1
		return ret

path = input('path:')
endPoint = path.find('.cpp')
bpnt = path.rfind('\\',0,endPoint)+1
libName = path[bpnt:endPoint]
cpp = open(path,'r')
cpp = cpp.read()
h = cpp[0:cpp.find('#')-1]
h = h+'\n#ifdef '+libName+'_h\n'
h = h+'#define '+libName+'_h\n\n'
h = h+'#include "Arduino.h"\n\n'
h = h+'class '+libName+'{\n  public:\n'

tpnt = cpp.find(libName+'::'+libName)
ret = sbtwn(cpp,tpnt,'::','{')[0]+";\n"
tpnt = tpnt + len(ret)
h = h+'    '+ret
txt = libName+' KEYWORD3\n\n'
while(getFunc(cpp,tpnt)[2]>0):
	tstr = getFunc(cpp,tpnt)
	print(tstr)
	if(tstr[0][0] !='_'):
		h = h+'    '+tstr[0]+';\n'
		txt = txt+tstr[1]+' KEYWORD2\n'
	tpnt = tstr[2]
tpnt = 0
h = h+'\n  private:\n'
while(getFunc(cpp,tpnt)[2]>0):
	tstr = getFunc(cpp,tpnt)
	if(tstr[0][0] == '_'):
		h = h+'    '+tstr[0]+';\n'
	tpnt = tstr[2]

hfile = open(path[0:bpnt]+libName+'_test.h','w')
hfile.write(h)
hfile.close()
txtfile = open(path[0:bpnt]+'keywords_test.txt','w')
txtfile.write(txt)
txtfile.close()
