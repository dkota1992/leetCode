class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.current = ListNode(None)
    
    def addNode(self,value):
        if self.current.val = None:
            self.current.val = value
        else:
            self.current.next = ListNode(value)
            self.current.val = ListNode(value).val
