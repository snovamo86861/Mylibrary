"""1.Within script.py in the pane to the right, create an empty Node class.

Inside, define an __init__() method for the Node. It should take a value and a next_node.

next_node should default to None if not provided. These variables should be saved to self with corresponding key names.

Checkpoint 2 Passed


2.Define .get_value() and .get_next_node() methods. These should return the corresponding values from self.

Checkpoint 3 Passed


3.Define a .set_next_node() method that takes self and next_node as parameters and allows you to update the link to the next node.

Checkpoint 4 Passed

4.Outside the Node class, create an instance of Node called my_node with a value of 44.

Use .get_value() to print the value of my_node."""



# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
      self.next_node = next_node

my_node = Node(44) 
print(my_node.get_value())


#Linked List Implementation I

"""1. Within script.py in the pane to the right, create an empty LinkedList class.

Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node, so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided.

Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.

2.Define a .get_head_node() method that helps us peek at the first node in the list.

Inside the method, return the head node of the linked list."""


# Create your LinkedList class below:
class LinkedList:
  def __init__(self,  value=None):
     self.head_node = Node(value)
  def get_head_node(self):
    return self.head_node

#Linked Lists Implementation II

"""
1. Define an .insert_beginning() method which takes new_value as an argument.

Inside the method, instantiate a Node with new_value. Name this new_node.
Now, link new_node to the existing head_node.
Finally, replace the current head_node with new_node.

2.Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.

The method should traverse the list, beginning at the head node, and collect each node’s value in a string. Once the end of the list has been reached, the method should return the string.

You can use str() to convert integers to strings!

Be sure to add "\n" between values so that each value prints on a new line."""

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  #node impleentation II
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

# Node

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node



