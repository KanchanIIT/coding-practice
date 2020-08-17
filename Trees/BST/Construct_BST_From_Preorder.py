"""
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
     10
   /   \
  5     40
 /  \      \
1    7      50

"""
## InOrder print would result a sorted array

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(pre, l, h):
    if l>h:
        return None
    node = Node(pre[l])
    if l==h:
        return node
    # node = Node(pre[l])
    # if (h-l)==1:
    #     return node

    for i in range(l+1,h+1):
        if pre[i]>pre[l]:
            break
    node.left = constructTree(pre, l+1, i-1)
    node.right = constructTree(pre, i,h)
    return node


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data)
    printInorder(root.right)


pre = [100, 50, 40, 30, 45, 60, 120, 110, 130, 125, 135] #[10, 5, 1, 7, 40, 50]
root = constructTree(pre, 0, len(pre)-1)

print ("Inorder traversal of the constructed tree: ")
printInorder(root)

## output
"""
Inorder traversal of the constructed tree: 
1 5 7 10 40 50
"""