# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder_list = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            inorder_list.append(node.val)
            inorder(node.right)
        inorder(root)
        def listHasDupliate(input_list):
            return len(input_list) != len(set(input_list))
        
        sorted_list = sorted(inorder_list)
        if listHasDupliate(sorted_list):
            return False
        return inorder_list == sorted_list
            
