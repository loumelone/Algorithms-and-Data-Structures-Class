class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    
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

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, start, new_val): 
        if start.value < new_val: 
            if start.right:
                self.insert_helper(start.right, new_val)
            else:
                new_node = Node(new_val) 
                start.right = new_node
        else: 
            if start.left: 
                self.insert_helper(start.left, new_val)
            else: 
                new_node = Node(new_val)
                start.left = new_node 
                
    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, start, find_val): 
        if start.value == find_val: 
            return True
        elif start.value > find_val: 
            if start.left: 
                return self.search_helper(start.left, find_val)
            return False
        elif start.value < find_val:
            if start.right: 
                return self.search_helper(start.right, find_val)
            return False
            
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())
# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))