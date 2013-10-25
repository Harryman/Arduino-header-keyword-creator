import os.path
import fCreate

head = fCreate.headCreator()

path = raw_input('file:')
while(os.path.isfile(path)==False):
	path = raw_input('try again:')
head.createFiles(path)
raw_input('done! press enter to exit')
