# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbersRe(self,root,sum,current):
        if not root:
            return sum
        current = current*10 + root.val
        if(not root.left and not root.right):
            sum = sum + current
            return sum

        sum = self.sumNumbersRe(root.left,sum,current)
        sum = self.sumNumbersRe(root.right,sum,current)
        current = current/10

        return sum
        
    def sumNumbers(self, root):
        sum = 0
        current = 0
        if not root:
            return sum
        return self.sumNumbersRe(root,sum,current)
    
