'''
recursion:
Binary Search Tree
Searching a key
To search a given key in Bianry Search Tree, we compare it with root and decide accordingly...


'''

class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None


def search(root,key):
    if root.val==key:
        return root
    elif root.val<key:
        ##check right subtree
        return search(root.right,key)
    elif root.val>key:
        ##check left subtree
        return search(root.left,key)
    else:
        return None


def insert(root,node):
    if root.val < node.val:
        if root.right is None:
            root.right=node
        else:              
            insert(root.right,node)
    elif root.val > node.val:
        if root.left is None:
            root.left=node
        else:              
            insert(root.left,node)




def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

    
##main
r=Node(100)
insert(r,Node(300))
insert(r,Node(20))
insert(r,Node(40))

'''
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
'''


inorder(r)
