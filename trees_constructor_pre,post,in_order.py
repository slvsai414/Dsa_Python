class TreeNode:
    def __init__(self, val):
        self.data = val 
        self.left = None 
        self.right = None 

       #preOrder
def printPreorder(root):
    if root == None:
        return

    print(root.data)
    printPreorder(root.left)
    printPreorder(root.right)

     #postOrder
def printPostorder(root):
    print()
    def helper(root):
        if root == None:
            return 
        helper(root.left)
        helper(root.right)
        print(root.data)
    helper(root)

     #inOrder
def printInorder(root):
    print()
    def helper1(root):
        if root == None:
            return 
        helper1(root.left)
        print(root.data)
        helper1(root.right)
    helper1(root)
    



obj1 = TreeNode(10)
obj1.left = TreeNode(12)
obj1.right = TreeNode(20)
obj1.left.left = TreeNode(11)
obj1.left.right = TreeNode(70)
obj1.right.right = TreeNode(87)
obj1.right.left = TreeNode(90)



obj2 = TreeNode(16)
obj2.left = TreeNode(12)
obj2.right = TreeNode(22)
obj2.left.left = TreeNode(111)
obj2.left.right = TreeNode(700)
obj2.right.right = TreeNode(878)
obj2.right.left = TreeNode(901)

obj3 = TreeNode(161)
obj3.left = TreeNode(121)
obj3.right = TreeNode(221)
obj3.left.left = TreeNode(1112)
obj3.left.right = TreeNode(7002)
obj3.right.right = TreeNode(8783)
obj3.right.left = TreeNode(9015)


printPreorder(obj1)
printPostorder(obj2)
printInorder(obj3)