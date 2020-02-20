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

        # new_node = BinarySearchTree(value)
        # def go_left(left_self, new_node):
        #     if new_node.value < left_self.value:
        #         if left_self.left is not None:
        #             go_left(left_self.left, new_node)
        #         else:
        #             left_self.left = new_node
        #     else:
        #         if left_self.right is not None:
        #             go_right(left_self, new_node.value)
        #         else:
        #             left_self.right = new_node
        
        # def go_right(right_self, new_node):
        #     if new_node.value >= right_self.value:
        #         if right_self.right is not None:
        #             go_right(right_self.right, new_node)
        #         else:
        #             right_self.right = new_node
        #     else:
        #         if right_self.left is not None:
        #             go_left(right_self.left, new_node)
        #         else:
        #             right_self.left = new_node

        # if new_node.value < self.value:
        #     if self.left is not None:
        #         go_left(self.left, new_node)
        #     else:
        #         self.left = new_node
        # elif new_node.value >= self.value:
        #     if self.right is not None:
        #         go_right(self.right, new_node)
        #     else:
        #         self.right = new_node

        # REFACTORED
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value) # new_node
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value) # new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # to search a given key in Binary Search Tree,
        # we first compare it with root, if theh key is
        # present at root, we return root. If key is greater
        # than root's key, we recur for right subtree of
        # root node. Otherwise we recur for left subtree.
        
        # def check_target(self, target):
        #     bool_return = None
        #     if self.value == target:
        #         bool_return = True
        #     else:
        #         if self.value > target:
        #             if self.left is not None:
        #                 bool_return= check_target(self.left, target)
        #             else:
        #                 bool_return = False
        #         else:
        #             if self.right is not None:
        #                 bool_return = check_target(self.right, target)
        #             else:
        #                 bool_return = False
        #     return bool_return
        
        # return check_target(self, target)

        # Lecture
        # if self.value == target:
        #     return True

        # if target < self.value:
        #     if not self.left:
        #         return False
        #     else:
        #         return self.left.contains(target)
        # else:
        #     if not self.right:
        #         return False
        #     else:
        #         return self.right.contains(target)

        # REFACTORED
        if self.value == target:
            return True

        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go no further
        # max_val = 0

        # def get_max_val(node):
        #     nonlocal max_val
        #     if node.right is None:
        #         max_val = node.value
        #     else:
        #         get_max_val(node.right)
        
        # get_max_val(self)
        
        # return max_val

        # LECTURE

        # Ver. 1
        # while self.right is not None:
        #     self = self.right
        
        # return self.value

        # Ver.2
        # return self.right.get_max() if self.right else self.value

        # REFACTORED
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore,
        # then go back and go right
        # track = 0

        # def iterate(node, cb):
        #     nonlocal track
        #     if node.left is None and node.right is None:
        #         cb(node.value)
        #         return
        #     if node.left is None and node.right is not None:
        #         track += 1
        #         cb(node.value)
        #         iterate(node.right, cb)
        #         track -= 1
        #         return
        #     if node.left is not None:
        #         track += 1
        #         iterate(node.left, cb)
        #         cb(node.value)
        #         track -= 1
        #     if node.right is not None:
        #         track += 1
        #         iterate(node.right, cb)
        #         track -= 1
        #         if track != 0:
        #             cb(node.value)

        # iterate(self, cb)

        # Lecture Version
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
            

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        track = 0

        def iterate(node, cb):
            nonlocal track
            if node.left is None and node.right is None:
                # cb(f"left IS none and right IS none: {node.value}")
                cb(node.value)
                return
            if node.left is None and node.right is not None:
                track += 1
                # cb(f"left IS none right IS NOT none: {node.value}")
                cb(node.value)
                iterate(node.right, cb)
                track -= 1
                return
            if node.left is not None:
                # cb(f"node left IS NOT none: {node.value}")
                track += 1
                iterate(node.left, cb)
                cb(node.value)
                track -= 1
            if node.right is not None:
                # cb(f"node right IS NOT none: {node.value}")
                track += 1
                iterate(node.right, cb)
                track -= 1

        iterate(self, print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        my_queue = Queue()

        my_queue.enqueue(node)

        while my_queue.size > 0:
            node = my_queue.dequeue()
            if node.left is not None:
                my_queue.enqueue(node.left)
            if node.right is not None:
                my_queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make stack
        # put the root in the stack
        # while stack is not empty
        #     Pop the top item in the stack
        #     look right
        #     push right to the stack
        #     look left
        #     if there is a left, push to stack

        # call function on root
        #     if left
        #         call on left
        #     if right
        #         call on right
        my_stack = Stack()

        my_stack.push(node)

        while my_stack.size > 0:
            node = my_stack.pop()
            if node.left is not None:
                my_stack.push(node.left)
            if node.right is not None:
                my_stack.push(node.right)
            print(node.value)

        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(1)
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
# bst.in_order_print(bst)

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# # bst.in_order_print(bst)
# # bst.dft_print(bst)
# bst.bft_print(bst)