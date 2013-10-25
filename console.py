import os
import os.path
import headCreator


path = raw_input('file:')
while(os.path.isfile(path)==False):
	path = raw_input('try again:')
headCreator.createFiles(path)
raw_input('done! press enter to exit')
