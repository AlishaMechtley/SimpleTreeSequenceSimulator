#######################################
# Alisha Rossi
# 11/6/2011
# ReadTree.py
# used with treeSequenceSimulator.py
# reads a .tre file
#######################################


class Node:
	def __init__(self, Name = None): # constructor
		#instance variables
		self.setName(Name)
		#self.Name=None
		self.leftChild = None
		self.rightChild = None
		self.parent = None
		self.branchLength = None
		self.sequence=None
	#setters	
	def setName(self,Name):
		self.Name = Name
	def setbranchLength(self,branchLength):
		self.branchLength = branchLength
	def setLeftChild(self, leftChild):
		self.leftChild = leftChild
		leftChild.parent = self
	def setRightChild(self, rightChild):
		self.rightChild = rightChild
		rightChild.parent = self
	def setParent(self, parent):
		self.parent = parent
	def setSequence(self, sequence):
		self.sequence=sequence

	#getters	
	def getName(self):
		return self.Name
	def getbranchLength(self):
		if self.branchLength==None:
			print "There is no branch length at this node."
		else:
			return self.branchLength
	def getLeftChild(self):
		return self.leftChild
	def getRightChild(self):
		return self.rightChild
	def getParent(self):
		return self.parent
	def getSequence(self):
		return self.sequence
	
	#Node class functions	
	def printName(self):
		return str(self.Name)
	def downpass(self):								# downpass algorithm p13 of first lecture notes "Evolutionary Trees"
		if  self.leftChild != None :
			l = self.leftChild.downpass()
		if self.rightChild != None:
			r = self.rightChild.downpass()
		if self.leftChild == None and self.rightChild == None:	
			if self.branchLength==None:
				return self.Name					# return just of name a tip if there is no branch length
			else:									# otherwise return name and branch length of a tip node
				return self.Name + ':' + str(self.branchLength)		 
		else:
			if self.branchLength== None:
				return '('+ l  + ',' + r + ')'		# returns subtrees recursively to get full tree
			else:									# returns branchlengths too if present
				return '('+ l  + ',' + r + ')' + ':' + str(self.branchLength) 
class Tree:
	def setRoot(self, root):
		self.root= root
	def getRoot(self):
		return self.root
	def douppass(self):
		self.root.uppass()		
	def dodownpass(self): # not working? use tree.root.downpass
		self.root.downpass()

def getNextStr(fData, fDataIndex):
	currentString = ''; spclChar = '(:,;)' 			# finds ( then : and so on
	if  spclChar.find(fData[fDataIndex])!=-1: 		# when special character present
		return [fData[fDataIndex],fDataIndex+1] 	# return the current character and the index of that character
	while spclChar.find(fData[fDataIndex])==-1:		# string.find returns -1 when there is nothing there
		currentString = currentString+fData[fDataIndex] #we have something else
		fDataIndex = fDataIndex+1					# increment to go to next character in the string
	return [currentString.strip(),fDataIndex]

##global variable declaration and intialization


def readTree(fData):
	fDataIndex = 0
	myNode=Node()
	root=Node()
	root.setName('root')
	[currStr,fDataIndex] = getNextStr(fData,fDataIndex)

	while currStr != ';': 							# until the end of the line
		if currStr=='(':
			if fDataIndex==1:
				myNode=root			
			else: 
				parNode=Node()						#create a node
				if myNode.getLeftChild()==None:		# If there is no left child
					myNode.setLeftChild(parNode)	# set left child to the new node					
				else:
					myNode.setRightChild(parNode)		
				myNode=parNode
		elif currStr==',':
			if myNode!=root:
				myNode=myNode.parent
				
		elif currStr==')':
			myNode=myNode.parent
			
		elif currStr==':':
			[currStr,fDataIndex] = getNextStr(fData,fDataIndex) # get the colon
			
			myNode.branchLength = float(currStr)
		else:
			tipNode=Node()
			tipNode.setName(currStr)
			if myNode.getLeftChild()==None:
				myNode.setLeftChild(tipNode)
			else:
				myNode.setRightChild(tipNode)	
			myNode=tipNode
			
		[currStr,fDataIndex] = getNextStr(fData,fDataIndex) 
		
	t = Tree()
	t.setRoot(root)
	return t
	
	#print root.downpass() + ';'


###################################################################
##Improvements and Future Code to incorporate

#def nodeParser(currentString,fDataIndex):
#	[currStr,fDataIndex] = getNextStr(fData,fDataIndex) #getNextStr?
#	if currStr=='(':
#		[node1,fDataIndex]=nodeParser(currentString,fDataIndex)
#		[node2,fDataIndex]=nodeParser(currentString,fDataIndex+1)
#		myNode= Node()
#		myNode.setLeftChild(node1)
#		myNode.setRightChild(node2)
#		return[myNode, fDataIndex+1]
#
#	myNode=Node(currStr)
#	return[myNode,fDataIndex]
#nodeParser(fData,fDataIndex)

## Within Node class
	#def uppass(self):
	#	self.printName()
	#	if  self.leftChild != None :
	#		self.leftChild.uppass()
	#	if self.rightChild != None:
	#		self.rightChild.uppass()





