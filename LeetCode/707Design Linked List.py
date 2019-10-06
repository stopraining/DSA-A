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
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val=val
            return
        
        else:
            temp = self.val
            self.val = val
            n = self.next
            self.next = MyLinkedList()
            self.next.val = temp         """先將原本的保留，輸入要加入的值，再將原本的放回去"""
            self.next.next = n
            return
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.val=val
            return
        
        p=self
        i=1
        while p.next != None :
            p=p.next
            i+=1
        p.next=MyLinkList()   """run到p.next想要的位置的next值就是我們要輸入的值(加在尾巴)"""
        p.next.val=val     
        return

