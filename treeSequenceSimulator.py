#######################################
# Alisha Rossi
# 11/6/2011
# treeSequenceSimulator.py
# reads a .tre file using ReadTree.py
# simulates sequence data and
# prints to file in phylip format.
#######################################

import random
import ReadTree
import sys

seqlen=500
treeFile=sys.argv[1] if len(sys.argv)>1 else 'treefile.tre'
phylipFile=sys.argv[2] if len(sys.argv)>2 else 'phylipfile.txt'

treeFile=open(treeFile)
lines=treeFile.readlines()

bases = 'GATC'

#make a random sequence of 500 nucleotides
def makeRandomSequence(): 
	sequence=''
	for i in range(seqlen):
		sequence+=random.choice(bases)	
	return sequence

def mutateSequence(sequence, branchLength):
	while(branchLength>0):
		branchLength -= random.expovariate(1)
		location=random.randrange(len(sequence))
		choice= random.choice(bases.replace(sequence[location], ''))
	return sequence[0:location]+choice+sequence[location+1:] 

def mutateChildren(node):
	if  node.leftChild != None :
		node.leftChild.sequence=mutateSequence(node.sequence, node.leftChild.branchLength)
		l=mutateChildren(node.leftChild)
	if node.rightChild != None:
		node.rightChild.sequence=mutateSequence(node.sequence, node.rightChild.branchLength)
		r=mutateChildren(node.rightChild)
	if node.leftChild == None and node.rightChild == None:	
		return [node.Name.ljust(10, ' ')+node.sequence+'\n']
	else: 
		return l+r

f=open(phylipFile, 'w')
rootSequence=makeRandomSequence()
#rootSequence='A'*20 #use this to see the mutations

for line in lines:
	tree=ReadTree.readTree(line)
	tree.root.sequence=rootSequence			#all root sequences same	
	#tree.root.sequence=makeRandomSequence() #use this to make all root sequences different
	phylipData=mutateChildren(tree.root)
	f.write(str(len(phylipData))+' '+str(seqlen)+'\n')
	f.writelines(phylipData)
	f.write('\n')

f.close()