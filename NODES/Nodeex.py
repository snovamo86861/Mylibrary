class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
"""1. Define an .add_to_head() method that takes self and new_value as parameters.

Inside, create:

A new_head Node that takes new_value as a parameter
A current_head Node that’s set to the list’s head
2.If there is a current head to the list:

Set current_head‘s previous node to new_head
Set new_head‘s next node to current_head
Remember to use the Node class’s .set_prev_node() and .set_next_node() methods.

3. Outside of the if statement, set the list’s head to new_head.

4. Lastly, if the list doesn’t have a tail, set the list’s tail to the new head.
"""
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head
   