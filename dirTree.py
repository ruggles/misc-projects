# Python Directory Tree Builder

import os

def buildTree(treeName, directory):
	
	treeFile = open(treeName, 'w')
	
	for root, directory, fileName in os.walk(directory):
		treeFile.write(root + '\n')
		
	treeFile.close()
	
