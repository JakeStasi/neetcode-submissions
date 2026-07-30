# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        # the queue at any time will hold a level of the tree
        while queue:
            rightSide = None 
            qLen = len(queue)
            # Loop thru each level
            for i in range(qLen):
                # Pop the first node in the queue because we dont need it, we need the last one or the right most side
                node = queue.popleft()

                if node:
                    # Store the node because on the last iteration of the for loop it will be our right most node
                    rightSide = node
                    # Add the children of the node we popped
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                # When it is done looping thru, append it at each level
                res.append(rightSide.val)
        return res