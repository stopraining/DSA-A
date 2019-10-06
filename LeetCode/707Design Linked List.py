class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None :
            return -1
        
        if index == 0:
            return self.val  
        p = self.next
        i = 1
        while p != None:
            if i == index:
                return p.val  
            p = p.next       """p=self.next.next 下一個的下一個"""
            i += 1        """i每次都在往上加"""
        return -1
