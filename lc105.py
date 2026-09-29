class Solution:
    class TreeNode:
        ...

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index = {value: i for i, value in enumerate(inorder)}
        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootValue = preorder[preIndex]
            preIndex += 1

            def TreeNode(rootValue):
                ...

            root = TreeNode(rootValue)

            mid = index[rootValue]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)