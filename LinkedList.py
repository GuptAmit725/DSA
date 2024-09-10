class Node:
    """
    Pass
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    This is a class for creating a LinkedList and its operations.
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_ll(self):
        """
       Print the elemnets. 
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        """
        :param value: value to be appended.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        """
        :param value: Value to be prepended
        """
        if index < 0 and index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        c = 1
        temp = self.head
        while c<index:
            temp = temp.next
            c += 1
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def prepend(self, value):
        """
        :param value: value to be inserted.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

        return True
    
    def pop(self):
        """
        Function to delete the last element.
        """
        pre = self.head
        temp = self.head
        if self.length==0:
            return None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

    def pop_first(self):
        """
        Pop the first element
        """
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.value

    def delete(self, index):
        """
        Function to delete the element at the given pos.
        :param pos: pos to delete.
        """
        if index < 0:
            return None
        elif index > self.length:
            return None
        elif index==0:
            self.pop_first()
        
        temp = self.head
        prev = self.head
        c = 0
        while c<index:
            prev = temp
            temp = temp.next
            c += 1
        prev.next = temp.next
        temp.next = None
        self.length -= 1
            



my_ll = LinkedList(11)
my_ll.append(12)
my_ll.append(13)
my_ll.append(14)
my_ll.append(15)

#my_ll.pop()
#my_ll.pop()
my_ll.prepend(19)
my_ll.insert(2,25)
my_ll.delete(2)
my_ll.print_ll()

















if __name__ == '__main__':
    pass