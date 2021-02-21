class Node:
    
    def __init__(self, node):
        self.node = node
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, node):
        if self.top_node is None:
            self.top_node = Node(node)
        else:
            temp = self.top_node
            self.top_node = Node(node)
            self.top_node.next = temp

    def top(self):
        return self.top_node.node
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            temp = self.top_node.node
            self.top_node = self.top_node.next
            return temp

    def isEmpty(self):
        if self.top_node is None:
            return True
        else:
            return False