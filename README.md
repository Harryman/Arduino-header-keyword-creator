Arduino-header-keyword-creator
==============================
The purpose of this script to make writing arduino libraries less painful by creating the header file and keywords.txt file automatically from your library. It will pull includes, functions, and variables with types*(see instructions)

This is the first python script I've written so feel free to show me what I did wrong

Instructions
----------------------------------------------------
* .cpp file must use explicit { }
* the variable type are pulled from the exsisting .h file
* if there is no exsisting .h file you will have to manually enter the datatype
*	Copies comments directly from the top 
* creates keywords.txt with all of the public functions and libname
* All references in the library should look like the file name YOURLIB.cpp YOURLIB will be used to parse the file and find functions etc. include your YOURLIB.h before any other includes

-------------------------------------------------------

If you find utility or vaule in it please return the favor via bitcoin: 17E66DJ5hEx6wSFxnSvYM7jgXY2PYBVrth

Or if you just want to donate to my beer fund: 151sgJ4z2tNGzVFJHGyBAd8H4F4RT62ebQ
