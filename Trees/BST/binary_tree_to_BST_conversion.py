"""

Given a Binary Tree, convert it to a Binary Search Tree. The conversion must be done in such a way that keeps the original structure of Binary Tree.
Examples.

Example 1
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7


Example 2
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30

"""


"""
SOLUTION

Solution
Following is a 3 step solution for converting Binary tree to Binary Search Tree.
1) Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
2) Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
3) Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(root):
    pass


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data)
    printInorder(root.right)




print ("Inorder traversal of the constructed tree: ")
printInorder(root)

