class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None # Stores a node, that corresponds to our first node in the list 
    self.tail = None # stores a node that is the end of the list
  
  def add_to_head(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new node
      self.head = new_node

  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)

    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point the node at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node

  # remove the head and return its value
  def remove_head(self):
    # if list is empty, do nothing
    if not self.head:
      return None
    # if list only has one element, set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    # otherwise we have more elements in the list
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 

  def contains(self, value):
    if self.head is None:
      return False
    
    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head

    while current_node is not None:
      # check if this is the node we are looking for
      if current_node.value == value:
        return True

      # otherwise, go to the next node
      current_node = current_node.next_node
    return False 
  def get_max(self):

    if self.head is None:
      return None

    current_node = self.head
    current_value = self.head.value

    while current_node is not None:
      if current_value < current_node.value:
        current_value = current_node.value
        current_node = current_node.next_node
    return current_value

    def reverse_list(self, node, prev):
        reversed_list = []        
        if self.next_node == None:
           # print reversed list
           for i in range(0, len(reversed_list)):
               print(reversed_list[i])
        else:
            #add newnode to reverse list
            if self.value == None:
                self.tail.add_to_tail(self.head)
            reverse_node = node(node.get_value)
            reverse_node = node.get_next(self.node_value) 
            else:
                self.tail.add_to_tail(self.next_node)           
            #newnode link is stacktop
            reverse_node.set_next = self.head
            # stacktop is newnode
            reverse_node.head = self.head
