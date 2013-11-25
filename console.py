import os.path
import fCreate

head = fCreate.headCreator()

path = input('file:')
while(os.path.isfile(path)==False):
	path = raw_input('try again:')
head.createFiles(path)
input('done! press enter to exit')
