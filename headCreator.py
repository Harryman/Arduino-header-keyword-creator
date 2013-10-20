# Developed by:
# Harrison Stahl https://github.com/Harryman
# The Everything Corp

#	If you find utility or vaule in it please return the favor via bitcoin:
# 17E66DJ5hEx6wSFxnSvYM7jgXY2PYBVrth
#INCLUDE ALL OF THE ABOVE WHEN COPYING^^^^^^^

#################### INSTRUCTIONS ########################
# This is the first python script I've written so feel free to show me what I did wrong
#
# .cpp file must use explicit {}
#
# the variable type are pulled from the exsisting .h file
#
# if there is no exsisting .h file you will have to manually enter the datatype
# 
#	Copies comments directly from the top 
#
# creates keywords.txt with all of the public functions and libname
#
# All references in the library should look like the file name YOURLIB.cpp
# YOURLIB will be used to parse the file and find functions etc.
# include your YOURLIB.h before any other includes



import os.path
def sbtwn(str,idx,a,b):#this finds the instance of b first then rfinds a keep in mind
	end = str.find(b,idx)
	start = str.rfind(a,0,end)+len(a)
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

path = input('file:')
endPoint = path.find('.cpp')
bpnt = path.rfind('\\',0,endPoint)+1
libName = path[bpnt:endPoint]

if(os.path.isfile(path[0:bpnt]+libName+'.h')):
	ohfilef = open(path[0:bpnt]+libName+'.h')
	ohfile = ohfilef.read()
	ohfilef.close()

cppfile = open(path,'r')
cpp = cppfile.read()
cppfile.close()

h = cpp[0:cpp.find('#')-1]
h +='\n#ifdef '+libName+'_h\n'
h += '#define '+libName+'_h\n\n'
h += '#include "Arduino.h"\n\n'
h += 'class '+libName+'{\n  '
pubvar = ''
pubfunc = 'public:\n'
privar = ''
prifunc = '\n  private:\n'
exclude=[]
tpnt = cpp.find(libName+'::'+libName)
ret = sbtwn(cpp,tpnt,'::','{')[0]+";\n"
tpnt = tpnt + len(ret)
pubfunc += '    '+ret
txt = libName+' KEYWORD3\n\n'

while(getFunc(cpp,tpnt)[2]>0):#gets public functions
	tstr = getFunc(cpp,tpnt)
	if(tstr[0][0] !='_'):
		pubfunc += '    '+tstr[0]+';\n'
		txt = txt+tstr[1]+' KEYWORD2\n'
	else:
		prifunc += '    '+tstr[0]+';\n'
	func = sbtwn(tstr[0],0,'(',')')
	func = func[0]+','	#gets arguments adds comma for easy looping
	tidx = 0
	while((sbtwn(func,tidx,' ',',')[2])>0): # goes through func args adding them to exclude
		args = sbtwn(func,tidx,' ',',')
		tidx = args[2]+1
		exclude += args[0]
	tpnt = tstr[2]
tpnt = 0

while(sbtwn(cpp, tpnt, ' ', ' = ')[2]>0):#selects anything left of an assignment will not dupe
	var = sbtwn(cpp, tpnt, ' ', ' = ')
	tpnt = var[2]+1
	cnt = 0
	for a in exclude:
		if(var[0] == a):
			cnt += 1
	if(cnt == 0):
		exclude += [var[0]]
		try:
			t = ohfile.find(var[0])
			if(t > 0):
				t = sbtwn(ohfile,t-1,' ', ' ')
				if(var[0][0] != '_'):
					pubvar += '    '+t[0]+' '+var[0]+';\n'
				else:
					privar += '    '+t[0]+' '+var[0]+';\n'
		except NameError:
			if(var[0][0] != '_'):
				pubvar += '    ????'+var[0]+';\n' # if no file exsists you will have to set manually
			else:
				privar += '    ????'+var[0]+';\n'

h += pubfunc +'\n'+ pubvar + prifunc +'\n'+ privar

hfile = open(path[0:bpnt]+libName+'.h','w')
hfile.write(h)
hfile.close()
txtfile = open(path[0:bpnt]+'keywords.txt','w')
txtfile.write(txt)
txtfile.close()
