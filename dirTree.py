# Python Directory Tree Builder

import os
import sys

def buildTree(directory, treeName):

	"""
	directory: Root directory for the tree.
	treeName: Name of the resulting file.
	"""
	
	treeFile = open(treeName, 'w')
	
	for root, filePath, fileName in os.walk(directory):
	
		level = root.replace(directory, '').count(os.sep)
		indent = ' ' * 4 * (level)
		treeFile.write('{}{}/'.format(indent, os.path.basename(root)) + '\n')
		
	treeFile.close()
	
if __name__ == "__main__":

	# argv[1] is the directory, argv[2] is the saved filename
	buildTree(sys.argv[1], sys.argv[2])
