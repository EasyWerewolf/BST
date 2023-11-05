# Imports
import csv


# Storm class object initialization
class Storm:
    def __init__(self, name, year, category, cost):
        self.name = name
        self.year = int(year)
        self.category = category
        self.cost = cost

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost


# Node class initialization
class Node:
    def __init__(self, storm, left=None, right=None, parent=None):
        self.storm = storm
        self.left = left
        self.right = right
        self.parent = parent

    def set_storm_object(self, storm):
        self.storm = storm

    def set_left_node(self, left):
        self.left = left

    def set_right_node(self, right):
        self.right = right

    def get_storm(self):
        return self.storm

    def get_left_node(self):
        return self.left

    def get_right_node(self):
        return self.right

    def get_parent_node(self):
        return self.parent


# Storm Tree initialization
class StormTree:
    def __init__(self):
        self.root = None

    def insert_storm(self, storm):
        if self.root is None:
            self.root = Node(storm)
        else:
            self.__insert_storm(storm, self.root)

    def __insert_storm(self, storm, current_node):  # Private version of the insert storm method
        if storm.year < current_node.get_storm().year:
            if current_node.get_left_node() is None:
                current_node.set_left_node(Node(storm, parent=current_node))
            else:
                self.__insert_storm(storm, current_node.get_left_node())
        else:
            if current_node.get_right_node() is None:
                current_node.set_right_node(Node(storm, parent=current_node))
            else:
                self.__insert_storm(storm, current_node.get_right_node())

    def traverse(self, traversal_type):  # This function will choose which traversal method to use
        if traversal_type == 1:  # Inorder
            self.__inorder_traversal(self.root)
        elif traversal_type == 2:  # Preorder
            self.__preorder_traversal(self.root)
        elif traversal_type == 3:  # Postorder
            self.__postorder_traversal(self.root)

    def __inorder_traversal(self, node):  # Private method for inorder traversal
        if node:
            self.__inorder_traversal(node.get_left_node())
            print(node.get_storm().get_name())
            self.__inorder_traversal(node.get_right_node())

    def __preorder_traversal(self, node):  # Private method for preorder traversal
        if node:
            print(node.get_storm().get_name())
            self.__preorder_traversal(node.get_left_node())
            self.__preorder_traversal(node.get_right_node())

    def __postorder_traversal(self, node):  # Private method for postorder traversal
        if node:
            self.__postorder_traversal(node.get_left_node())
            self.__postorder_traversal(node.get_right_node())
            print(node.get_storm().get_name())

    def breadth_first_search(self):  # Custom function for breadth-first search
        if self.root is None:
            return

        result = []  # Initialize an empty array which will hold the values for each node
        queue = [self.root]

        while queue:
            node = queue.pop(0)  # Remove the first element
            result.append(node.get_storm().get_name())

            if node.get_left_node():
                queue.append(node.get_left_node())

            if node.get_right_node():
                queue.append(node.get_right_node())

        return result


# Main Application
# Read data from CSV file and make the StormTree
storm_tree = StormTree()

with open('cyclones_1900_2010_bst.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name, year, category, cost = row
        storm = Storm(name, year, category, cost)
        storm_tree.insert_storm(storm)

# Perform 4 traversals:
print("Inorder Traversal:")
storm_tree.traverse(1)

print("\nPreorder Traversal:")
storm_tree.traverse(2)

print("\nPostorder Traversal:")
storm_tree.traverse(3)

print("\nBreadth-First Search:")
result = storm_tree.breadth_first_search()
for storm_name in result:
    print(storm_name)
