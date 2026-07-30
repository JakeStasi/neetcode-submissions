# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        leftToRight = True
        res = []
        while q:
            lenQ = len(q)
            lvl = []
            for x in range(lenQ):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl.append(node.val)
            if not leftToRight:
                lvl.reverse()
            res.append(lvl)
            leftToRight = not leftToRight
        return res
                
        