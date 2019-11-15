import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        # >= go right
        new_node = BinarySearchTree(value)
        def go_left(left_self, new_node):
            if new_node.value < left_self.value:
                if left_self.left is not None:
                    go_left(left_self.left, new_node)
                else:
                    left_self.left = new_node
            else:
                if left_self.right is not None:
                    go_right(left_self, new_node.value)
                else:
                    left_self.right = new_node
        
        def go_right(right_self, new_node):
            if new_node.value >= right_self.value:
                if right_self.right is not None:
                    go_right(right_self.right, new_node)
                else:
                    right_self.right = new_node
            else:
                if right_self.left is not None:
                    go_left(right_self.left, new_node)
                else:
                    right_self.left = new_node

        if new_node.value < self.value:
            if self.left is not None:
                go_left(self.left, new_node)
            else:
                self.left = new_node
        elif new_node.value >= self.value:
            if self.right is not None:
                go_right(self.right, new_node)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # to search a given key in Binary Search Tree,
        # we first compare it with root, if theh key is
        # present at root, we return root. If key is greater
        # than root's key, we recur for right subtree of
        # root node. Otherwise we recur for left subtree.
        
        def check_target(self, target):
            bool_return = None
            if self.value == target:
                bool_return = True
            else:
                if self.value > target:
                    if self.left is not None:
                        bool_return= check_target(self.left, target)
                    else:
                        bool_return = False
                else:
                    if self.right is not None:
                        bool_return = check_target(self.right, target)
                    else:
                        bool_return = False
            return bool_return
        
        return check_target(self, target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go no further
        max_val = 0

        def get_max_val(node):
            nonlocal max_val
            if node.right is None:
                max_val = node.value
            else:
                get_max_val(node.right)
        
        get_max_val(self)
        
        return max_val


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore,
        # then go back and go right
        track = 0

        def iterate(node, cb):
            nonlocal track
            if node.left is None and node.right is None:
                cb(node.value)
                return
            if track == 0 and node.left is None and node.right is not None:
                cb(node.value)
            if node.left is not None:
                track += 1
                iterate(node.left, cb)
                cb(node.value)
                track -= 1
            if node.right is not None:
                track += 1
                iterate(node.right, cb)
                track -= 1
                if track != 0:
                    cb(node.value)

        iterate(self, cb)
            

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(5)
# # print(bst)
# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(6)
# bst.insert(5)
# bst.insert(5)
# arr = []
# cb = lambda x: arr.append(x)
# bst.for_each(cb)
# print(arr)