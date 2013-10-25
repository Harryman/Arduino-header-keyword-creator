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
# Copies comments from driectly above or on the same line as the function or above it 
#
# just to be on the safe side you should make copy of your exsisting header file, just incase
#
# creates keywords.txt with all of the public functions and libname
#
# All references in the library should look like the file name YOURLIB.cpp
# YOURLIB will be used to parse the file and find functions etc.
# include your YOURLIB.h before any other includes


import os.path

class headCreator():
	@staticmethod
	def sbtwn(str,idx,a,b):#this finds the instance of b first then rfinds a keep in mind
		end = str.find(b,idx)
		start = str.rfind(a,0,end)+len(a)
		ret = str[start:end],start,end
		return ret

	@staticmethod
	def getFunc(str,start,libName):
		if(str.find(libName+"::",start)>0):
			funcType = headCreator.sbtwn(str,start,'\n',libName+"::")
			func = headCreator.sbtwn(str,funcType[2],'::','{')
			keyword = headCreator.sbtwn(str,funcType[2],'::','(')
			tpnt = str.find('}',func[2])

			cmnts = ''
			pabvcmnts = str.find('//',str.rfind('\n',0,funcType[1]-1),funcType[1])
			if(pabvcmnts<0):
				pabvcmnts = str.find('*/',str.rfind('\n',0,funcType[1]-1),funcType[1])
				if(pabvcmnts > 0):
					abvcmnts = str[str.rfind('/*',0,pabvcmnts):pabvcmnts+2]
				else:
					abvcmnts = str[pabvcmnts:str.find('\n', pabvcmnts)]
				cmnts += abvcmnts 
			pcmnts = str.find('//',func[2],str.find('\n',func[2]))
			if(pcmnts>0):
				inlinecmnts = headCreator.sbtwn(str, pcmnts, '{', '\n')[0]
				cmnts += inlinecmnts
			ret = funcType[0]+func[0],keyword[0],tpnt,cmnts
			return ret
		else:
			ret = '','',-1
			return ret

	@staticmethod
	def createFiles(path):
		endPoint = path.find('.cpp')
		bpnt = path.rfind('\\',0,endPoint)+1
		libName = path[bpnt:endPoint]
		cppfile = open(path,'r')
		cpp = cppfile.read()
		cppfile.close()	

		if(os.path.isfile(path[0:bpnt]+libName+'.h')):
			ohfilef = open(path[0:bpnt]+libName+'.h')
			ohfile = ohfilef.read()
			ohfilef.close()
			tmp = ''
			tpnt = 0
			while(ohfile.find('/*',tpnt)>0):### Strips out all of the comments in header, simpler to match
				tmp += ohfile[tpnt:ohfile.find('/*',tpnt)]
				tpnt = ohfile.find('*/',tpnt)+2
			tmp += ohfile[tpnt:]
			tpnt = 0
			ohfile = ''
			while(tmp.find('//',tpnt)>0):#remove single line comments next
				ohfile += tmp[tpnt:tmp.find('//',tpnt)]
				tpnt = tmp.find('//',tpnt)
				tpnt = tmp.find('\n',tpnt)
			ohfile += tmp[tpnt:]


		h = cpp[0:cpp.find('#')-1]
		h +='\n#ifndef '+libName+'_h\n'
		h += '#define '+libName+'_h\n\n'
		h += '#include "Arduino.h"\n\n'
		h += 'class '+libName+'{\n  '
		pubvar = ''
		pubfunc = 'public:\n'
		privar = ''
		prifunc = '\n  private:\n'
		exclude = []
		tpnt = cpp.find(libName+'::'+libName)
		ret = headCreator.sbtwn(cpp,tpnt,'::','{')[0]+";\n"
		tpnt = tpnt + len(ret)
		pubfunc += '    '+ret
		txt = '##################################\n# Class Name\n##################################\n'+libName+'\tKEYWORD1\n\n##################################\n# Methods/Functions \n##################################\n'

		while(headCreator.getFunc(cpp,tpnt,libName)[2]>0):#gets functions
			tstr = headCreator.getFunc(cpp,tpnt,libName)
			if(tstr[0][0] !='_'):
				pubfunc += '    '+tstr[0]+';'+tstr[3]+'\n'
				txt = txt+tstr[1]+'\tKEYWORD2\n'
			else:
				prifunc += '    '+tstr[0]+';'+tstr[3]+'\n'
			func = headCreator.sbtwn(tstr[0],0,'(',')')[0]+',' #gets arguments adds comma for easy looping
			tidx = 0
			while((headCreator.sbtwn(func,tidx,' ',',')[2])>0): # goes through func args adding them to exclude
				args = headCreator.sbtwn(func,tidx,' ',',')
				tidx = args[2]+1
				exclude += [args[0]]
			tpnt = tstr[2]
		tpnt = 0


		while(cpp.find(' = ',tpnt)>0):#selects anything left of an assignment will not dupe
			var = headCreator.sbtwn(cpp, tpnt, ' ', ' = ')
			if(len(var[0])>len(headCreator.sbtwn(cpp,tpnt, '\t', ' = ')[0])):
				var = headCreator.sbtwn(cpp, tpnt, '\t', ' = ')
			tpnt = var[2]+1
			cnt = 0
			for a in exclude:
				if(var[0] == a):
					cnt += 1
			if(cnt == 0):
				exclude += [var[0]]
				try:
					tp = ohfile.find(var[0])
					if(tp > 0):
						t = headCreator.sbtwn(ohfile,tp-1,' ', ' ')
						if(len(t[0])>len(headCreator.sbtwn(ohfile,tp-1,'\t',' ')[0])):
							t = headCreator.sbtwn(ohfile,tp-1,'\t',' ')
						if(var[0][0] != '_'):
							pubvar += '    '+t[0]+' '+var[0]+';\n'
						else:
							privar += '    '+t[0]+' '+var[0]+';\n'
					else:
						if(var[0][0] != '_'):
							pubvar += '    //????'+var[0]+';\n' # if no var exsists you will have to set manually
						else:
							privar += '    //????'+var[0]+';\n'
				except NameError:
					if(var[0][0] != '_'):
						pubvar += '    //????'+var[0]+';\n' # if no file exsists you will have to set manually
					else:
						privar += '    //????'+var[0]+';\n'

		h += pubfunc +'\n'+ pubvar + prifunc +'\n'+ privar+'\n};\n\n#endif'

		hfile = open(path[0:bpnt]+libName+'.h','w')
		hfile.write('// file generated using https://github.com/Harryman/Arduino-header-keyword-creator\n\n'+h)
		hfile.close()
		txtfile = open(path[0:bpnt]+'keywords.txt','w')
		txtfile.write('# file generated using https://github.com/Harryman/Arduino-header-keyword-creator\n'+txt)
		txtfile.close()
