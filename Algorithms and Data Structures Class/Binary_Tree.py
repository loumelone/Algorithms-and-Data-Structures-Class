#DFS 
#Inorder Traversal (4 2 5 1 3)
#Alogrithm goes as follows: 
    #Traverse the left subtree i.e. call Inorder(left-subtree)
    #visit the root 
    #Traverse the right substree i.e. call Inorder(right-subtree)

#preorder traversal (D, B, A, C, E, F)
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.preorder_search(self.root, find_val):
            return True 
        return False


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = None
        array = self.preorder_print(self.root, traversal)
        for i in range(0, len(array)):
            if i == 0: 
                string = "{}".format(array[i])
            else: 
                string += "-{}".format(array[i])
        return string 

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        print(start.value)
        if start.value == find_val: 
            return True 
        if start.left: 
            if self.preorder_search(start.left, find_val):
                return True
        if start.right: 
            if self.preorder_search(start.right, find_val):
                return True
        return False



    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if traversal is None: 
            traversal = [start.value]
        else:
            traversal.append(start.value)
        if start.left: 
            self.preorder_print(start.left, traversal)
        if start.right: 
            self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())