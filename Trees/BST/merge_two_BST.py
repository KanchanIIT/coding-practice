"""
Merge Two Balanced Binary Search Trees

You are given two balanced binary search trees e.g., AVL or Red Black Tree. Write a function that merges the two given balanced BSTs into a balanced binary search tree. Let there be m elements in first tree and n elements in the other tree. Your merge function should take O(m+n) time.

####################################################
Method 1 (Insert elements of first tree to second)
Take all elements of first BST one by one, and insert them into the second BST. Inserting an element to a self balancing BST takes Logn time (See this) where n is size of the BST. So time complexity of this method is Log(n) + Log(n+1) … Log(m+n-1). The value of this expression will be between mLogn and mLog(m+n-1). As an optimization, we can pick the smaller tree as first tree.
####################################################

####################################################
Method 2 (Merge Inorder Traversals)
1) Do inorder traversal of first tree and store the traversal in one temp array arr1[]. This step takes O(m) time.
2) Do inorder traversal of second tree and store the traversal in another temp array arr2[]. This step takes O(n) time.
3) The arrays created in step 1 and 2 are sorted arrays. Merge the two sorted arrays into one array of size m + n. This step takes O(m+n) time.
4) Construct a balanced tree from the merged array using the technique discussed in this post. This step takes O(m+n) time.

Time complexity of this method is O(m+n) which is better than method 1. This method takes O(m+n) time even if the input BSTs are not balanced.
####################################################

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =  None

class Solution:
    def __init__(self):
        self.all_nodes = list()

    def printInorder(self, root):
        if root is None:
            return
        self.printInorder(root.left)
        print(root.val)
        self.printInorder(root.right)

    def ReturnInorder(self, root):
        if root is None:
            return
        self.ReturnInorder(root.left)
        self.all_nodes.append(root.val)
        self.ReturnInorder(root.right)

    def BST_Insert(self, root, value):
        if root==None:
            return
        elif value>root.val and root.right!=None:
            self.BST_Insert(root.right, value)
        elif value<root.val and root.left!=None:
            self.BST_Insert(root.left, value)
        elif value>root.val and root.right==None:
            root.right = Node(value)
            return
        elif value<root.val and root.left==None:
            root.left = Node(value)


    def merge_trees(self, Tree1, Tree2):
        self.ReturnInorder(Tree1)
        for i in self.all_nodes:
            self.BST_Insert(Tree2, i)

        self.printInorder(Tree2)


Tree1 = Node(2)
Tree1.left = Node(1)
Tree1.right = Node(3)

Tree2 = Node(5)
Tree2.left = Node(4)
Tree2.right = Node(6)

SOLUTION = Solution()
SOLUTION.merge_trees(Tree1, Tree2)