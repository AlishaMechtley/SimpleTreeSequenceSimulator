# Instructions to run treeSequenceimulator.py


## HOW TO RUN

To run the assignment3.py program, type the name of the source file 
followed by the the name of the tree file you wish to run and the 
name you would like to call the output file.

```$python treeSimulator.py treefile outputfile```

If you do not specify a treefile or phylipfile, the default treefile is  
treefile.tre and the default outputfile is phylipfile.txt



HOW TO RUN the ReadWriteTree program 

Type the name of the source file 
followed by the the name of the tree file you wish to run. Note that
the tree file name must be in quotes.

python ReadWriteTree.py 'treefile1.txt'

If you do not specify a file, the default is treefile1.txt. Thus,
the following line of code will have the same result as the one 
above.

python ReadWriteTree.py

You can also execute the tree from within python or within ipython.
This will automatically use treefile1.txt unless you change the 
name of the file within the code directly. 

Example:
execfile('ReadWriteTree.py')

After you run the first tree you can run another tree by using the 
readWriteTree funtion and typing in name of the tree you wish to use.

readWriteTree('treefile2.txt')
readWriteTree('treefile3.txt')
readWriteTree('treefile4.txt')


HOW TO TRAVERSE THE TREE

To  traverse the tree, execute the file from within python or 
from within ipython. Starting at the root, use the getLeftChild and 
getRightChild functions to traverse the tree. Use the getName or 
getbranchLength to get the label or branch length of node (respectively).


Example 1: To traverse the tree in treefile1 to get tip names
execfile('ReadWriteTree.py')
root.getLeftChild().getLeftChild().getLeftChild().getName()
root.getRightChild().getName()
#This should return 'a' and 'd' respectively.


Example 2:To traverse the tree in treefile2, type into ipython
execfile('ReadWriteTree.py')
readWriteTree('treefile2.txt')
root.getLeftChild().getLeftChild().getLeftChild().getName()
root.getLeftChild().getLeftChild().getLeftChild().getbranchLength()
#This should return 'a' and 1.0 respectively.

root.getRightChild().getName()
root.getRightChild().getbranchLength()
#This should return 'd' and 1.5 respectively.


IMPROVEMENTS

Using the tree class to save tree data would be the next 
improvement to make. Recursively being able to parse the tree with 
a nodeParser function would be another improvement. The code to 
begin working on these improvements are commented out at the bottom 
of the source file.