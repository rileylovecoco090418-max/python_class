class Node: # The foundation of a linked list
    def __init__(self, data):
        self.data = data # Actual information
        self.next = None # Pointer to next node (starts as None)

    
class LinkedList: # The "Manager" class 
    def __init__(self):
        self.head = None # Initially empty

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
      
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head # Links to current first item
        self.head = new_node      # New node becomes the first item
        
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next: # Walk to the very end
            last = last.next
        last.next = new_node # Link the old tail to the new node

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next:  # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None 

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value '{value}' found at position {position}"
            current = current.next
            position += 1
        return f"Value '{value}' not found"

#  Test code
if __name__ == '__main__':
    # node1 = Node(1)
    # node2 = Node(2)
    # print(node1)
    # print(node2)

    # my_linked_list = LinkedList()
    # print(my_linked_list)

    # Create a new LinkedList instance
    llist = LinkedList()
    print(llist)

    # Insert each letter at the beginning using the method we created
    llist.insertAtBeginning('fox') 
    print(llist)
    llist.insertAtBeginning('brown') 
    print(llist)
    llist.insertAtBeginning('quick')  
    print(llist)
    llist.insertAtBeginning('the')  

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'
    # Print the list
    llist.insertAtEnd('jumps')
    print(llist)

      
      # Print the list before deletion
    print("List before deletion:")
    print(llist)

    # Deleting nodes from the beginning and end
    llist.deleteFromBeginning()
    llist.deleteFromEnd()

    # Print the list after deletion
    print("List after deletion:")
    print(llist)

       # Search for 'quick' and 'lazy' in the list
    print(llist.search('quick'))  # Expected to find
    print(llist.search('lazy'))   # Expected not to find






