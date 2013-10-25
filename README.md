Arduino-header-keyword-creator
==============================
The purpose of this script to make writing arduino libraries less painful by creating the header file and keywords.txt file automatically from your library. It will pull Top comments, includes, functions along with their adjacent comments, and variables with types*(see instructions)

This is the first python script and Sublime Text plugin I've made so the code is a bit of a mess.

####This is available through Package Control 
I haven't tested it on ST3 but it does work on ST2 for windows. I'm pretty sure this will bug out and not work Linux because of different path separators.

Instructions
----------------------------------------------------
* .cpp file must use explicit { }
* Private functions & variables must start with and underscore(_) i.e. _privar
* the variable type are pulled from the exsisting .h file
* just to be on the safe side you should make copy of your exsisting header file, just incase
* if there is no exsisting .h file you will have to manually enter the datatype
*	Copies comments directly from the top 
* Copies comments from driectly above or on the same line as the function or above it 
* creates keywords.txt with all of the public functions and libname
* All references in the library should look like the file name YOURLIB.cpp YOURLIB will be used to parse the file and find functions etc. include your YOURLIB.h before any other includes
* Use library https://github.com/Harryman/simple-buttons-arduino as an example of what the formatting looks like if you are still unsure how it works


-------------------------------------------------------

If you find utility or vaule in it please return the favor via bitcoin: 17E66DJ5hEx6wSFxnSvYM7jgXY2PYBVrth

Or if you just want to donate to my beer fund: 151sgJ4z2tNGzVFJHGyBAd8H4F4RT62ebQ
