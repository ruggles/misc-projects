# Python Directory Tree Builder

import os

def buildTree(treeName, directory, relative = False):
	
	treeFile = open(treeName, 'w')
	
	for root, filePath, fileName in os.walk(directory):
		if relative:
			root = root[len(directory):]
			
		treeFile.write(root + '\n')
		
	treeFile.close()
	
