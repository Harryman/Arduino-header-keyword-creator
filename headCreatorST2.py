
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


import sublime, sublime_plugin
import fCreate

head = fCreate.headCreator()

class CreateHeaderCommand(sublime_plugin.TextCommand):
	def run(self, veiw):
		path = self.view.file_name()
		if(path.find('.cpp')>0):
			fCreate.headCreator.createFiles(path)
			sublime.status_message('Files Created Successfully')
		else:
			sublime.status_message('This is not a valid file')

