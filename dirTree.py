# Python Directory Tree Builder

import os

def buildTree(treeName, directory):
	
	treeFile = open(treeName, 'w')
	
	for root, filePath, fileName in os.walk(directory):
	
		level = root.replace(directory, '').count(os.sep)
		indent = ' ' * 4 * (level)
		treeFile.write('{}{}/'.format(indent, os.path.basename(root)) + '\n')
		
	treeFile.close()
	
