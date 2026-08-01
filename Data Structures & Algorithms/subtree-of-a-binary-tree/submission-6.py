class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the subRoot is empty then we return True because one of our subTrees from our leaf
        # nodes will also be empty
        if not subRoot:
            return True
        # if the root is empty and the subRoot is non Empty then they are not equal so it is F
        if not root:
            return False
        # Now we check if they are the same tree
        if self.sameTree(root,subRoot):
            return True
        # Check if there is a subtree to the left or right of our root
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))


    def sameTree(self,root,subRoot):
        # If both trees are empty then they are equal
        if not root and not subRoot:
            return True
        # If the nodes are equal recursively call and compare the left and right sides of the
        # trees
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and 
            self.sameTree(root.right,subRoot.right))   
        # One of the trees is empty and the other is non empty so that means it is 
        # not the same tree so we return False           
        return False